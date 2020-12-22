from tkinter.filedialog import askdirectory
from os import walk, path
from tkinter import Tk
from PIL import Image

gui=Tk().withdraw()

directory = ""
while directory == "":
	directory = askdirectory(title = "Select Pack")

for subdir, dirs, files in walk(directory):
	for file in files:
		if not file.endswith(".png"):
			continue
		img = Image.open(f"{subdir}/{file}")
		print(img.mode)
		if img.mode == "LA":
			img = img.convert("RGBA")
			img.save(path.join(subdir, file))
			print(f"Converted {file} to RGBA")
		elif img.mode == "L":
			img = img.convert("RGB")
			img.save(path.join(subdir, file))
			print(f"Converted {file} to RGB")
input()