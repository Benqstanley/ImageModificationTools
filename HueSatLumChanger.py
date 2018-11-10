from PIL import Image
import colorsys

import math

fname = "C:/Users/Ben/Dropbox/Coding/Python Coding/ImageOutliner/For Ben/Originals/Horse"
fextension = ".jpg"
pname = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/DesignSupportingImages/Scroll 2WhitedOut"
pext = ".png"


picture = Image.open(pname + pext)

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
bhupper1 = .63
bhlower1 = 0

phupper1 = 1
phlower1 = .0
Smod = .00
Lmod = .00
pdest = pname + str(bhlower1) + "-" + str(bhupper1) + "to" + str(phlower1) + "-" + str(phupper1)+ "L mod" + str(Lmod) + "S mod" + str(Smod) + ".png"

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
        newh = (1-newh)*(phupper1 - phlower1)
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
while x <= picture.width - 1:
    print("Percent Complete: " + str(x*picture.height/total*100))
    while y <= picture.height - 1:
        if (picture.getpixel((x,y))[0] >= brlower and picture.getpixel((x,y))[0] <= brupper) and \
                (picture.getpixel((x,y))[1] >= bglower and picture.getpixel((x,y))[1] <= bgupper) and \
                (picture.getpixel((x,y))[2] >= bblower and picture.getpixel((x,y))[2] <= bbupper):
            ncolor = findNewColor(picture.getpixel((x,y)))
            newcolor = (int(ncolor[0]), int(ncolor[1]), int(ncolor[2]))
            if newcolor != (1000, 1000, 1000):
                #print(newcolor)
                picture.putpixel((x, y), newcolor)



        #for i in range(8):

            # if color_dist(picture.getpixel((x,y)), ColorArray[i]) <= 20:
            #     for j in range(3):
            #         newcolor[j] = NewColorArray[i][j] + directional_diff(picture.getpixel((x,y)), ColorArray[i])[j]
            #     picture.putpixel((x,y), tuple(newcolor))
        # else:
            # for i in (0, 1, 2):
                # color[i] = picture.getpixel((x,y))[i] - Darkest[i]
        #     picture.putpixel( (x,y), tuple(color))

        y = y+1
    x = x+1
    y = 0
picture.show()
picture.save(pdest, "PNG")
