import math

def color_dist(color1, color2):
    dist = math.sqrt(math.pow((color1[0] - color2[0]), 2) + math.pow((color1[1] - color2[1]), 2) + math.pow((color1[2] - color2[2]), 2))
    return dist
def directional_diff(color1, color2):
    rdist = color1[0] - color2[0]
    gdist = color1[1] - color2[1]
    bdist = color1[2] - color2[2]
    return (rdist, gdist, bdist)
ColorList = []
Blue = [(62, 253, 191), (125, 154, 189), (129, 186, 167), (61, 167, 254)]
BlueNames = ["urcornerblue", "ulcornerblue", 'brcornerblue', 'blcornerblue']
Purple = [(163, 60, 255), (254, 61, 152), (151, 131, 184), (187, 128, 165)]
PurpleNames = ['urcornerpurple', 'ulcornerpurple', 'brcornerpurple', 'blcornerpurple']

for j in (0, 1, 2, 3, 4, 5, 6, 7):
    colorname = "color" + str(j)
    exec(colorname + " = {}")

for j in (0, 1, 2, 3):
    colorname = "color" + str(j)
    exec(colorname + "['Label'] = BlueNames[j]")
    exec(colorname + "['Color Code'] = Blue[j]")
    exec("ColorList.append(" + colorname + ")")
for j in (4, 5, 6, 7):
    colorname = "color" + str(j)
    exec(colorname + "['Label'] = PurpleNames[j-4]")
    exec(colorname + "['Color Code'] = Purple[j-4]")
    exec("ColorList.append(" + colorname + ")")
print(ColorList)

for j in range(4):
    for l in range(4):
        print(ColorList[j]["Label"] + " and " + ColorList[l]["Label"])
        StrDist = "|" + str(ColorList[j]['Color Code']) + ", " + str(ColorList[l]['Color Code']) + "| = " + str(color_dist(ColorList[j]['Color Code'], ColorList[l]['Color Code']))
        print(StrDist)
        StrDirDiff = "||" + str(ColorList[j]['Color Code']) + ", " + str(ColorList[l]['Color Code']) +"|| = " + str(directional_diff(ColorList[j]['Color Code'], ColorList[l]['Color Code']))
        print(StrDirDiff)
    break

for j in range(4):
    for l in range(4):
        print(ColorList[j + 4]["Label"] + " and " + ColorList[l+4]["Label"])
        StrDist = "|" + str(ColorList[j+4]['Color Code']) + ", " + str(ColorList[l+4]['Color Code']) + "| = " + str(color_dist(ColorList[j+4]['Color Code'], ColorList[l+4]['Color Code']))
        print(StrDist)
        StrDirDiff = "||" + str(ColorList[j+4]['Color Code']) + ", " + str(ColorList[l+4]['Color Code']) +"|| = " + str(directional_diff(ColorList[j+4]['Color Code'], ColorList[l+4]['Color Code']))
        print(StrDirDiff)
    break