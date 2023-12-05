import time
import machine, neopixel
from Color import Color, Colors

import math

def rgb_to_hsv(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = high, high, high

    d = high - low
    s = 0 if high == 0 else d/high

    if high == low:
        h = 0.0
    else:
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return h, s, v

def hsv_to_rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 42.666667 # Note: this was 60.0 before
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

class Controller:
    def __init__(self, pin, pixels):
        self.pin = pin
        self.pixels = pixels
        
        # Create neo pixel array
        self.np = neopixel.NeoPixel(machine.Pin(self.pin), pixels)

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
                self.np[__] = Colors.BLACK.toRGB()
            self.np[_ % n] = color
            self.show()
            time.sleep_ms(80)

    # DOES update the pixels
    def bounce(self, color: Color):
        color = color.toRGB()
        n = self.np.n
        
        for _ in range(4 * n):
            for __ in range(n):
                self.np[__] = color
            if (_ // n) % 2 == 0:
                self.np[_ % n] = Colors.BLACK.toRGB()
            else:
                self.np[n - 1 - (_ % n)] = Colors.BLACK.toRGB()
            self.show()
            time.sleep_ms(80)

    # DOES update the pixels
    def rainbow_cycle(self, wait, brightness=1.0):
        n = self.np.n
        for j in range(256):  # one cycle of all 256 colors in the wheel
            for i in range(n):
                rc_index = (i * 256 // n) + j  # color based on a gradient on the wheel
                hsv_color = rc_index % 256, 1, 1  # HSV is easier for generating rainbows
                rgb_color = hsv_to_rgb(*hsv_color)
                dimmed_rgb = tuple(int(c * brightness) for c in rgb_color)  # apply brightness
                self.np[i] = dimmed_rgb
            self.show()
            time.sleep_ms(wait)

    # DOES update the pixels
    def clear(self):
        n = self.np.n
        
        for _ in range(n):
            self.np[_] = Colors.BLACK.toRGB()
        self.show()

