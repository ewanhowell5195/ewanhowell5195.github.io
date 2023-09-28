from json import load, dumps
from requests import get
from random import choice

with open("site.json") as file:
	data = load(file)

for page in data:
	for category in data[page]:
		for pack in category["packs"]:
			if "buttons" in pack["details"]:
				for button in pack["details"]["buttons"]:
					if not "mirrorless" in button or not button["mirrorless"]:
						if not "mirror" in button:
							button["mirror"] = button["link"]
						print(f"Generating {button['mirror']}")
						button["link"] = get(f"http://adfoc.us/api/?key=fc50038c0973a84e3c8dd40b5f1d5dec&url={button['mirror']}").content.decode()
						button["type"] = "download"
			if "extras" in pack["details"]:
				for button in pack["details"]["extras"]:
					if not "local" in button or ("local" in button and not button["local"]):
						if not "mirrorless" in button or not button["mirrorless"]:
							if not "mirror" in button:
								button["mirror"] = button["link"]
							print(f"Generating {button['mirror']}")
							button["link"] = get(f"http://adfoc.us/api/?key=fc50038c0973a84e3c8dd40b5f1d5dec&url={button['mirror']}").content.decode()
							button["type"] = "download"

with open("site.json", "w") as file:
	file.write(dumps(data, indent = "\t"))