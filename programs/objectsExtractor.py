from tkinter.filedialog import askdirectory
from os import path, makedirs
from requests import get
from tkinter import Tk
from sys import exit

Tk().withdraw()

r = get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
versionManifest = r.json()

url = None
while url == None:
	try:
		version = input("Enter Minecraft Version: ")
		url = next(item for item in versionManifest["versions"] if item["id"] == version)
	except:
		print(f"{version} does not exist")

r = get(url["url"])
versionJson = r.json()

r = get(versionJson["assetIndex"]["url"])
data = r.json()

outputDir = askdirectory(title = "Select output folder")
if outputDir == "":
	exit(0)

for file in data["objects"]:
	directory = path.dirname(path.join(outputDir, file))
	if not path.exists(directory):
		makedirs(directory)

	r = get(f"https://resources.download.minecraft.net/{data['objects'][file]['hash'][:2]}/{data['objects'][file]['hash']}")
	open(path.join(outputDir, file), "wb").write(r.content)

	print(f"Saved {file}")