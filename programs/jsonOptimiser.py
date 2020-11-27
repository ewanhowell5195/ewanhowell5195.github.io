from tkinter.filedialog import askdirectory
from os import walk, path, getenv
from json import load, dumps
from tkinter import Tk

gui=Tk().withdraw()

rootdir = ""
while rootdir == "":
	rootdir = askdirectory(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Pack")

beforeSize = 0
for subdir, dirs, files in walk(rootdir):
	for file in files:
		if file.endswith(".json") or file.endswith(".jem"):
			beforeSize += path.getsize(path.join(subdir, file))

print(f"{round(beforeSize/1024, 2)}kB")

for subdir, dirs, files in walk(rootdir):
	for file in files:
		if file.endswith(".json"):
			print(f"\n{file}")
			print(f"Before: {round((path.getsize(path.join(subdir, file))/1024), 2)}kB")
			filepath = path.join(subdir, file)
			with open(filepath, "r") as jsonfile:
				data = load(jsonfile)
			for item in list(data):
				if item == "groups" or item == "credit":
					data.pop(item, None)
				elif item == "elements":
					x = 0
					for dictionary in data[item]:
						for item2 in list(dictionary):
							if item2 == "__comment":
								data[item][x].pop(item2, None)
						x += 1
			with open(filepath, "w") as outFile:
				outFile.write(dumps(data, separators=(',', ':')))
			print(f"After: {round((path.getsize(path.join(subdir, file))/1024), 2)}kB")

		elif file.endswith(".jem"):
			print(f"\n{file}")
			print(f"Before: {round((path.getsize(path.join(subdir, file))/1024), 2)}kB")
			filepath = path.join(subdir, file)
			with open(filepath, "r") as jsonfile:
				data = load(jsonfile)
			for item in list(data):
				if item not in ["texture", "textureSize", "shadowSize", "models"]:
					data.pop(item)
				elif item == "models":
					x = 0
					for dictionary in data[item]:
						if "boxes" in list(dictionary) or "submodels" in list(dictionary):
							pass
						else:
							for item2 in list(dictionary):
								if not item2 == "part":
									data[item][x].pop(item2, None)
						x += 1
			with open(filepath, "w") as outFile:
				outFile.write(dumps(data, separators=(',', ':')))
			print(f"After: {round((path.getsize(path.join(subdir, file))/1024), 2)}kB")

fileCount = 0
afterSize = 0
for subdir, dirs, files in walk(rootdir):
	for file in files:
		if file.endswith(".json") or file.endswith(".jem"):
			afterSize += path.getsize(path.join(subdir, file))
			fileCount += 1

input(f"\n-----\n\nCompressed {fileCount} files\nBefore: {round(beforeSize/1024, 2)}kB\nAfter: {round(afterSize/1024, 2)}kB")