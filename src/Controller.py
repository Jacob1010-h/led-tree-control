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
    h/=360.0
    if s == 0.0:
        return int(v*255), int(v*255), int(v*255)
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i %= 6
    if i == 0:
        return int(v*255), int(t*255), int(p*255)
    if i == 1:
        return int(q*255), int(v*255), int(p*255)
    if i == 2:
        return int(p*255), int(v*255), int(t*255)
    if i == 3:
        return int(p*255), int(q*255), int(v*255)
    if i == 4:
        return int(t*255), int(p*255), int(v*255)
    if i == 5:
        return int(v*255), int(p*255), int(q*255)
    # Cannot get here

class Controller:
    def __init__(self, pin, pixels):
        self.pin = pin
        self.pixels = pixels
        
        # Create neo pixel array
        self.np = neopixel.NeoPixel(machine.Pin(self.pin), pixels)

    def onRange(self, start, end, color: Color):
        for i in range(start, end):
            self.np[i] = (color.r, color.g, color.b)

    def offRange(self, start, end):
        for i in range(start, end):
            self.np[i] = Colors.BLACK.toRGB()
        

    def setBrightness(self, brightness):
        brightness = min(1.0, max(0.07, brightness))
        for i in range(self.np.n):
            self.np[i] = tuple(int(c * brightness) for c in self.np[i])
        

    # DOES update the pixels
    def apply(self):
        self.np.write()

    # DOES update the pixels
    def cycle(self, color: Color):
        color = color.toRGB()
        n = self.np.n
        
        for _ in range(4 * n):
            for __ in range(n):
                self.np[__] = Colors.BLACK.toRGB()
            self.np[_ % n] = color
            self.apply()
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
            self.apply()
            time.sleep_ms(80)

    # DOES update the pixels
    def rainbow_cycle(self, wait, brightness=0.4):
        n = self.np.n
        for j in range(256):  # one cycle of all 256 colors in the wheel
            for i in range(n):
                rc_index = (i * 256 // n) + j  # color based on a gradient on the wheel
                hsv_color = rc_index % 256, 1, 1  # HSV is easier for generating rainbows
                rgb_color = hsv_to_rgb(*hsv_color)
                dimmed_rgb = tuple(int(c * brightness) for c in rgb_color)  # apply brightness
                self.np[i] = dimmed_rgb
            self.apply()
            time.sleep_ms(wait)

    def rainbow_pulse(self, start, end, wait=35, brightness=0.4, loops=1):
        for hue in range(360*loops+196):
            rgb_color = hsv_to_rgb(hue%360, 1, brightness)
            self.onRange(start, end, Color(rgb_color[0], rgb_color[1], rgb_color[2]))
            self.apply()
            time.sleep_ms(wait)

    # DOES update the pixels
    def clear(self):
        n = self.np.n
        for _ in range(n):
            self.np[_] = Colors.BLACK.toRGB()
            self.apply()
            time.sleep_ms(10)

