from tkinter.filedialog import askopenfilename
from json import load, dumps, loads
from os import getenv, path
from zipfile import ZipFile
from tkinter import Tk
Tk().withdraw()
file = ""
while file == "":
	file = askopenfilename(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Language File", filetypes = [('LANG', '*.json')])
while True:
	try:
		version = input("Minecraft Version: ")
		with ZipFile(f"{getenv('APPDATA')}/.minecraft/versions/{version}/{version}.jar", "r") as zip_ref:
				head, tail = path.split(file)
				try:
					langFile = zip_ref.read(f"assets/minecraft/lang/{tail}")
					vanilla = langFile.decode("utf-8")
					vanillaJSON = loads(vanilla)
				except:
					input("I couldn't find that language in your JAR file\nPress ENTER to select a custom one")
					vanillaFile = ""
					while vanillaFile == "":
						vanillaFile = askopenfilename(initialdir = f"{getenv('APPDATA')}/.minecraft/resourcepacks", title = "Select Language File", filetypes = [('LANG', '*.json')])
					with open(vanillaFile) as json_file:
						vanillaJSON = load(json_file)
				with open(file) as json_file:
					customJSON = load(json_file)
				new = {}
				for lang in customJSON:
					try:
						if vanillaJSON[lang] == customJSON[lang]:
							print(f"Removed {lang}")
						else:
							print(f"Kept {lang}")
							new[lang] = customJSON[lang]
					except:
						pass
				with open(file, "w") as outFile:
					outFile.write(dumps(new, indent = 2))
				input("Press ENTER to quit")
				break
	except:
		print("Please install that version first")