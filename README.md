# 🖥️ Keep Awake – Mouse & Keyboard Activity Simulator

A **lightweight Python script** that prevents your computer from going to sleep, locking, or entering idle mode by simulating natural human-like activity:

- Small random mouse movements  
- Occasional harmless key presses (Shift)  
- Rare random scrolling  

Perfect for long downloads, video renders, remote desktop sessions, online meetings (when AFK), or any situation where you need the system to stay awake without changing power settings.

![Demo GIF or screenshot](https://via.placeholder.com/800x400.png?text=Keep+Awake+in+Action)  
*(replace with real recording — highly recommended)*

## ✨ Features

- **Random small mouse movements** every ~30 seconds (configurable)  
- **Harmless Shift key press** every ~2 minutes (configurable)  
- **Occasional random scrolling** (~10% chance per cycle)  
- **Configurable total runtime** (default: 8–9 hours)  
- **Very low CPU & resource usage**  
- **Console feedback** — see every action in real time  
- No tray icon, no background service — just run and forget  

## 📦 Ideal Repository Name

`keep-awake-python`

## 📝 Short Description (for GitHub / PyPI)

Prevent system sleep / screen lock by simulating random mouse movements, occasional scrolling, and harmless key presses.

## 🚀 Quick Start

```bash
# 1. Install dependencies (only two small libraries)
pip install pyautogui keyboard