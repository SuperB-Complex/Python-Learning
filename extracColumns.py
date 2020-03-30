import json

OPENFILE, CUSTOMIZED = "open.json", "customised.json"

def readFile(file):
    result, dup = [], set()
    with open(file, 'r') as f:
        for row in f.readlines():
            # print(row)
            # print(type(row))
            maps = dict(json.loads(row))
            # print(maps)
            # print(type(maps))
            for key,discard in maps.items():
                if exist(result, key) == False:
                    result.append(key)
                else:
                    dup.add(key)
    return result, dup

def exist(keyList, key):    
    for item in keyList:
        if key == item:
            return True
    return False

def compare(input1, input2):
    result = []
    for item in input2:
        if exist(input1, item) == False:
            result.append(item)
    return result

def show(data):
    for item in data:
        print(item)

openized, openizedDup = readFile(OPENFILE)
customized, customizedDup = readFile(CUSTOMIZED)
openSubt = compare(openized, openizedDup)
customizedSubt = compare(customized, customizedDup)
# show(openized)
# print("-----------------------------")
# show(openizedDup)
# print("-----------------------------------------------")
# show(customized)
# print("-----------------------------")
# show(customizedDup)
# print("-----------------------------------------------")
# show(openSubt)
# print("-----------------------------")
# show(customizedSubt)

"""
open:
{'rankin2009':'2019', }
"""