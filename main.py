from Alpaca import Alpaca
import gc
import time

from Alpaca.SSD1351 import Display

gc.enable()
alpaca = Alpaca.Alpaca()
alpaca.display.init()

class Statusbar:
    def __init__(self, alpaca: Alpaca, x: int, y: int, x_0: int = 0, y_0: int = 0):
        self.alpaca = alpaca
        self.x_0 = x_0
        self.y_0 = y_0
        self.x = x
        self.y = y
        self.redraw_counter = 20
        self.update_counter = 200
        self.battery_level = int(alpaca.battery.get_percentage() * 100)
        self.show_nick = False
        self.switch_after = 20
        self.battery_color = 0x0f0
        self.nick_color = 0x00f
        self.banner_color = 0xfff
        if alpaca.display:
            # makes sure leftovers are blanked
            alpaca.display.fill_rect(self.x_0, self.y_0, x, y, 0x000)

    def render(self, display: Display):
        self.redraw_counter += 1
        if self.redraw_counter > self.switch_after:
            self.redraw_counter = 0
            self.show_nick = not self.show_nick
            display.fill_rect(self.x_0, self.y_0, self.x, self.y, 0x000)
            bar = f"@{self.alpaca.nick}" if self.show_nick else "Jugend hackt"
            color = self.nick_color if self.show_nick else self.banner_color
            display.text(bar, 0, 0, display.rgb_to_rgb565(
                color & 0xf00,
                color & 0x0f0,
                color & 0x00f
            ))
            indicator = f"{self.battery_level}%"
            display.text(indicator, 128 - len(indicator) * 8, 0, display.rgb_to_rgb565(
                self.battery_color & 0xf00,
                self.battery_color & 0x0f0,
                self.battery_color & 0x00f
            ))

    def tick(self, alpaca: Alpaca):
        self.update_counter += 1
        if self.update_counter > 200:
            self.battery_level = int(alpaca.battery.get_percentage() * 100)
            self.battery_color = 0x0f0
            if self.battery_level < 70:
                self.battery_color = 0x00f
            if self.battery_level < 30:
                self.battery_color = 0xff0
            if self.battery_level < 10:
                self.battery_color = 0xf00
            self.update_counter = 0

    def set_nick_color(self, color: int):
        self.nick_color = color

    def set_banner_color(self, color: int):
        self.banner_color = color

    def set_battery_color(self, color: int):
        self.battery_color = color


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

        alpaca.render_text("MAC Address", 10, 0xfff)
        alpaca.render_text(f"{alpaca.mac}", 11, 0xfff)

        alpaca.display.show()
        time.sleep(0.05)
