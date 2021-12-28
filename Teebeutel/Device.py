from micropython import const

# Pin definitions)
UART_TxD = const(1)
UART_RxD = const(3)

I2C_ID = const(1)
I2C_SCL = const(25)
I2C_SDA = const(26)

SD_SPI_ID = const(2)
SD_SCK = const(18)
SD_CS = const(5)
SD_MISO = const(19)
SD_MOSI = const(23)
SD_PATH = const('/sd')

OLED_SPI_ID = const(1)
OLED_CS = const(17)
OLED_SCK = const(14)
OLED_MOSI = const(13)
# OLED_MISO = const(12)
OLED_DC = const(21)
OLED_RES = const(16)

TOUCH_A = const(None)
TOUCH_B = const(None)

ADC_BAT = const(4)

IR_Rx = const(5)
IR_Tx = const(27)

WS2812_PIN = const(32)
WS2812_NUM = const(12)

BTN_UP = const(34)
BTN_DOWN = const(35)
BTN_LEFT = const(15)
BTN_RIGHT = const(22)
BTN_PUSH = const(33)
