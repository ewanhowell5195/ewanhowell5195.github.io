from tkinter.filedialog import askopenfilename
from sys import exit, argv
from tkinter import Tk
from PIL import Image

if len(argv) > 1:
	file = argv[1]
else:
	Tk().withdraw()
	file = askopenfilename(title = "Select Compact CTM", filetypes = [('PNG', '*.png')])
	if file == "":
		exit()

img = Image.open(file)

m = img.size[0] / 80

print(m)

ctm = Image.new("RGBA", (int(192*m), int(64*m)))

full = img.crop((0, 0, int(16*m), int(16*m)))
empty = img.crop((int(16*m), 0, int(32*m), int(16*m)))
eastWest = img.crop((int(32*m), 0, int(48*m), int(16*m)))
topBottom = img.crop((int(48*m), 0, int(64*m), int(16*m)))
corners = img.crop((int(64*m), 0, int(80*m), int(16*m)))
fullLeft = full.crop((0, 0, int(8*m), int(16*m)))
fullRight = full.crop((int(8*m), 0, int(16*m), int(16*m)))
fullTop = full.crop((0, 0, int(16*m), int(8*m)))
fullBottom = full.crop((0, int(8*m), int(16*m), int(16*m)))
topBottomLeft = topBottom.crop((0, 0, int(8*m), int(16*m)))
topBottomRight = topBottom.crop((int(8*m), 0, int(16*m), int(16*m)))
eastWestTop = eastWest.crop((0, 0, int(16*m), int(8*m)))
eastWestBottom = eastWest.crop((0, int(8*m), int(16*m), int(16*m)))
eastWestLeft = eastWest.crop((0, 0, int(8*m), int(16*m)))
eastWestRight = eastWest.crop((int(8*m), 0, int(16*m), int(16*m)))
topBottomTop = topBottom.crop((0, 0, int(16*m), int(8*m)))
topBottomBottom = topBottom.crop((0, int(8*m), int(16*m), int(16*m)))
fullTopLeft = full.crop((0, 0, int(8*m), int(8*m)))
fullTopRight = full.crop((int(8*m), 0, int(16*m), int(8*m)))
fullBottomLeft = full.crop((0, int(8*m), int(8*m), int(16*m)))
fullBottomRight = full.crop((int(8*m), int(8*m), int(16*m), int(16*m)))
topBottomTopLeft = topBottom.crop((0, 0, int(8*m), int(8*m)))
topBottomTopRight = topBottom.crop((int(8*m), 0, int(16*m), int(8*m)))
topBottomBottomLeft = topBottom.crop((0, int(8*m), int(8*m), int(16*m)))
topBottomBottomRight = topBottom.crop((int(8*m), int(8*m), int(16*m), int(16*m)))
eastWestTopLeft = eastWest.crop((0, 0, int(8*m), int(8*m)))
eastWestTopRight = eastWest.crop((int(8*m), 0, int(16*m), int(8*m)))
eastWestBottomLeft = eastWest.crop((0, int(8*m), int(8*m), int(16*m)))
eastWestBottomRight = eastWest.crop((int(8*m), int(8*m), int(16*m), int(16*m)))
cornersTopLeft = corners.crop((0, 0, int(8*m), int(8*m)))
cornersTopRight = corners.crop((int(8*m), 0, int(16*m), int(8*m)))
cornersBottomLeft = corners.crop((0, int(8*m), int(8*m), int(16*m)))
cornersBottomRight = corners.crop((int(8*m), int(8*m), int(16*m), int(16*m)))
emptyTopLeft = empty.crop((0, 0, int(8*m), int(8*m)))
emptyTopRight = empty.crop((int(8*m), 0, int(16*m), int(8*m)))
emptyBottomLeft = empty.crop((0, int(8*m), int(8*m), int(16*m)))
emptyBottomRight = empty.crop((int(8*m), int(8*m), int(16*m), int(16*m)))

