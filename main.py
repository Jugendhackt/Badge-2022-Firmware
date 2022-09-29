from Alpaca import Alpaca
import gc
import time

gc.enable()
alpaca = Alpaca.Alpaca()
alpaca.display.init()


colors = [[0, 255, 0], [0, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 255], [255, 0, 255], [255, 255, 255]]
c = 0

while True:
    for i in range(len(colors)):
        alpaca.display.fill(alpaca.display.rgb_to_rgb565(0, 0, 0))
        #alpaca.display.fill(alpaca.display.rgb_to_rgb565(colors[i][0], colors[i][1], colors[i][2]))
        #alpaca.display.text("JugendHackt", 64 - 8 * int(len("JugendHackt")/2), 64 - 4 - 10, 0xfff)
        #alpaca.display.text("Berlin 2022", 64 - 8 * int(len("Berlin 2022")/2), 64 - 4, 0xfff)
        charge_stat = alpaca.battery.get_percentage()
        alpaca.render_text(f"JugendHackt {charge_stat}%", 0, 0xfff)
        alpaca.render_text("Berlin 2022", 1, 0x000)
        alpaca.render_text(f"UP: {('YES' if alpaca.dpad.up else 'NO')}", 3, 0xfff)
        alpaca.render_text(f"DOWN: {('YES' if alpaca.dpad.down else 'NO')}", 4, 0xfff)
        alpaca.render_text(f"LEFT: {('YES' if alpaca.dpad.left else 'NO')}", 5, 0xfff)
        alpaca.render_text(f"RIGHT: {('YES' if alpaca.dpad.right else 'NO')}", 6, 0xfff)
        alpaca.render_text(f"SELECT: {('YES' if alpaca.dpad.push else 'NO')}", 7, 0xfff)
        alpaca.render_text(f"A: {('YES' if alpaca.a.pressed else 'NO')}", 8, 0xfff)
        alpaca.render_text(f"B: {('YES' if alpaca.b.pressed else 'NO')}", 9, 0xfff)

        alpaca.display.show()
        time.sleep(0.05)
