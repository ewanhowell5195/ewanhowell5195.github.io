from tkinter.filedialog import askdirectory
from os import walk, getenv
from tkinter import Tk
from PIL import Image

gui=Tk().withdraw()

directory = ""
while directory == "":
	directory = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Pack")

assetsDir = f"{directory}/assets/minecraft/textures"

def scrolling(textureDir):
	for subdir, dirs, files in walk(textureDir):
		for file in files:
			if not file.endswith(".png"):
				continue
			img = Image.open(f"{subdir}/{file}")
			w, h = img.size
			newImg = Image.new("RGBA", (w, w * w), (0, 0, 0, 0))
			x = 0
			while x < w:
				newImg.paste(img, (x, w * x))
				newImg.paste(img, (x - w, w * x))
				x += 1
			with open(f"{subdir}/{file}.mcmeta", "w") as mcmeta:
				mcmeta.write('{ "animation": { "frametime": 1 } }')
			newImg.save(f"{subdir}/{file}")
			print(f"Done {file}")

scrolling(f"{directory}/assets/minecraft/textures/block")
scrolling(f"{directory}/assets/minecraft/textures/item")