ctm.paste(empty, (int(32*m), int(32*m)))
ctm.paste(empty, (int(16*m), int(16*m)))
ctm.paste(empty, (int(32*m), int(16*m)))
ctm.paste(empty, (int(16*m), int(32*m)))
ctm.paste(empty, (int(48*m), int(16*m)))
ctm.paste(empty, (int(16*m), int(48*m)))
ctm.paste(empty, (int(48*m), int(32*m)))
ctm.paste(empty, (int(32*m), int(48*m)))
ctm.paste(empty, (int(48*m), int(48*m)))
ctm.paste(empty, (int(64*m), int(32*m)))
ctm.paste(empty, (int(64*m), int(48*m)))
ctm.paste(empty, (int(80*m), int(32*m)))
ctm.paste(empty, (int(80*m), int(48*m)))
ctm.paste(empty, (int(96*m), int(32*m)))
ctm.paste(empty, (int(96*m), int(48*m)))
ctm.paste(empty, (int(112*m), int(32*m)))
ctm.paste(empty, (int(112*m), int(48*m)))
ctm.paste(empty, (int(128*m), int(32*m)))
ctm.paste(empty, (int(144*m), int(32*m)))
ctm.paste(empty, (int(128*m), int(48*m)))
ctm.paste(empty, (int(144*m), int(48*m)))
ctm.paste(empty, (int(160*m), 0))
ctm.paste(empty, (int(176*m), 0))
ctm.paste(empty, (int(160*m), int(16*m)))
ctm.paste(empty, (int(176*m), int(16*m)))
ctm.paste(empty, (int(160*m), int(32*m)))
ctm.paste(empty, (int(176*m), int(32*m)))

ctm.paste(corners, (int(96*m), 0))
ctm.paste(corners, (int(96*m), int(16*m)))
ctm.paste(corners, (int(112*m), 0))
ctm.paste(corners, (int(112*m), int(16*m)))
ctm.paste(corners, (int(128*m), 0))
ctm.paste(corners, (int(144*m), 0))
ctm.paste(corners, (int(128*m), int(16*m)))
ctm.paste(corners, (int(144*m), int(16*m)))

