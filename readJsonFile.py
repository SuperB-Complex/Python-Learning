import json

# only works for one line one json object 
# with open('customised.json') as of:
#     data = json.load(of)
#     print(data)

# now I have a json file has multiplt json objects in one line, how to parse
info, result = "", []
with open("customised.txt", "r", encoding="utf-8") as f:
    for row in f.readline():
        info += row
array = info.split("}{")
array[0] += "}"
array[-1] = "{" + array[-1] 
for item in array[1:-1]:
    item = "{" + item + "}"
    item = json.loads(item)
    result.append(item['url'])
print(result)