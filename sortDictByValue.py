import json

OPENFILE, CUSTOMIZED = "open.json", "customised.json"

def readFile(file):
    result = {}
    with open(file, 'r') as f:
        for row in f.readlines():
            entry = dict(json.loads(row))
            year = entry['year']
            result[entry['url']] = int(entry[str(year)])
    return result

o = readFile(OPENFILE)
print(sorted((v, k) for (k, v) in o.items()))