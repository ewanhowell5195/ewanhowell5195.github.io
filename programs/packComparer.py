from tkinter.filedialog import askdirectory
from filecmp import cmp as cmpfile
from os import getenv, walk, path
from zipfile import ZipFile
from shutil import rmtree
from tkinter import Tk

Tk().withdraw()

pack1 = ""
while pack1 == "":
	pack1 = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select First Pack")

pack2 = ""
while pack2 == "":
	pack2 = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Second Pack")

identical = []
for subdir, dirs, files in walk(path.join(pack1, "assets")):
	for file in files:
		if file.endswith(".mcmeta"):
			continue
		filePath = f"assets{path.join(subdir, file).split('assets')[1]}"
		try:
			if cmpfile(f"{pack1}/{filePath}", f"{pack2}/{filePath}"):
				identical.append(filePath.replace("assets", ""))
				print(f"Identical: {filePath.replace('assets', '')}")
			else:
				continue
		except:
			continue

with open(f"{path.basename(pack1)}_{path.basename(pack2)}_identicalFiles.txt", "w") as outFile:
	outFile.write("\n".join(identical))