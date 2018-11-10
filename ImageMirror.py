from PIL import Image

pname = "C:/Users/Ben/Dropbox/Coding/App Coding/D&D App Design Stuff/DesignSupportingImages/Scroll 2"
fname = "C:/Users/Ben/Dropbox/Coding/Python Coding/ImageOutliner/For Ben/Originals/swoopytoinvert"
fextension = ".png"
fdest = fname.replace("Originals", "Edited") + "Inverted.png"
picture = Image.open(fname + fextension)
pdest = pname + "WhitedOut.png"
mirror = Image.new('RGB', (picture.width, picture.height))
xtot = picture.width-1
ytot = picture.height-1
for x in range(picture.width):
    for y in range(picture.height):
        mirror.putpixel((x, ytot-y), picture.getpixel((x,y)))

mirror.save(fdest, 'PNG')
