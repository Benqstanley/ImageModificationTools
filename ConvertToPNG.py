from PIL import Image
fname = "C:/Users/Ben/Dropbox/Coding/Python Coding/ImageOutliner/For Rob/Originals/QuestionMarksRob"
fextension = ".jpg"
fdest = fname.replace("Originals", "Edited") + ".png"
file = fname + fextension
picture = Image.open(file)
picture.save(fdest, "PNG")