from PIL import Image, ImageOps
from sys import argv
from os import path

for image in argv[1:]:
	img = Image.open(image)

	width, height = img.size

	file = path.basename(image).rsplit(".", 1)[0]

	m = height // 64

	if width == height:
		lidTop = img.crop((14*m, 0, 28*m, 14*m))
		lidTop = ImageOps.flip(lidTop)

		lidBottom = img.crop((28*m, 0, 42*m, 14*m))
		lidBottom = ImageOps.flip(lidBottom)

		baseTop = img.crop((14*m, 19*m, 28*m, 33*m))
		baseTop = ImageOps.flip(baseTop)

		baseBottom = img.crop((28*m, 19*m, 42*m, 33*m))
		baseBottom = ImageOps.flip(baseBottom)

		knobTop = img.crop((1*m, 0, 3*m, 1*m))
		knobBottom = img.crop((3*m, 0, 5*m, 1*m))

		lidEast = img.crop((0, 14*m, 14*m, 19*m))
		lidEast = lidEast.rotate(180)

		lidSides = img.crop((14*m, 14*m, 56*m, 19*m))
		lidSides = lidSides.rotate(180)

		baseEast = img.crop((0, 33*m, 14*m, 43*m))
		baseEast = baseEast.rotate(180)

		baseSides = img.crop((14*m, 33*m, 56*m, 43*m))
		baseSides = baseSides.rotate(180)

		knobEast = img.crop((0, 1*m, 1*m, 5*m))
		knobEast = knobEast.rotate(180)

		knobSides = img.crop((1*m, 1*m, 6*m, 5*m))
		knobSides = knobSides.rotate(180)

		img.paste(lidTop,(28*m, 0))
		img.paste(lidBottom,(14*m, 0))
		img.paste(baseTop,(28*m, 19*m))
		img.paste(baseBottom,(14*m, 19*m))
		img.paste(knobTop,(3*m, 0))
		img.paste(knobBottom,(1*m, 0))
		img.paste(lidEast,(0, 14*m))
		img.paste(lidSides,(14*m, 14*m))
		img.paste(baseEast,(0, 33*m))
		img.paste(baseSides,(14*m, 33*m))
		img.paste(knobEast,(0, 1*m))
		img.paste(knobSides,(1*m, 1*m))

		img.save(f"{file}_new.png")

	else:

		lidTop = img.crop((14*m, 0, 44*m, 14*m))
		lidTop = ImageOps.flip(lidTop)

		lidBottom = img.crop((44*m, 0, 74*m, 14*m))
		lidBottom = ImageOps.flip(lidBottom)

		baseTop = img.crop((14*m, 19*m, 44*m, 33*m))
		baseTop = ImageOps.flip(baseTop)

		baseBottom = img.crop((44*m, 19*m, 74*m, 33*m))
		baseBottom = ImageOps.flip(baseBottom)

		knobTop = img.crop((1*m, 0, 3*m, 1*m))
		knobBottom = img.crop((3*m, 0, 5*m, 1*m))

		lidEast = img.crop((0, 14*m, 14*m, 19*m))
		lidEast = lidEast.rotate(180)

		lidSides = img.crop((14*m, 14*m, 88*m, 19*m))
		lidSides = lidSides.rotate(180)

		baseEast = img.crop((0, 33*m, 14*m, 43*m))
		baseEast = baseEast.rotate(180)

		baseSides = img.crop((14*m, 33*m, 88*m, 43*m))
		baseSides = baseSides.rotate(180)

		knobEast = img.crop((0, 1*m, 1*m, 5*m))
		knobEast = knobEast.rotate(180)

		knobSides = img.crop((1*m, 1*m, 6*m, 5*m))
		knobSides = knobSides.rotate(180)

		img.paste(lidTop,(44*m, 0))
		img.paste(lidBottom,(14*m, 0))
		img.paste(baseTop,(44*m, 19*m))
		img.paste(baseBottom,(14*m, 19*m))
		img.paste(knobTop,(3*m, 0))
		img.paste(knobBottom,(1*m, 0))
		img.paste(lidEast,(0, 14*m))
		img.paste(lidSides,(14*m, 14*m))
		img.paste(baseEast,(0, 33*m))
		img.paste(baseSides,(14*m, 33*m))
		img.paste(knobEast,(0, 1*m))
		img.paste(knobSides,(1*m, 1*m))

		leftLidTop = img.crop((59*m, 0, 74*m, 14*m))
		rightLidTop = img.crop((44*m, 0, 59*m, 14*m))

		leftLidBottom = img.crop((29*m, 0, 44*m, 14*m))
		rightLidBottom = img.crop((14*m, 0, 29*m, 14*m))

		leftBaseTop = img.crop((59*m, 19*m, 74*m, 33*m))
		rightBaseTop = img.crop((44*m, 19*m, 59*m, 33*m))

		leftBaseBottom = img.crop((29*m, 19*m, 44*m, 33*m))
		rightBaseBottom = img.crop((14*m, 19*m, 29*m, 33*m))

		leftKnobTop = img.crop((2*m, 0, 3*m, 1*m))
		rightKnobTop = img.crop((1*m, 0, 2*m, 1*m))

		leftKnobBottom = img.crop((4*m, 0, 5*m, 1*m))
		rightKnobBottom = img.crop((3*m, 0, 4*m, 1*m))

		leftLidSides = img.crop((29*m, 14*m, 73*m, 19*m))
		rightLidFront = img.crop((73*m, 14*m, 88*m, 19*m))
		rightLidSides = img.crop((0, 14*m, 29*m, 19*m))

		leftBaseSides = img.crop((29*m, 33*m, 73*m, 43*m))
		rightBaseFront = img.crop((73*m, 33*m, 88*m, 43*m))
		rightBaseSides = img.crop((0, 33*m, 29*m, 43*m))

		leftKnobSides = img.crop((2*m, 1*m, 5*m, 5*m))
		rightKnobFront = img.crop((5*m, 1*m, 6*m, 5*m))
		rightKnobSides = img.crop((0, 1*m, 2*m, 5*m))

		leftImg = Image.new('RGBA', (64*m, 64*m), (0, 0, 0, 0))

		leftImg.paste(leftLidTop,(29*m, 0))
		leftImg.paste(leftLidBottom,(14*m, 0))
		leftImg.paste(leftBaseTop,(29*m, 19*m))
		leftImg.paste(leftBaseBottom,(14*m, 19*m))
		leftImg.paste(leftLidSides,(14*m, 14*m))
		leftImg.paste(leftBaseSides,(14*m, 33*m))
		leftImg.paste(leftKnobTop,(1*m, 0))
		leftImg.paste(leftKnobBottom,(2*m, 0))
		leftImg.paste(leftKnobSides,(1*m, 1*m))

		rightImg = Image.new('RGBA', (64*m, 64*m), (0, 0, 0, 0))

		rightImg.paste(rightLidTop,(29*m, 0))
		rightImg.paste(rightLidBottom,(14*m, 0))
		rightImg.paste(rightBaseTop,(29*m, 19*m))
		rightImg.paste(rightBaseBottom,(14*m, 19*m))
		rightImg.paste(rightLidSides,(0, 14*m))
		rightImg.paste(rightLidFront,(43*m, 14*m))
		rightImg.paste(rightBaseSides,(0, 33*m))
		rightImg.paste(rightBaseFront,(43*m, 33*m))
		rightImg.paste(rightKnobTop,(1*m, 0))
		rightImg.paste(rightKnobBottom,(2*m, 0))
		rightImg.paste(rightKnobSides,(0, 1*m))
		rightImg.paste(rightKnobFront,(3*m, 1*m))

		leftImg.save(f"{file}_left.png")
		rightImg.save(f"{file}_right.png")