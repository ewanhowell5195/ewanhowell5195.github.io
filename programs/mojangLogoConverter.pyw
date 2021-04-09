from PIL import Image, ImageOps
from sys import argv
from os import path

for image in argv[1:]:
	img = Image.open(image)

	width, height = img.size

	if width < 512 or height < 512:
		img = img.resize((512, 512), Image.NEAREST)
		width, height = img.size

	file = path.basename(image).rsplit(".", 1)[0]

	m = height // 512

	leftSide = img.crop((0, 192*m, 256*m, 320*m))
	rightSide = img.crop((256*m, 192*m, 512*m, 320*m))

	newImg = Image.new('RGBA', (256*m, 256*m), (0, 0, 0, 0))

	newImg.paste(leftSide,(0, 0))
	newImg.paste(rightSide,(0, 128*m))

	newImg.save(f"{file}studios.png")