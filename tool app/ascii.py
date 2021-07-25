#from PIL import Image, ImageDraw, ImageFont

from PIL import Image as anh
from PIL import ImageDraw as anh1
from PIL import ImageFont as anh2

import math
def build():
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,`'. "[::-1]
    #chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    scaleFactor = 0.2

    oneCharWidth = 10
    oneCharHeight = 30

    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]

    text_file = open("Output.txt", "w")

    im = anh.open("album/my.jpg")

    fnt = anh2.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), anh.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = anh.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = anh1.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            #r, g, b = pix[j, i]
            pixel = pix[j, i]
            r, g, b = pixel[0], pixel[1], pixel[2]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
     
        text_file.write('\n')

    outputImage.save('output.png')
build()
