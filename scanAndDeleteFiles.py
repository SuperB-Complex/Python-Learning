import os

OPENFILE, CUSTOMIZEDFILE = "open.json", "customised.json"

path = os.getcwd()
for dirpath, dirnames, files in os.walk('.'):
    for name in files:
        if OPENFILE in name or CUSTOMIZEDFILE in name:
            os.remove(name)
