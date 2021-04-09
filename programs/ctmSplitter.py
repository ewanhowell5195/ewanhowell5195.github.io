from tkinter.filedialog import askopenfilename
from os import getenv, path
from tkinter import Tk
from PIL import Image

def check(n):
    if (n == 0): 
        return False
    while (n != 1): 
        if (n % 2 != 0): 
            return False
        n = n // 2  
    return True

passed = False
while not passed:
	try:
		res = int(input("Enter pack resolution: "))
		passed = check(res)
	except:
		print("Invalid Resolution")

Tk().withdraw()

file = ""
while file == "":
	file = askopenfilename(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select CTM Template", filetypes = [('PNG', '*.png')])

directory = path.dirname(file)

img = Image.open(file)

w, h = img.size

width = w // res
height = h // res

for i in range(height):
	for o in range(width):
		imgCrop = img.crop((o * res, i * res, o * res + res, i * res + res))
		fileName = width * i + o
		imgCrop.save(f"{directory}/{fileName}.png")
		print(f"Done {fileName}.png")