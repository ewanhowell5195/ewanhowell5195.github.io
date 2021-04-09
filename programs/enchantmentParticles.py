from tkinter.filedialog import askopenfilename
from string import ascii_lowercase
from tkinter import Tk
from os import getenv
from PIL import Image

Tk().withdraw()

imgDir = ""
while imgDir == "":
	imgDir = askopenfilename(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select ASCII SGA File", filetypes = [("PNG", "ascii_sga.png")])

img = Image.open(imgDir)

w, h = img.size

m =  w // 128

w = 8
h = 32
for letter in ascii_lowercase:
	if letter == "p":
		w = 0
		h = 40
	sga = img.crop((w*m, h*m, (w+8)*m, (h+8)*m))
	sga.save(f"sga_{letter}.png")
	w += 8