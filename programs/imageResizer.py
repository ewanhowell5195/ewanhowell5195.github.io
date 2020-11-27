from tkinter.filedialog import askdirectory
from re import search as regexsearch
from os import walk, path, getenv
from tkinter import Tk
from PIL import Image

gui=Tk().withdraw()

rootdir = ""
while rootdir == "":
	rootdir = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Pack")

print("Please enter a fraction of the original size that you want to resize to.\nFor example, 16x16 -> 8x8 would be 1/2, and 16x16 -> 32x32 would be 2/1")

passed = False
while passed == False:
	fraction = input("Fraction: ")
	try:
		split = fraction.split("/")
		num1 = int(split[0])
		num2 = int(split[1])
		if (not (num1 % 2) == 0 and not num1 == 1) or (not (num2 % 2) == 0 and not num2 == 1):
			print("Only use even numbers or 1")
			continue
		passed = True
	except:
		print("Invalid Fraction")


for subdir, dirs, files in walk(rootdir):
	for file in files:

		if not file.endswith(".png"):
			continue

		if regexsearch("font|colormap", path.join(subdir, file)) != None:
			continue

		try:
			img = Image.open(f"{subdir}/{file}")
			
			width, height = img.size
			newWidth=int(width/num2*num1)
			newHeight=int(height/num2*num1)

			imResize = img.resize((newWidth,newHeight), Image.NEAREST)
			imResize.save(path.join(subdir, file), 'PNG', quality = 100)

			print(f"Resized {file} to {newWidth}x{newHeight}")
		except:
			print(f"{file} failed to resize")

input("Press ENTER to continue")