from PIL import Image
import os, sys

def resize(folder, width, height, mode):
	print(f"Scanning {folder}")
	rootdir = f"E:/Programming/GitHub/ewanhowell/assets/images/{folder}"
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			if not file.endswith(".png"):
				continue
			img = Image.open(os.path.join(subdir, file)).convert("RGBA")
			imgwidth, imgheight = img.size
			if imgwidth == width and imgheight == height:
				continue
			img.resize((width, height), mode).save(os.path.join(subdir, file), 'PNG', quality = 100)
			print("Resized " + file)

resize("banners", 400, 160, Image.BILINEAR)
resize("showcase-images", 1920, 1080, Image.BILINEAR)
resize("icons", 256, 256, Image.NEAREST)

input("Finished")