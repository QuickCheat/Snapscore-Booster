import pyautogui, keyboard, json, time, os, threading
from datetime import datetime

pyautogui.FAILSAFE = False
POSITIONS_FILE = "positions.json"

paused = False
should_exit = False
positions = {}
sent = 0
start_time = None
ascii_theme = "block"  # Change to "minimal" if you prefer

click_delay = 0.30     # Recommended delay between clicks
snap_delay = 0.30      # Recommended delay between full snap sequence

ascii_digits_block = {
    '0': [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    '1': ["  █  ", " ██  ", "  █  ", "  █  ", " ███ "],
    '2': [" ███ ", "    █", " ███ ", "█    ", "█████"],
    '3': ["████ ", "    █", " ███ ", "    █", "████ "],
    '4': ["█  █ ", "█  █ ", "█████", "   █ ", "   █ "],
    '5': ["█████", "█    ", "████ ", "    █", "████ "],
    '6': [" ███ ", "█    ", "████ ", "█   █", " ███ "],
    '7': ["█████", "    █", "   █ ", "  █  ", "  █  "],
    '8': [" ███ ", "█   █", " ███ ", "█   █", " ███ "],
    '9': [" ███ ", "█   █", " ████", "    █", " ███ "]
}

ascii_digits_minimal = {
    '0': [" __ ", "|  |", "|  |", "|__|"],
    '1': ["  | ", "  | ", "  | ", "  | "],
    '2': [" __ ", " __|", "|__ ", "    "],
    '3': [" __ ", " __|", " __|", "    "],
    '4': ["|__|", "   |", "   |", "    "],
    '5': ["|__ ", " __|", " __|", "    "],
    '6': [" __ ", "|__ ", "|__|", "    "],
    '7': ["___ ", "  / ", " /  ", "    "],
    '8': [" __ ", "|__|", "|__|", "    "],
    '9': [" __ ", "|__|", " __|", "    "]
}

def save_positions(pos_dict):
    with open(POSITIONS_FILE, "w") as f:
        json.dump(pos_dict, f)

def load_positions():
    if not os.path.exists(POSITIONS_FILE):
        return None
    with open(POSITIONS_FILE, "r") as f:
        return json.load(f)

def calibrate_positions():
    print("🔧 Calibrating positions:")
    positions = {}
    instructions = {
        "take_picture": "Hover mouse over 'Take Picture' button, then press F",
        "send_to": "Hover mouse over 'Send To', then press F",
        "shortcut": "Hover mouse over your shortcut, then press F",
        "select_all": "Hover mouse over 'Select All', then press F",
        "send": "Hover mouse over 'Send' button, then press F"
    }

    for key, prompt in instructions.items():
        print(prompt)
        while not keyboard.is_pressed("f"):
            if should_exit:
                exit()
            time.sleep(0.1)
        positions[key] = pyautogui.position()
        time.sleep(0.5)

    save_positions(positions)
    return positions

def send_snap(pos):
    pyautogui.click(pos["take_picture"])
    time.sleep(click_delay)
    pyautogui.click(pos["send_to"])
    time.sleep(click_delay)
    pyautogui.click(pos["shortcut"])
    time.sleep(click_delay)
    pyautogui.click(pos["select_all"])
    time.sleep(click_delay)
    pyautogui.click(pos["send"])

def draw_ascii_counter(number):
    os.system("cls" if os.name == "nt" else "clear")
    digits = ascii_digits_block if ascii_theme == "block" else ascii_digits_minimal
    lines = [""] * len(next(iter(digits.values())))
    for digit in str(number):
        for i in range(len(lines)):
            lines[i] += digits[digit][i] + "  "
    border = "╭" + "─" * 44 + "╮"
    print(border)
    print("│           📸  SNAPS SENT            │")
    print("╰" + "─" * 44 + "╯")
    for line in lines:
        print("     " + line)
    print("\n[CTRL+Q] Pause  |  [F] Resume  |  [R] Recalibrate  |  [ESC] Exit")

def show_stats():
    elapsed = (datetime.now() - start_time).total_seconds()
    minutes = elapsed / 60 if elapsed > 0 else 1
    spm = sent / minutes
    print("\n📊 Session Stats:")
    print(f"   Time Elapsed: {int(elapsed)} seconds")
    print(f"   Total Snaps Sent: {sent}")
    print(f"   Average Snaps/Minute: {spm:.2f}")

def listen_hotkeys():
    keyboard.add_hotkey('ctrl+q', pause)
    keyboard.add_hotkey('f', resume)
    keyboard.add_hotkey('r', recalibrate)
    keyboard.add_hotkey('esc', exit_script)

def pause():
    global paused
    paused = True
    print("\n⏸️  Script paused. Press F to resume, R to recalibrate, ESC to exit.")

def resume():
    global paused
    if paused:
        print("▶️  Resuming.")
        paused = False

def recalibrate():
    global paused, positions
    paused = True
    print("\n🔧 Recalibrating positions...")
    positions = calibrate_positions()
    print("✅ Positions recalibrated. Press F to resume.")

def exit_script():
    global should_exit
    print("\n❌ Exiting script.")
    should_exit = True

def wait_for_start():
    os.system("cls" if os.name == "nt" else "clear")
    border = "╭" + "─" * 44 + "╮"
    print(border)
    print("│        ⚡ ULTRA FAST SNAP SPAMMER        │")
    print("╰" + "─" * 44 + "╯")
    print("→ Use this script with Snapchat Web/App")
    print("→ Press [F] when everything is ready to spam")
    print("→ [CTRL+Q] Pause  |  [F] Resume  |  [R] Recalibrate  |  [ESC] Exit")
    print("\n🕓 Waiting for start signal... (press F to begin)")
    while not keyboard.is_pressed("f"):
        if should_exit:
            exit()
        time.sleep(0.1)
    print("▶️  Starting in 0.5s...")
    time.sleep(0.5)

def main():
    global paused, should_exit, positions, sent, start_time

    positions = load_positions()
    if not positions:
        positions = calibrate_positions()

    threading.Thread(target=listen_hotkeys, daemon=True).start()

    wait_for_start()
    start_time = datetime.now()

    try:
        while True:
            if should_exit:
                break
            if not paused:
                send_snap(positions)
                sent += 1
                draw_ascii_counter(sent)
                time.sleep(snap_delay)
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    show_stats()
    print(f"\n✅ Script ended. Total snaps sent: {sent}.")

if __name__ == "__main__":
    main()
