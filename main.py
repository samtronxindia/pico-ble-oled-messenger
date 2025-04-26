from oled_manager import OLEDManager
from ble_manager import BLEManager
import time

# Define your pins
SCK_PIN = 18
MOSI_PIN = 19
DC_PIN = 20
RST_PIN = 16
CS_PIN = 17

# Create managers
oled = OLEDManager(
    sck_pin=SCK_PIN,
    mosi_pin=MOSI_PIN,
    dc_pin=DC_PIN,
    rst_pin=RST_PIN,
    cs_pin=CS_PIN,
    rotate=True,
    scroll_speed=0.03,
    align="left"
)

def handle_ble_message(text):
    command = text.upper()
    if command == "CLEAR":
        oled.clear()
        oled.add_line("Screen Cleared")
    elif command == "PAUSE":
        oled.pause()
        oled.add_line("Scrolling Paused")
    elif command == "RESUME":
        oled.resume()
        oled.add_line("Scrolling Resumed")
    elif command == "CENTER":
        oled.set_align("center")
        oled.add_line("Centering Text")
    else:
        oled.add_line(text)

# Setup BLE with callback
ble = BLEManager(callback=handle_ble_message)

# Main loop
while True:
    oled.update()
    time.sleep(0.03)
