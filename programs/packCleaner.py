from os import getenv, walk, path, remove, rmdir
from tkinter.filedialog import askdirectory
from zipfile import ZipFile
from shutil import rmtree
from tkinter import Tk
import filecmp

gui=Tk().withdraw()

directory = ""
while directory == "":
	directory = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Pack")

while True:
	try:
		version = input("Minecraft Version: ")
		with ZipFile(f"{getenv('APPDATA')}/.minecraft/versions/{version}/{version}.jar", "r") as zip_ref:
				print("Extracting JAR")
				zip_ref.extractall(f"{directory}/temp")
		break
	except:
		print("Please install that version first")

listOfFiles = []
for (dirpath, dirnames, filenames) in walk(f"{directory}/assets/"):
	listOfFiles += [path.join(dirpath, file) for file in filenames]

print(f"Checking for {version} vanilla files")

removed = []
for file in listOfFiles:
	fileSplit = file.rpartition("assets")
	packDir = f"{directory}/assets/{fileSplit[2]}"
	tempDir = f"{directory}/temp/assets/{fileSplit[2]}"
	try:
		if filecmp.cmp(packDir, tempDir):
			removed.append(f"{packDir.rpartition('assets')[2]}")
			remove(packDir)
		else:
			continue
	except FileNotFoundError:
		continue

print(f"Removed {len(removed)} vanilla assets")

print("Deleting extracted JAR")

rmtree(f"{directory}/temp")

if len(removed) == 0:
	input("Press ENTER to quit")
	quit()

folders = list(walk(f"{directory}/assets"))[1:]
folders.sort(key = len)
folders.reverse()

for folder in folders:
	if not folder[2]:
		try:
			rmdir(folder[0])
		except:
			continue

with open(f"{directory}/removed_files.txt", "w") as removedFile:
	for file in removed:
		removedFile.write(f"{file}\n")

print(f"Added 'removed_files.txt' to pack")

input("Press ENTER to quit")