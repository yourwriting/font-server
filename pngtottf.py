from __future__ import print_function
import sys
import fontforge
from PIL import Image
Image.MAX_IMAGE_PIXELS=1000000000

def makefont(width, height):
    output = "result.ttf"
    image = Image.open('./concat.PNG')

    factor = 10 # size factor so that coords are in range [16, 65536]
    private_range = 0xAC00
    #background = (0, 0, 0) # background RGB color
    background = (255, 255, 255)

    font = fontforge.font()
    font.ascent = height * factor
    font.descent = 0 * factor
    font.encoding = 'KSC5601' # required encoding to access private range
    #font.encoding = 'UnicodeFull'

    # 설정할 글꼴 이름과 스타일
    font.familyname = "realWriting"
    font.fontname = "realWriting"
    font.fullname = "realWriting"
    font.weight = "Book"  # 글꼴 무게 (예: Book, Bold 등)

    pixels = image.load()

    for j in range(image.height // height):
        for i in range(image.width // width):
            offset = i + j * (image.width // width)

            for codepoint in [offset, private_range + offset]:
                char = font.createChar(codepoint)
                char.width = width * factor
                pen = char.glyphPen()

                # draw each non-background pixel as a square
                for y in range(height):
                    for x in range(width):
                        pixel = pixels[i * width + x, j * height + y]
                        if pixel != background:
                            pen.moveTo((x * factor, (height - y) * factor)) # draw a pixel
                            pen.lineTo(((x + 1) * factor, (height - y) * factor))
                            pen.lineTo(((x + 1) * factor, (height - y - 1) * factor))
                            pen.lineTo((x * factor, (height - y - 1) * factor))
                            pen.closePath()

    # export to font
    font.generate(output, flags=('opentype'))