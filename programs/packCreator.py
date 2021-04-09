from distutils.dir_util import copy_tree
import json, os, zipfile, shutil
from PIL import Image
from glob import glob

passed = False
while passed == False:
	packName = input("Enter pack name: ")
	print(f"Selected pack name: {packName}")

	path = (f"{os.getcwd()}\\{packName}")
	packs = glob(f"{os.getcwd()}/*/")

	passed = True

	for pack in packs:
		packSplit = pack.split("\\")
		if packName.lower() == packSplit[-2].lower():
			print("Pack already exists")
			passed = False


print(f"Creating path '{path}'")
os.mkdir(path)
print(f"Creating path '{path}\\assets'")
os.mkdir(f"{path}/assets")
print(f"Creating path '{path}\\assets\\minecraft'")
os.mkdir(f"{path}/assets/minecraft")

description = input("Enter description: ")

while True:
	try:
		packFormat = int(input("Enter format number: "))
		break
	except:
		print("Not a number")

data = {}
data["pack"] = {
	"description": description,
	"pack_format": packFormat
}

with open(f"{packName}/pack.mcmeta","w") as outFile:
	outFile.write(json.dumps(data, indent = 2))

print(f"Added 'pack.mcmeta'\n    description = '{description}'\n    version = {packFormat}")

Image.new('RGBA', (256, 256), (256, 256, 256, 256)).save(f"{packName}/pack.png")

print("Added blank 'pack.png'")

print("---\nBuilt empty pack successfully\n---")

copy = "e"
while not copy in ["y", "n", "yes", "no"]:
	copy = input("Copy in vanilla assets? (y/n): ")

if "n" in copy:
	quit()

while True:
	try:
		version = input("Minecraft Version: ")
		with zipfile.ZipFile(f"{os.getenv('APPDATA')}/.minecraft/versions/{version}/{version}.jar", "r") as zip_ref:
				print("Extracting JAR")
				zip_ref.extractall(f"{path}/temp")
		break
	except:
		print("Please install that version first")

print("Copying assets")
copy_tree(f"{path}/temp/assets", f"{path}/assets")

shutil.rmtree(f"{path}/temp")

print("---\nCopied vanilla assets successfully\n---")

input("Press ENTER to quit")