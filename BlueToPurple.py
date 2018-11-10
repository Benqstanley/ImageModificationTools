from PIL import Image
import colorsys

import math

fname = "C:/Users/Ben/My Documents/MEGASync/Coding/Python Coding/ImageOutliner/For Ben/Originals/D20Image"
fextension = ".jpg"
pname = "C:/Users/Ben/My Documents/MEGASync/Coding/Python Coding/ImageOutliner/For Ben/Edited/D20ImageGreenI"
pext = ".png"

pdest = pname + pext


picture = Image.open(fname + fextension)

brlower = 0
brupper = 185
bglower = 70
bgupper = 253
bblower = 167
bbupper = 255

prlower = 151
prupper = 254
pglower = 9
pgupper = 141
pblower = 152
pbupper = 255

bhupper1 = 240/240
bhlower1 = 150/240

phupper1 = 37/240
phlower1 = 85/240
Smod = .00
Lmod = .00

bhupper2 = 2
bhlower2 = 2.5
phupper2 = 2
phlower2 = 2.5

def color_dist(color1, color2):
    dist = math.sqrt(math.pow((color1[0] - color2[0]), 2) + math.pow((color1[1] - color2[1]), 2) + math.pow((color1[2] - color2[2]), 2))
    return dist
def directional_diff(color1, color2):
    rdist = color1[0] - color2[0]
    gdist = color1[1] - color2[1]
    bdist = color1[2] - color2[2]
    return (rdist, gdist, bdist)
def findNewColor(color):
    h = colorsys.rgb_to_hls(color[0], color[1], color[2])
    #print(h)
    if h[0] <= bhupper1 and h[1] >= bhlower1:
        #print("entered here")
        newh = (h[0]-bhlower1)/(bhupper1-bhlower1)
        newh = newh*(phupper1 - phlower1)
        newh = newh + phlower1
        if newh > .8:
            print("What the fuck?")
        return colorsys.hls_to_rgb(newh, h[1] + Smod, h[2]+Lmod)
    # elif h[0] <= bhupper2 and h[1] >= bhlower2:
    #     #print("entered here")
    #     newh = (h[0]-bhlower2)/(bhupper2-bhlower2)
    #     newh = (1-newh)*(phupper2 - phlower2)
    #     newh = newh + phlower2
    #     return colorsys.hls_to_rgb(newh, h[1], h[2])
    else:
        return (1000, 1000, 1000)


x = 0
y = 0
total = int(picture.width)*int(picture.height)
# Darkest = (255, 255, 255)
# while x <= picture.width - 1:
#     while y <= picture.height - 1:
#         if picture.getpixel( (x, y) )[0] <= Darkest[0] and picture.getpixel( (x, y) )[1] <= Darkest[1] and picture.getpixel( (x, y) )[2] <= Darkest[2]:
#             Darkest = picture.getpixel((x,y))
#         y = y+1
#     x = x+1
#     y = 0
# x = 0
# y = 0
# color = [0, 0, 0]
ColorArray = [(118, 228, 253), (50, 156, 240), (66, 238, 248), (14, 102, 236), (76, 235, 254), (10, 91, 222),
              (150, 232, 254), (62, 214, 253)]
NewColorArray = [(240, 118, 254), (241, 48, 150), (250, 65, 167), (211, 11, 240), (240, 75, 254), (186, 7, 224),
                 (237, 149, 255), (201, 61, 254)]

image = Image.new("RGB", (512,512), (255,255, 255))
while x <= picture.width - 1:
    print("Percent Complete: " + str(x*picture.height/total*100))
    while y <= picture.height - 1:
        # if (picture.getpixel((x,y))[0] >= brlower and picture.getpixel((x,y))[0] <= brupper) and \
        #         (picture.getpixel((x,y))[1] >= bglower and picture.getpixel((x,y))[1] <= bgupper) and \
        #         (picture.getpixel((x,y))[2] >= bblower and picture.getpixel((x,y))[2] <= bbupper):
        ncolor = findNewColor(picture.getpixel((x,y)))
        newcolor = (int(ncolor[0]), int(ncolor[1]), int(ncolor[2]))
        if newcolor != (1000, 1000, 1000):
            #print(newcolor)
            image.putpixel((x, y), newcolor)

        y = y+1
    x = x+1
    y = 0
image.show()
image.save(pdest, "PNG")