ctm.paste(full, (0, 0))
ctm.paste(eastWest, (0, int(32*m)))
ctm.paste(topBottom, (int(32*m), 0))
ctm.paste(corners, (int(160*m), int(48*m)))
ctm.paste(fullLeft, (int(16*m), 0))
ctm.paste(fullRight, (int(56*m), 0))
ctm.paste(fullTop, (0, int(16*m)))
ctm.paste(fullBottom, (0, int(56*m)))
ctm.paste(topBottomLeft, (int(48*m), 0))
ctm.paste(topBottomRight, (int(24*m), 0))
ctm.paste(eastWestTop, (0, int(48*m)))
ctm.paste(eastWestBottom, (0, int(24*m)))
ctm.paste(topBottomTop, (int(32*m), int(16*m)))
ctm.paste(eastWestLeft, (int(16*m), int(32*m)))
ctm.paste(topBottomBottom, (int(32*m), int(56*m)))
ctm.paste(eastWestRight, (int(56*m), int(32*m)))
ctm.paste(topBottomTop, (int(112*m), 0))
ctm.paste(topBottomTop, (int(112*m), int(32*m)))
ctm.paste(topBottomBottom, (int(96*m), int(24*m)))
ctm.paste(topBottomBottom, (int(96*m), int(56*m)))
ctm.paste(eastWestLeft, (int(96*m), 0))
ctm.paste(eastWestLeft, (int(96*m), int(32*m)))
ctm.paste(eastWestRight, (int(120*m), int(16*m)))
ctm.paste(eastWestRight, (int(120*m), int(48*m)))
ctm.paste(fullTopLeft, (int(16*m), int(16*m)))
ctm.paste(fullTopRight, (int(56*m), int(16*m)))
ctm.paste(fullBottomLeft, (int(16*m), int(56*m)))
ctm.paste(fullBottomRight, (int(56*m), int(56*m)))
ctm.paste(topBottomTopRight, (int(24*m), int(16*m)))
ctm.paste(topBottomTopLeft, (int(48*m), int(16*m)))
ctm.paste(topBottomBottomRight, (int(24*m), int(56*m)))
ctm.paste(topBottomBottomLeft, (int(48*m), int(56*m)))
ctm.paste(eastWestTopRight, (int(56*m), int(48*m)))
ctm.paste(eastWestTopLeft, (int(16*m), int(48*m)))
ctm.paste(eastWestBottomRight, (int(56*m), int(24*m)))
ctm.paste(eastWestBottomLeft, (int(16*m), int(24*m)))
ctm.paste(topBottomTop, (int(80*m), int(32*m)))
ctm.paste(topBottomBottom, (int(64*m), int(56*m)))
ctm.paste(eastWestLeft, (int(64*m), int(32*m)))
ctm.paste(eastWestRight, (int(88*m), int(48*m)))
ctm.paste(fullTopLeft, (int(64*m), 0))
ctm.paste(topBottomTopRight, (int(72*m), 0))
ctm.paste(topBottomTopLeft, (int(80*m), 0))
ctm.paste(fullTopRight, (int(88*m), 0))
ctm.paste(fullBottomLeft, (int(64*m), int(24*m)))
ctm.paste(topBottomBottomRight, (int(72*m), int(24*m)))
ctm.paste(topBottomBottomLeft, (int(80*m), int(24*m)))
ctm.paste(fullBottomRight, (int(88*m), int(24*m)))
ctm.paste(cornersTopRight, (int(72*m), int(32*m)))
ctm.paste(cornersBottomRight, (int(88*m), int(40*m)))
ctm.paste(cornersTopLeft, (int(64*m), int(48*m)))
ctm.paste(cornersBottomLeft, (int(80*m), int(56*m)))
ctm.paste(cornersBottomRight, (int(72*m), int(8*m)))
ctm.paste(cornersBottomLeft, (int(80*m), int(8*m)))
ctm.paste(cornersTopRight, (int(72*m), int(16*m)))
ctm.paste(cornersTopLeft, (int(80*m), int(16*m)))
ctm.paste(eastWestBottomLeft, (int(64*m), int(8*m)))
ctm.paste(eastWestTopLeft, (int(64*m), int(16*m)))
ctm.paste(eastWestBottomRight, (int(88*m), int(8*m)))
ctm.paste(eastWestTopRight, (int(88*m), int(16*m)))
ctm.paste(cornersBottomRight, (int(104*m), int(40*m)))
ctm.paste(cornersBottomLeft, (int(112*m), int(40*m)))
ctm.paste(cornersTopRight, (int(104*m), int(48*m)))
ctm.paste(cornersTopLeft, (int(112*m), int(48*m)))
ctm.paste(emptyTopRight, (int(136*m), 0))
ctm.paste(emptyTopLeft, (int(128*m), int(16*m)))
ctm.paste(emptyBottomRight, (int(152*m), int(8*m)))
ctm.paste(emptyBottomLeft, (int(144*m), int(24*m)))
ctm.paste(cornersBottomRight, (int(136*m), int(40*m)))
ctm.paste(cornersBottomLeft, (int(144*m), int(40*m)))
ctm.paste(cornersTopRight, (int(136*m), int(48*m)))
ctm.paste(cornersTopLeft, (int(144*m), int(48*m)))
ctm.paste(cornersTopRight, (int(168*m), 0))
ctm.paste(cornersBottomRight, (int(168*m), int(8*m)))
ctm.paste(cornersBottomLeft, (int(176*m), int(8*m)))
ctm.paste(cornersBottomRight, (int(184*m), int(8*m)))
ctm.paste(cornersTopLeft, (int(160*m), int(16*m)))
ctm.paste(cornersTopRight, (int(168*m), int(16*m)))
ctm.paste(cornersTopLeft, (int(176*m), int(16*m)))
ctm.paste(cornersBottomLeft, (int(176*m), int(24*m)))
ctm.paste(cornersTopLeft, (int(160*m), int(32*m)))
ctm.paste(cornersTopRight, (int(184*m), int(32*m)))
ctm.paste(cornersBottomRight, (int(168*m), int(40*m)))
ctm.paste(cornersBottomLeft, (int(176*m), int(40*m)))

ctm.save(f"{file[:-4]}_full_ctm.png")