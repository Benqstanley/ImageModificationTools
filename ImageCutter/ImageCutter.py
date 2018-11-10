from PIL import Image
import math

path = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/"
pname = "ScrollWhitedOut Transparent"
pext = ".png"
dname = pname + "Half"

picture = Image.open(path + pname + pext)

pieces = 13
cut = "horizontal"
if cut == "horizontal" or cut == "h":
    Heights = []
    for item in range(pieces):
        Cuts = {}
        Cuts["Beginning"] = math.ceil(picture.height/pieces * item)
        Cuts["End"] = math.floor(picture.height/pieces*(item+1))
        Cuts["Length"] = int(Cuts["End"] - Cuts["Beginning"])
        Heights.append(Cuts)
elif cut == "verticle" or cut == "v":
    Widths = []
    for item in range(pieces):
        Cuts = {}
        Cuts["Beginning"] = math.ceil(picture.height / pieces * item)
        Cuts["End"] = math.floor(picture.height / pieces * (item+1))
        Cuts["Length"] = int(Cuts["End"] - Cuts["Beginning"])
        Widths.append(Cuts)
ImageArray = []
count = 0
if cut == "horizontal" or cut == "h":
    count = 0
    for item in Heights:
        ImageArray.append(Image.new("RGBA", (picture.width, item["Length"])))
        for x in range(picture.width):
            for y in range(item["Beginning"], item["End"]):
                ImageArray[count].putpixel((x,y - item["Beginning"]), picture.getpixel((x,y)))
        ImageArray[count].save(path + dname + "HCut" + str(count + 1) + pext)
        count += 1
elif cut == "verticle" or cut == "v":
    count = 0
    for item in Widths:
        ImageArray.append(Image.new("RGBA", (picture.width, item["Length"])))
        for x in range(item["Beginning"], item["End"]):
            for y in range(picture.height):
                ImageArray[count].putpixel((x - item["Beginning"], y), picture.getpixel((x, y)))
        ImageArray[count].save(path + dname + "VCut" + str(count + 1) + pext)
        count += 1