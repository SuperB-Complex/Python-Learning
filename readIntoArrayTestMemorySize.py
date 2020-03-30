import json
import datetime

def readFile(file):
    result = []
    with open(file, 'r') as f:
        for row in f.readlines():
            map = dict(json.loads(row))
            result.append(map)
    return result
    
# start = datetime.datetime.now()
# readFile("jsonFile0.json") # 408MB
# end = datetime.datetime.now()
# print((end - start)) # 0:00:08.331888

# start = datetime.datetime.now()
# readFile("jsonFile1.json")
# end = datetime.datetime.now() # 1GB
# print((end - start)) # 0:00:17.360950

start = datetime.datetime.now()
readFile("jsonFile2.json") # 1GB 
end = datetime.datetime.now()
print((end - start))

# start = datetime.datetime.now()
# readFile("jsonFile3.json") # 2GB the memory kind of break down, starting from half used
# end = datetime.datetime.now()
# print((end - start)) # 0:00:50.056749 