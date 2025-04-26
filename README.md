# Pico BLE OLED Messenger

![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Pico%20W-blue)
![Language](https://img.shields.io/badge/language-MicroPython-orange)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

A Bluetooth Low Energy (BLE) text receiver and OLED message scroller for Raspberry Pi Pico W, written in MicroPython.

This project cleanly separates BLE communication and OLED control into modular libraries for easy reuse and extension.

## Features

- Receive text over BLE from any BLE app (e.g., nRF Connect, LightBlue)
- Display received messages scrolling vertically on SH1106 OLED screen
- Recognizes simple BLE text commands:
  - `CLEAR` — Clears the screen
  - `PAUSE` — Pauses scrolling
  - `RESUME` — Resumes scrolling
  - `CENTER` — Centers text horizontally
- Modular architecture:
  - `oled_manager.py`: OLED screen control
  - `ble_manager.py`: BLE communication handling
- Configurable settings:
  - Pin mappings (SPI OLED connections)
  - BLE device name
  - Scroll speed
  - Text alignment (left or center)

## Hardware Required

- Raspberry Pi Pico W
- SH1106 128x64 OLED display (SPI)
- Battery pack or USB power

## Software Required

- [MicroPython firmware](https://micropython.org/download/rp2-pico-w/)
- Thonny IDE or any MicroPython-compatible uploader
- BLE app on phone (e.g., [nRF Connect](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp) or [LightBlue](https://apps.apple.com/us/app/lightblue/id557428110))

## Installation

1. Flash your Pico W with MicroPython firmware.
2. Upload the following files to your Pico W:
    - `oled_manager.py`
    - `ble_manager.py`
    - `ble_msg.py`
3. (Optional) Rename `ble_msg.py` to `main.py` if you want the program to auto-start on boot.
4. Power the Pico W.

## Usage

1. Open a BLE app on your smartphone.
2. Connect to the advertised BLE device (default name: `PicoW-BLE-OLED`).
3. Send text messages.
4. Special commands you can send:
    - `CLEAR`
    - `PAUSE`
    - `RESUME`
    - `CENTER`
5. Watch your text scroll smoothly on the OLED!

## Folder Structure

