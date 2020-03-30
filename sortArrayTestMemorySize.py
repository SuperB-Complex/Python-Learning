import json
import datetime
from operator import itemgetter

def readFile(file):
    result = []
    with open(file, 'r') as f:
        for row in f.readlines():
            map = dict(json.loads(row))
            result.append(map)
    return result

# start = datetime.datetime.now()
# data = readFile("jsonFile0.json") # 400MB
# result = sorted(data, key=itemgetter('year', 'school'))
# end = datetime.datetime.now()
# print((end - start)) # 0:00:11.760524

# start = datetime.datetime.now()
# data = readFile("jsonFile1.json") # 800MB
# result = sorted(data, key=itemgetter('year', 'school'))
# end = datetime.datetime.now() 
# print((end - start)) # 0:00:21.632255

# start = datetime.datetime.now()
# data = readFile("jsonFile2.json") # 1GB
# result = sorted(data, key=itemgetter('year', 'school'))
# end = datetime.datetime.now() 
# print((end - start)) # 0:00:56.776623

start = datetime.datetime.now()
data = readFile("jsonFile3.json") # 800MB
result = sorted(data, key=itemgetter('year', 'school'))
end = datetime.datetime.now() 
print((end - start))