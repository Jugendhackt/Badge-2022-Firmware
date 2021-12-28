from Teebeutel import Teebeutel
import gc

gc.enable()
teebeutel = Teebeutel.Teebeutel()
teebeutel.display.init()

direction = True
x = 30
y = 66
colors = [[0, 255, 0], [0, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 255], [255, 0, 255], [255, 255, 255]]
c = 0

while True:
    teebeutel.neopixel.fill(colors[c])
    teebeutel.neopixel.write()
    teebeutel.display.fill(0)
    teebeutel.display.text('MicroPython!', x, y, teebeutel.display.rgb_to_rgb565(*colors[c]))
    teebeutel.display.hline(x, y+9, 96, teebeutel.display.rgb_to_rgb565(*colors[c]))
    teebeutel.display.show()

    if teebeutel.dpad.up:
        y = y - 1
    if teebeutel.dpad.down:
        y = y + 1
    if teebeutel.dpad.right:
        x = x - 1
    if teebeutel.dpad.left:
        x = x + 1
    if teebeutel.dpad.push:
        c = c + 1
        if c == len(colors):
            c = 0
        while teebeutel.dpad.push:
            None
