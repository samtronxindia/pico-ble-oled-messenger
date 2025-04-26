import time
from machine import Pin, SPI
import sh1106

class OLEDManager:
    def __init__(self, sck_pin, mosi_pin, dc_pin, rst_pin, cs_pin,
                 width=128, height=64, rotate=True,
                 max_chars_per_line=16, scroll_speed=0.03, align="left"):

        self.width = width
        self.height = height
        self.max_chars_per_line = max_chars_per_line
        self.scroll_speed = scroll_speed
        self.align = align.lower()  # "left" or "center"
        self.paused = False
        self.scroll_offset_y = 0
        self.lines = []

        self.spi = SPI(0, baudrate=1_000_000, polarity=0, phase=0,
                       sck=Pin(sck_pin), mosi=Pin(mosi_pin))
        self.dc = Pin(dc_pin)
        self.rst = Pin(rst_pin)
        self.cs = Pin(cs_pin)
        self.oled = sh1106.SH1106_SPI(width, height, self.spi, self.dc, self.rst, self.cs)

        if rotate:
            self.oled.rotate(True)

        self.add_line("OLED Ready")

    def add_line(self, text):
        chunks = [text[i:i+self.max_chars_per_line] for i in range(0, len(text), self.max_chars_per_line)]
        for chunk in chunks:
            self.lines.append(chunk)
        if len(self.lines) > 100:
            self.lines = self.lines[-100:]
        self.scroll_offset_y = 0

    def clear(self):
        self.lines = []
        self.oled.fill(0)
        self.oled.show()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def set_align(self, align_mode):
        self.align = align_mode.lower()

    def update(self):
        self.oled.fill(0)
        lines_on_screen = 5

        if len(self.lines) > lines_on_screen:
            start_line = self.scroll_offset_y // 8
            pixel_shift = self.scroll_offset_y % 8

            for i in range(lines_on_screen + 1):
                line_index = start_line + i
                if line_index < len(self.lines):
                    self._draw_text(self.lines[line_index], (i * 8) - pixel_shift)

            if not self.paused:
                self.scroll_offset_y += 1
                if self.scroll_offset_y >= (len(self.lines) * 8):
                    self.scroll_offset_y = 0
        else:
            for i, line in enumerate(self.lines):
                self._draw_text(line, i * 8)

        self.oled.show()

    def _draw_text(self, text, y):
        if self.align == "center":
            text_width = len(text) * 8  # 8 pixels per character
            x = max(0, (self.width - text_width) // 2)
        else:
            x = 0
        self.oled.text(text, x, y)

    def loop(self):
        while True:
            self.update()
            time.sleep(self.scroll_speed)
