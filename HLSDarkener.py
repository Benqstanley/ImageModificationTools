from PIL import Image
import colorsys

import math
#Picture Path

fname = "C:/Users/Ben/Dropbox/Coding/Python Coding/ImageOutliner/For Ben/Originals/MapGuy"
fext = ".jpg"
pname = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/DesignSupportingImages/Scroll 2WhitedOut"
pext = ".png"

#open picture

picture = Image.open(fname + fext)

# Parameters

#Destination Path

pdest = fname + "Darkened.png"
init = list((0, 0, 0))
HLScolorArray = [[init for x in range(picture.width)] for i in range(picture.height)]
RGBcolorArray = [[init for x in range(picture.width)] for i in range(picture.height)]
newRGB = [[init for x in range(picture.width)] for i in range(picture.height)]
def findMinLum(image):
    global HLScolorArray
    minLum = 1
    color = (0, 0, 0)
    for x in range(image.width):
        for y in range(image.height):
            color = image.getpixel((x,y))
            HLScolorArray[y][x] = colorsys.rgb_to_hls(color[0], color[1], color[2])
            if HLScolorArray[y][x][2] < minLum:
                minLum = HLScolorArray[y][x][2]
    return minLum


def makeImage(minLum):
    global picture
    global HLScolorArray
    global RGBcolorArray
    global newRGB
    for x in range(picture.width):
        for y in range(picture.height):
            color = (HLScolorArray[y][x][0], HLScolorArray[y][x][1], HLScolorArray[y][x][2] - minLum)
            RGBcolorArray[y][x] = tuple(colorsys.hls_to_rgb(color[0], color[1], color[2]))
            current = list(RGBcolorArray[y][x])
            newRGB[y][x] = (int(current[0]), int(current[1]), int(current[2]))
    return minLum

minLum = findMinLum(picture)
makeImage(minLum)
for x in range(picture.width):
    for y in range(picture.height):
        picture.putpixel((x,y), newRGB[y][x])

picture.show()
picture.save(pdest, "PNG")
