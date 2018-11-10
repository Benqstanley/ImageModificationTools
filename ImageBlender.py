from PIL import Image
import colorsys
import math

def replaceColor(color1, color2):
    oldh = colorsys.rgb_to_hls(color1[0], color1[1], color1[2])
    newh = colorsys.rgb_to_hls(color2[0], color2[1], color2[2])
    colorU = colorsys.hls_to_rgb(min(newh[0], oldh[0]), max(newh[1], oldh[1]), min(newh[2], oldh[2]))
    colorR = (int(colorU[0]), int(colorU[1]), int(colorU[2]))
    return colorR



path1 = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/DesignSupportingImages/Scroll 2WhitedOut"
path2 = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/DesignSupportingImages/bparchresized"
ext1 = ".png"
ext2 = ".jpg"
Style = Image.open(path2 + ext2)
Dest = Image.open(path1 + ext1)
dest = path1 + "Fucked.png"

for x in range(Dest.width):
    for y in range(Dest.height):
        print(Dest.getpixel((x,y)))
        if Dest.getpixel((x,y)) != (0, 0, 0, 255):
            newColor = replaceColor(Dest.getpixel((x,y)), Style.getpixel((x,y)))
            Dest.putpixel((x,y), newColor)
Dest.save(dest, "PNG")
Dest.show()