#
# RGBとHEXの相互変換を行うクラス
#
class HexRGBConverter:
    def __init__(self):
        pass

    #
    # RGBをHEXに変換する関数
    #
    def rgb_to_hex(self, r, g, b):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be in the range 0-255.")
        return "#{:02X}{:02X}{:02X}".format(r, g, b)

    #
    # HEXをRGBに変換する関数
    #
    def hex_to_rgb(self, hex_color):
        if not hex_color.startswith("#") or (
            len(hex_color) != 4 and len(hex_color) != 7
        ):
            raise ValueError("HEX color must be in the format #RRGGBB.")
        if len(hex_color) == 4:
            hex_color = "#" + "".join([c * 2 for c in hex_color[1:]])
        return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))

    #
    # RGBAをHEXに変換する関数
    #
    def rgba_to_hex(self, r, g, b, a):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and 0 <= a <= 255):
            raise ValueError("RGBA values must be in the range 0-255.")
        return "#{:02X}{:02X}{:02X}{:02X}".format(r, g, b, a)

    #
    # HEXをRGBに変換する関数
    #
    def hex_to_rgba(self, hex_color):
        if not hex_color.startswith("#") or (
            len(hex_color) != 5 and len(hex_color) != 9
        ):
            raise ValueError("HEX color must be in the format #RRGGBBAA.")
        if len(hex_color) == 5:
            hex_color = "#" + "".join([c * 2 for c in hex_color[1:]])
        return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5, 7))
