from PIL import Image
import colorsys

import math

fname = "C:/Users/Ben/Dropbox/Coding/Python Coding/ImageOutliner/For Ben/Originals/Horse"
fextension = ".jpg"
fdest = fname.replace("Originals", "Edited") + "TestOutliningDarkening.png"
picture = Image.open(fname + fextension)


rlower = 0
rupper = 0
glower = 0
gupper = 0
blower = 0
bupper = 255


x = 0
y = 0
total = int(picture.width)*int(picture.height)
Darkest = (255, 255, 255)
while x <= picture.width - 1:
    while y <= picture.height - 1:
        if picture.getpixel( (x, y) )[0] <= Darkest[0] and picture.getpixel( (x, y) )[1] <= Darkest[1] and picture.getpixel( (x, y) )[2] <= Darkest[2]:
            Darkest = picture.getpixel((x,y))
        y = y+1
    x = x+1
    y = 0
x = 0
y = 0
color = [0, 0, 0]

while x <= picture.width - 1:
    print("Percent Complete: " + str(x*picture.height/total*100))
    while y <= picture.height - 1:
        if (picture.getpixel((x,y))[0] >= rlower and picture.getpixel((x,y))[0] <= rupper) and \
                (picture.getpixel((x,y))[1] >= glower and picture.getpixel((x,y))[1] <= gupper) and \
                (picture.getpixel((x,y))[2] >= blower and picture.getpixel((x,y))[2] <= bupper):
            picture.putpixel((x,y), (255, 255, 255))
        else:
            for i in range(3):
                color[i] = picture.getpixel((x,y))[i] - Darkest[i]
                picture.putpixel((x,y), tuple(color))
        y = y+1
    x = x+1
    y = 0
picture.show()
picture.save(fdest, "PNG")

