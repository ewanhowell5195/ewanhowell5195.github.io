from tkinter.filedialog import askdirectory
from os import path, makedirs, getenv
from requests import get
from tkinter import Tk
from json import load
from sys import exit
from shutil import copy

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

mcDirectory = path.join(getenv("APPDATA"), ".minecraft")

outputDir = askdirectory(title = "Select output folder")
if outputDir == "":
	exit(0)

with open(path.join(mcDirectory, "assets", "indexes", version + ".json")) as jsonFile:
	data = load(jsonFile)

for item in data["objects"]:
	assetPath = path.join(outputDir, item)
	assetDir = path.dirname(assetPath)
	if not path.isdir(assetDir):
		makedirs(assetDir)
	copy(path.join(mcDirectory, "assets", "objects", data["objects"][item]["hash"][:2], data["objects"][item]["hash"]), assetPath)
	print(f"Copied {item}")