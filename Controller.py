import time
import machine, neopixel
from Color import Color, Colors

class Controller:
    def __init__(self, pin, pixels):
        self.pin = pin
        self.pixels = pixels
        
        # Create neo pixel array
        self.np = neopixel.NeoPixel(machine.Pin(self.pin), pixels)

    # DOES NOT update the pixels
    def on(self, index, color: Color):
        self.np[index] = (color.r, color.g, color.b)

    # DOES NOT update the pixels
    def off(self, index):
        self.np[index] = Colors.BLACK

    # DOES NOT update the pixels
    def onRange(self, start, end, color: Color):
        for i in range(start, end):
            self.np[i] = (color.r, color.g, color.b)

    # DOES NOT update the pixels
    def offRange(self, start, end):
        for i in range(start, end):
            self.np[i] = Colors.BLACK.toRGB()

    # DOES update the pixels
    def show(self):
        self.np.write()

    # DOES update the pixels
    def cycle(self, color: Color):
        color = color.toRGB()
        n = self.np.n
        
        for _ in range(4 * n):
            for __ in range(n):
                self.np[__] = Color.BLACK.toRGB()
            self.np[_ % n] = color
            self.show()
            time.sleep_ms(25)

    # DOES update the pixels
    def bounce(self, color: Color):
        color = color.toRGB()
        n = self.np.n
        
        for _ in range(4 * n):
            for __ in range(n):
                self.np[__] = color
            if (_ // n) % 2 == 0:
                self.np[_ % n] = Color.BLACK.toRGB()
            else:
                self.np[n - 1 - (_ % n)] = Color.BLACK.toRGB()
            self.show()
            time.sleep_ms(60)

    # DOES update the pixels
    def fade(self, color: Color):
        color = color.toRGB()
        n = self.np.n

        for _ in range(0, 4 * 256, 8):
            for __ in range(n):
                val = _ & 0xff if (__ // 256) % 2 == 0 else 255 - (_ & 0xff)
                self.np[__] = (val, 0, 0)
            self.show()

    # DOES update the pixels
    def clear(self):
        n = self.np.n
        
        for _ in range(n):
            self.np[_] = Color.BLACK.toRGB()
        self.show()

