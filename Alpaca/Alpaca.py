import machine
import os

from neopixel import NeoPixel

from Alpaca import Device
from Alpaca.SSD1351 import Display


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


class Button:
    def __init__(self, pin: int):
        self.button = machine.Signal(machine.Pin(pin, machine.Pin.IN), invert=True)

    @property
    def pressed(self) -> bool:
        return self.button.value() == 1


class Battery:
    def __init__(self, adc: int):
        self.battery = machine.ADC(machine.Pin(adc))
        self.voltage_empty = 3.6
        self.voltage_full = 4.0

    def get_percentage(self) -> int:
        # returns between 0 and 65535
        voltage = self.get_voltage() - self.voltage_empty
        return int((voltage / (self.voltage_full - self.voltage_empty)) * 100)

    def get_voltage(self) -> float:
        # returns between 0 and 1024, 1024 is one volt
        raw = self.battery.read_u16()
        return (raw / 65535) * 4


class Alpaca:
    def __init__(self):
        self.i2c = machine.I2C(Device.I2C_ID, freq=Device.I2C_FREQ)
        self.sd_card = None
        self.battery = Battery(Device.ADC_BAT)
        self.display = Display(Device.OLED_SPI_ID, Device.OLED_CS, Device.OLED_DC, Device.OLED_RES)
        self.dpad = DPad(Device.BTN_UP, Device.BTN_DOWN, Device.BTN_LEFT, Device.BTN_RIGHT, Device.BTN_PUSH)
        self.a = Button(Device.BTN_A)
        self.b = Button(Device.BTN_B)
        self.neopixel = NeoPixel(machine.Pin(Device.WS2812_PIN, machine.Pin.OUT), Device.WS2812_NUM)

    def hard_reset(self):
        machine.reset()

    def soft_reset(self):
        self.__del__()
        machine.soft_reset()

    def __del__(self):
        if Device.SD_PATH:
            self.umount_SD()
