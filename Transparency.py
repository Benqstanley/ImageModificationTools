from PIL import Image
fname = "C:/Users/Ben/My Documents/MEGAsync/Coding/Python Coding/ImageOutliner/For Ben/Originals/Banner_Zianderthals_Plate"
fextension = ".png"
fdest = fname.replace("Originals", "Edited") + " Transparent.png"
fnow = fname.replace("Originals", "Edited") + ".png"

picture = Image.open(fname + fextension)


print(picture)
x = 0
y = 0

picture = picture.convert("RGBA")
datas = picture.getdata()
pixdata = picture.load()
total = int(picture.width)*int(picture.height)
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
        print("Making Things Transparent")
    else:
        newData.append(item)
picture.putdata(newData)

# while x <= picture.width - 1:
#     print("Percent Complete: " + str(x*picture.height/total*100))
#     while y <= picture.height - 1:
#         print(pixdata[x,y])
#         if pixdata[x, y] == (255, 255, 255, 255):
#             print("Making Things Transparent")
#             pixdata[x, y] = (255, 255, 255, 0)
#         y = y+1
#     x = x+1
#     y = 0



picture.show()
picture.save(fdest, "PNG")

