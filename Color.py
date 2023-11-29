class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    # converts to hex
    def __str__(self):
        # return the string repr
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"

    def __getitem__(self, item):
        # allow `color[0],color[1],color[2]` access
        return [self.r, self.g, self.b][item]

    def __iter__(self):
        # cast to list
        return iter([self.r, self.g, self.b])

    def toRGB(self):
        # cast to tuple
        return (self.r, self.g, self.b)

class Colors:
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
