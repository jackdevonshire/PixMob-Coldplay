import base64

class Color:
    def __init__(self, name):
        self.name = name
        self.codes = {}

    def add_code(self, fade, b64_code):
        b64_code = b64_code + '=' * (-len(b64_code) % 4)
        value = base64.b64decode(b64_code)
        self.codes[fade] = value

    def get_ir_signal(self, fade=None):
        if not fade or fade < 0 or fade > 6:
            return self.codes[0]
        
        return self.codes.get(fade, self.codes[0])

red = Color("RED")
red.add_code(0, "JgAYAC4uFxcXLhdcF0UuFxcXFy4uXC5cFwANBQ==")
red.add_code(1, "JgAkAC4uFxcXLhdcF0UuFxcXFy4uXC5cF0UXFy4XF0UXXC5cFwANBQAAAAA=")
red.add_code(2, "JgAmAC4uFxcXLhdcF0UuFxcXFy4uXC5cFy4XLi4XFxcXFxdcLlwXAA0FAAA=")
red.add_code(3, "JgAmAC4uFxcXLhdcF0UuFxcXFy4uXC5cF0UXFy4XFxcXFxdcLlwXAA0FAAA=")
red.add_code(4, "JgAkAC4uFxcXLhdcF0UuFxcXFy4uXC5cF1wuLhdFFxcXLi5cFwANBQAAAAA=")
red.add_code(5, "JgAkAC4uFxcXLhdcF0UuFxcXFy4uXC5cF0UXFy4XFy4uXC5cFwANBQAAAAA=")
red.add_code(6, "JgAkAC4uFxcXLhdcF0UuFxcXFy4uXC5cFy4XLi4XFy4uXC5cFwANBQAAAAA=")
green = Color("GREEN")
green.add_code(0, "JgAYAC4uFxcXFy5cFy4XLhcuFy4uXC5cFwANBQ==")
green.add_code(1, "JgAkAC4uFxcXFy5cFy4XLhcuFy4uXC5cF0UXFy4XF0UXXC5cFwANBQAAAAA=")
green.add_code(2, "JgAmAC4uFxcXFy5cFy4XLhcuFy4uXC5cFy4XLi4XFxcXFxdcLlwXAA0FAAA=")
green.add_code(3, "JgAmAC4uFxcXFy5cFy4XLhcuFy4uXC5cF0UXFy4XFxcXFxdcLlwXAA0FAAA=")
green.add_code(4, "JgAkAC4uFxcXFy5cFy4XLhcuFy4uXC5cF1wuLhdFFxcXLi5cFwANBQAAAAA=")
green.add_code(5, "JgAkAC4uFxcXFy5cFy4XLhcuFy4uXC5cF0UXFy4XFy4uXC5cFwANBQAAAAA=")
green.add_code(6, "JgAkAC4uFxcXFy5cFy4XLhcuFy4uXC5cFy4XLi4XFy4uXC5cFwANBQAAAAA=")
light_green = Color("LLIGHT_GREEN")
light_green.add_code(0, "JgAcABcXFxcuLi5cFy4XLhcuFxcXLhdFFy4XLhcADQUAAAAAAAAAAAAAAAA=")
light_green.add_code(1, "JgAoABcXFxcuLi5cFy4XLhcuFxcXLhdFFxcuFxdFF1wuXBcADQU=")
light_green.add_code(2, "JgAqABcXFxcuLi5cFy4XLhcuFxcXLhdFFy4XLhcuFy4uFxcXFxcXXC5cFwANBQAAAAAAAAAAAAAAAAAA")
light_green.add_code(3, "JgAqABcXFxcuLi5cFy4XLhcuFxcXLhdFFy4XLhdFFxcuFxcXFxcXXC5cFwANBQAAAAAAAAAAAAAAAAAA")
light_green.add_code(4, "JgAoABcXFxcuLi5cFy4XLhcuFxcXLhdFF4XLhdcLi4XRRcXFy4uXBcADQU=")
light_green.add_code(5, "JgAoABcXFxcuLi5cFy4XLhcuFxcXLhdFFy4XLhdFFxcuFxcuLlwuXBcADQU=")
light_green.add_code(6, "JgAoABcXFxcuLi5cFy4XLhcuFxcXLhdFFy4XLhcuFy4uFxcuLlwuXBcADQU=")
yellow_green = Color("YELLOW_GREEN")
yellow_green.add_code(0, "JgAaABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXAA0FAAAAAAAAAAAAAAAAAAA=")
yellow_green.add_code(1, "JgAmABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXRRcXLhcXRRdcLlwXAA0FAAA=")
yellow_green.add_code(2, "JgAoABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXLhcuLhcXFxcXF1wuXBcADQU=")
yellow_green.add_code(3, "JgAoABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXRRcXLhcXFxcXF1wuXBcADQU=")
yellow_green.add_code(4, "JgAmABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXXC4uF0UXFxcuLlwXAA0FAAA=")
yellow_green.add_code(5, "JgAmABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXRRcXLhcXLi5cLlwXAA0FAAA=")
yellow_green.add_code(6, "JgAmABcXFxcuLi5cF0UXFxcuFy4XFxdFLlwXLhcuLhcXLi5cLlwXAA0FAAA=")
blue = Color("BLUE")
blue.add_code(0, "JgAeABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFFwANBQAAAAAAAAAAAAA=")
blue.add_code(1, "JgAqABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFF0UXFy4XF0UXXC5cFwANBQAAAAAAAAAAAAAAAAAA")
blue.add_code(2, "JgAsABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFFy4XLi4XFxcXFxdcLlwXAA0FAAAAAAAAAAAAAAAA")
blue.add_code(3, "JgAsABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFF0UXFy4XFxcXFxdcLlwXAA0FAAAAAAAAAAAAAAAA")
blue.add_code(4, "JgAqABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFF1wuLhdFFxcXLi5cFwANBQAAAAAAAAAAAAAAAAAA")
blue.add_code(5, "JgAqABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFF0UXFy4XFy4uXC5cFwANBQAAAAAAAAAAAAAAAAAA")
blue.add_code(6, "JgAqABcXF0UuFxdcFy4XFxcuLhcXLhcXFxcXFxdFFy4XLi4XFy4uXC5cFwANBQAAAAAAAAAAAAAAAAAA")
light_blue = Color("LIGHT_BLUE")
light_blue.add_code(0, "JgAeABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFFwANBQAAAAAAAAAAAAA=")
light_blue.add_code(1, "JgAqABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFF0UXFy4XF0UXXC5cFwANBQAAAAAAAAAAAAAAAAAA")
light_blue.add_code(2, "JgAsABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFFy4XLi4XFxcXFxdcLlwXAA0FAAAAAAAAAAAAAAAA")
light_blue.add_code(3, "JgAsABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFF0UXFy4XFxcXFxdcLlwXAA0FAAAAAAAAAAAAAAAA")
light_blue.add_code(4, "JgAqABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFF1wuLhdFFxcXLi5cFwANBQAAAAAAAAAAAAAAAAAA")
light_blue.add_code(5, "JgAqABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFF0UXFy4XFy4uXC5cFwANBQAAAAAAAAAAAAAAAAAA")
light_blue.add_code(6, "JgAqABcXF0UuFxdcFy4XFxcuFxcXFxcXFxcuLhdFFy4XLi4XFy4uXC5cFwANBQAAAAAAAAAAAAAAAAAA")
magenta = Color("MAGENTA")
magenta.add_code(0, "JgAaABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXAA0FAAAAAAAAAAAAAAAAAAA=")
magenta.add_code(1, "JgAmABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXRRcXLhcXRRdcLlwXAA0FAAA=")
magenta.add_code(2, "JgAoABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXLhcuLhcXFxcXF1wuXBcADQU=")
magenta.add_code(3, "JgAoABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXRRcXLhcXFxcXF1wuXBcADQU=")
magenta.add_code(4, "JgAmABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXXC4uF0UXFxcuLlwXAA0FAAA=")
magenta.add_code(5, "JgAmABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXRRcXLhcXLi5cLlwXAA0FAAA=")
magenta.add_code(6, "JgAmABcXFxcuLi5cF0UuRRcXFxcuRRcXF0UXLhcuLhcXLi5cLlwXAA0FAAA=")
yellow = Color("YELLOW")
yellow.add_code(0, "JgAaABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXAA0FAAAAAAAAAAAAAAAAAAA=")
yellow.add_code(1, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXRRdcLlwXAA0FAAA=")
yellow.add_code(2, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXLhcuLhcXFxcXF1wuXBcADQU=")
yellow.add_code(3, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXFxcXF1wuXBcADQU=")
yellow.add_code(4, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXXC4uF0UXFxcuLlwXAA0FAAA=")
yellow.add_code(5, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXLi5cLlwXAA0FAAA=")
yellow.add_code(6, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXLhcuLhcXLi5cLlwXAA0FAAA=")
pink = Color("PINK")
pink.add_code(0, "JgAaABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXAA0FAAAAAAAAAAAAAAAAAAA=")
pink.add_code(1, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXRRdcLlwXAA0FAAA=")
pink.add_code(2, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXLhcuLhcXFxcXF1wuXBcADQU=")
pink.add_code(3, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXFxcXF1wuXBcADQU=")
pink.add_code(4, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXXC4uF0UXFxcuLlwXAA0FAAA=")
pink.add_code(5, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXRRcXLhcXLi5cLlwXAA0FAAA=")
pink.add_code(6, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcXF0UXLhcuLhcXLi5cLlwXAA0FAAA=")
orange = Color("ORANGE")
orange.add_code(0, "JgAaABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXAA0FAAAAAAAAAAAAAAAAAAA=")
orange.add_code(1, "JgAmABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXRRcXLhcXRRdcLlwXAA0FAAA=")
orange.add_code(2, "JgAoABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXLhcuLhcXFxcXF1wuXBcADQU=")
orange.add_code(3, "JgAoABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXRRcXLhcXFxcXF1wuXBcADQU=")
orange.add_code(4, "JgAmABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXXC4uF0UXFxcuLlwXAA0FAAA=")
orange.add_code(5, "JgAmABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXRRcXLhcXLi5cLlwXAA0FAAA=")
orange.add_code(6, "JgAmABcXFxcuLi5cF0UXFxcuFxcXLhdFLlwXLhcuLhcXLi5cLlwXAA0FAAA=")
white = Color("WHITE")
white.add_code(0, "JgAaABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XAA0FAAAAAAAAAAAAAAAAAAA=")
white.add_code(1, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XRRcXLhcXRRdcLlwXAA0FAAA=")
white.add_code(2, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XLhcuLhcXFxcXF1wuXBcADQU=")
white.add_code(3, "JgAoABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XRRcXLhcXFxcXF1wuXBcADQU=")
white.add_code(4, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XXC4uF0UXFxcuLlwXAA0FAAA=")
white.add_code(5, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XRRcXLhcXLi5cLlwXAA0FAAA=")
white.add_code(6, "JgAmABcXF0UuFxdcFy4XFxdcLi4XRRcuFy4XLhcuLhcXLi5cLlwXAA0FAAA=")
turquoise = Color("TURQ")
turquoise.add_code(0, "JgAaABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXAA0FAAAAAAAAAAAAAAAAAAA=")
turquoise.add_code(1, "JgAmABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXRRcXLhcXRRdcLlwXAA0FAAA=")
turquoise.add_code(2, "JgAoABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXLhcuLhcXFxcXF1wuXBcADQU=")
turquoise.add_code(3, "JgAoABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXRRcXLhcXFxcXF1wuXBcADQU=")
turquoise.add_code(4, "JgAmABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXXC4uF0UXFxcuLlwXAA0FAAA=")
turquoise.add_code(5, "JgAmABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXRRcXLhcXLi5cLlwXAA0FAAA=")
turquoise.add_code(6, "JgAmABcXFxcuLi5cFy4XFy4uFy4uXBcXF0UXLhcuLhcXLi5cLlwXAA0FAAA=")

ALL_AVAILABLE_COLOURS = {
    'RED': red,
    'GRN': green,
    'LLIGHT_GREEN': light_green,
    'YELLOW_GREEN': yellow_green,
    'BLUE': blue,
    'LIGHT_BLUE': light_blue,
    'MAG': magenta,
    'YEL': yellow,
    'PINK': pink,
    'ORANGE': orange,
    'WHITE': white,
    'TURQ': turquoise,
}


class IRCodes:

    def __init__(self):
        self.b64_codes = {}
        b64_codes = {k: v for k, v in self.__class__.__dict__.items() if isinstance(v, str) and len(v) > 10}
        for key, value in b64_codes.items():
            value = value + '=' * (-len(value) % 4)
            self.b64_codes[key] = base64.b64decode(value)

    def all_available_codes(self):

        return self.b64_codes
    
    def main_colors(self):
        main_colors = {
            'RED': self.RED,
            'GRN': self.GRN,
            'BLUE': self.BLUE,
            'YEL': self.YEL,
            'MAG': self.MAG,
        }
        return main_colors