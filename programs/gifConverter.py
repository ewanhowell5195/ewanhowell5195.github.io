from tkinter.filedialog import askopenfilename
from tkinter import Tk
from PIL import Image, ImageSequence

Tk().withdraw()

file = ""
while file == "":
	file = askopenfilename(title = "Select GIF", filetypes = [('GIF', '*.gif')])

img = Image.open(file)

w, h = img.size

newImg = Image.new("RGBA", (w, h * img.n_frames), (0, 0, 0, 0))

x = 0
for frame in ImageSequence.Iterator(img):
	newImg.paste(frame, (0, h * x))

	print(f"Done frame {x}")

	x += 1
	
newImg.save("gif.png")