from bot_control.usb_botbase import USBBotbase
from bot_control.controller_inputs import INPUTS
import time

bot = USBBotbase()
print("Connected to Switch. Testing A button...")

try:
    while True:
        bot.send_input(INPUTS["A"])
        time.sleep(0.1)
        bot.send_input(INPUTS["RELEASE"])
        time.sleep(0.4)
except KeyboardInterrupt:
    bot.send_input(INPUTS["RELEASE"])
    print("\nTest stopped")
