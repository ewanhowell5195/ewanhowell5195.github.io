import os, sys, zipfile

version = input("Minecraft Version: ")

try:
    vanilla=zipfile.ZipFile(f"{os.getenv('APPDATA')}/.minecraft/versions/{version}/{version}.jar")
    packdir = os.path.dirname(os.path.realpath(__file__))
    
    missing = 0
    total = 0
    
    for file in sorted(vanilla.namelist()):
        if not file.endswith(".png"):
            continue
        if "font" in file:
            continue
        total = total + 1
        if os.path.exists(os.path.join(packdir, file)):
            continue
        print(file)
        missing = missing + 1
    print(f"""
------------------

Missing: {missing}
         {round(missing/total*100,2)}%""")
    
except:
    print("Doesn't exist or isn't installed")

input()
