import machine
import os

from neopixel import NeoPixel

from Teebeutel import Device
from Teebeutel.SSD1351 import Display
from Teebeutel.PPSI262 import PPSI262


class DPad:
    def __init__(self, up: int, down: int, left: int, right: int, push: int):
        Pin = machine.Pin
        Signal = machine.Signal
        self.up_signal = Signal(Pin(up, Pin.IN), invert=True)
        self.down_signal = Signal(Pin(down, Pin.IN), invert=True)
        self.left_signal = Signal(Pin(left, Pin.IN), invert=True)
        self.right_signal = Signal(Pin(right, Pin.IN), invert=True)
        self.push_signal = Signal(Pin(push, Pin.IN), invert=True)

    @property
    def up(self) -> bool:
        return self.up_signal.value() == 1

    @property
    def down(self) -> bool:
        return self.down_signal.value() == 1

    @property
    def left(self) -> bool:
        return self.left_signal.value() == 1

    @property
    def right(self) -> bool:
        return self.right_signal.value() == 1

    @property
    def push(self) -> bool:
        return self.push_signal.value() == 1


class Teebeutel:
    def __init__(self):
        self.i2c = machine.I2C(Device.I2C_ID)
        self.sd_card = None
        self.display = Display(Device.OLED_SPI_ID, Device.OLED_CS, Device.OLED_DC, Device.OLED_RES)
        self.dpad = DPad(Device.BTN_UP, Device.BTN_DOWN, Device.BTN_LEFT, Device.BTN_RIGHT, Device.BTN_PUSH)
        self.neopixel = NeoPixel(machine.Pin(Device.WS2812_PIN, machine.Pin.OUT), Device.WS2812_NUM)
        self.heartrate = PPSI262(self.i2c)

    def mount_SD(self) -> bool:
        try:
            self.sd_card = machine.SDCard(slot=Device.SD_SPI_ID)
            os.mount(self.sd_card, Device.SD_PATH)
            return True
        except OSError:
            return False

    def umount_SD(self) -> bool:
        try:
            os.umount(Device.SD_PATH)
            self.sd_card.deinit()
            self.sd_card = None
            return True
        except OSError:
            return False

    def hard_reset(self):
        machine.reset()

    def soft_reset(self):
        self.__del__()
        machine.soft_reset()

    def __del__(self):
        self.umount_SD()
