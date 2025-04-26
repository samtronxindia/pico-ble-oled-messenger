USAGE GUIDE

This project is split into:

1. oled_manager.py — controls only the OLED screen
2. ble_manager.py — handles BLE communication
3. ble_msg.py — main file combining both modules

How it works:

- BLEManager receives text messages from Bluetooth.
- If the message is "CLEAR", "PAUSE", "RESUME", or "CENTER", it triggers actions.
- Otherwise, it adds the text to OLEDManager for scrolling display.

Steps:

1. Upload all three files to your Pico W.
2. Save ble_msg.py as main.py if needed.
3. Connect using BLE app like nRF Connect or LightBlue.
4. Send messages!

Supported Commands:

- CLEAR  — clears screen
- PAUSE  — stops scrolling
- RESUME — resumes scrolling
- CENTER — center-aligns future text
- any other text — displays as scrolling text
