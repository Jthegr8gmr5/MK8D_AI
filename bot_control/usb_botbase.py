import usb.core

class USBBotbase:
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x057E)
        if self.dev is None:
            raise ValueError("Switch not detected on USB!")
        self.dev.set_configuration()

    def send_input(self, data: list):
        # Send controller input over USB
        self.dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, data)

    def get_screenshot(self):
        # Screenshot via USB
        return self.dev.ctrl_transfer(0xC0, 0x42, 0, 0, 400000)

    def read_memory(self, addr, size):
        # Read raw RAM
        return self.dev.ctrl_transfer(0xC0, 0x81, addr & 0xFFFF, addr >> 16, size)
