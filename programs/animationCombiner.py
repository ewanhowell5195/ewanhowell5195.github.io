from tkinter.filedialog import askdirectory
from os import listdir, path
from tkinter import Tk
from PIL import Image

Tk().withdraw()

passed = False
while passed == False:
	res = int(input("Enter texture resolution: "))
	passed = True

directory = ""
while directory == "":
	directory = askdirectory(title = "Select Folder")

files = listdir(directory)

fileCount = 0
for file in files:
	if not file.endswith(".png"):
		continue
	fileCount += 1

newImg = Image.new("RGBA", (res, res * fileCount), (0, 0, 0, 0))

x = 0
for file in listdir(directory):
	if not file.endswith(".png"):
		continue
	img = Image.open(path.join(directory, file)).convert("RGBA")
	newImg.paste(img, (0, x))
	print(f"Added {file}")
	x += res

newImg.save(path.join(directory, "animation.png"))
input("Press ENTER to exit")