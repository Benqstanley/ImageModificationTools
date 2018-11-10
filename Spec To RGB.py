from PIL import Image
import colorsys
color = [0, 0, 0]
picture = Image.new("RGB", (360, 100))
for x in range(picture.width):
    x_1 = x/360
    if x_1 >=.40 and x_1 <= .7:
        for y in range(picture.height):
            y_1 = y/100
            for i in (0, 1, 2):
                color[i] = int(colorsys.hls_to_rgb(x_1, .5, y_1)[i]*360)
            picture.putpixel((x,y), tuple(color))

picture.show()

picture.save("C:/Users/Ben/Desktop/Spectrum.png", "PNG")