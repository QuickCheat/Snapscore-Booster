# 📸 snapboost V1

`snapboost V1` is an ultra-fast automated snap sender for Snapchat Web, created for educational and experimental purposes only.

## 🚀 Features

- Auto-calibration of screen positions
- Simple hotkey controls (pause, resume, recalibrate, exit)
- Visual ASCII counter to track sent snaps
- Ultra-fast execution loop

## ⚙️ Installation

1. Clone the repository or download the ZIP.
2. Run `install_requirements.bat` to install dependencies.
3. Launch the script using `launch.bat`.

> ✅ **Python 3 must be installed and available in your PATH.**

## 📱 Snapchat Setup (VERY IMPORTANT)

Before using the script, **you must create a shortcut in Snapchat (on your phone)**:

1. Open Snapchat on your **mobile device**.
2. Create a new **shortcut** (via the "Send to..." screen).
3. Add all the people you want to auto-send snaps to.
4. This shortcut will appear on Snapchat Web as a selectable group.

> 🟡 The script will automatically click on that shortcut and send a snap to **everyone in it**, in a loop.

## 🎮 Usage

1. Open Snapchat Web and prepare to take a snap.
2. Run `launch.bat`.
3. Calibrate the positions by hovering over the requested UI elements and pressing `F`.
4. Once calibration is done, press `F` to start.
5. Hotkeys available:
   - `CTRL + Q` → Pause
   - `F` → Resume
   - `R` → Recalibrate
   - `ESC` → Exit

## 🎨 ASCII Theme

Choose the visual style of the snap counter display.

In the script, modify this line:
```python
ascii_theme = "block"  # or "minimal"

## ⚠️ Disclaimer

This script is intended **for educational purposes only**.  
I am **not responsible** for any bans, penalties, or consequences resulting from its use.  
Use it **at your own risk**.

## 🙏 Credit

If you find this useful, a little credit would be super cool! ❤️  
Feel free to fork, modify, and improve the script.
