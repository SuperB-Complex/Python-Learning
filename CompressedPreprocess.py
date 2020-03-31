import json 
import heapq
import struct
import sys

OPENFILE, CUSTOMIZEDFILE = "open.json", "customised.json"


'''
the compression is based on Huffman encode.
However, the size of the files showing no differences between you are using huffman to encode and you are using the original string.
And with some validation, showing in another file named 'size differences in chr()ascii()bytearray() in python'
'''

class Node:
    __slots__ = ['name', 'count', 'left', 'right']

    def __init__(self, name, count, left=None, right=None):
        self.name = name
        self.count = count
        self.left = left
        self.right = right
    
    def getCount(self):
        return self.count

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getName(self):
        return self.name

    def __lt__(self, other):
        return self.getCount() < other.getCount()

    def __repr__(self):
        return self.name + ' ' + str(self.count) + ' ' + str(self.left) + ' ' + str(self.right)


class Compression:
    __slots__ = ['frequency', 'root', 'code', 'codeInByteArrayFormat', 'sizeOfOrigin', 'sizeOfCompression', 'sizeOfCompressionBinaryFormat']

    def __init__(self, data):
        self.root = self.up(list(self.sort(self.count(data))))
        self.code = self.encode()
        self.codeInByteArrayFormat = self.encodeInByteArrayFormat()
        self.sizeOfOrigin = []
        self.sizeOfCompression = []
        self.sizeOfCompressionBinaryFormat = bytearray()

    def getRoot(self):
        return self.root

    def getCodeInByteArrayFormat(self):
        return self.codeInByteArrayFormat

    def getCode(self):
        return self.code

    def getSizeOfOrigin(self):
        return self.sizeOfOrigin

    def getSizeOfCompression(self):
        return self.sizeOfCompression

    def getSizeOfCompressionBinaryFormat(self):
        return self.sizeOfCompressionBinaryFormat

    def count(self, data):
        result = {}
        for ele in data:
            for e in ele:
                if e not in result:
                    result[e] = 0
                result[e] += 1
        return result
    
    def sort(self, data):
        return (Node(k, v) for (k, v) in data.items())

    def up(self, data):
        while len(data) != 0:
            childLeft = heapq.heappop(data)
            if len(data) == 0:
                self.root = childLeft
                break
            childRight = heapq.heappop(data)
            heapq.heappush(data, Node('', childLeft.getCount() + childRight.getCount(), childLeft, childRight))
        return self.root

    def encodeEnhanced(self, data):
        result = []
        for ele in data:
            self.sizeOfOrigin.append(ele)
            result.append(self.code[ele])
        return ''.join(result)

    def encodeEnhancedInByteArrayFormat(self, data):
        result = bytearray()
        for ele in data:
            result.extend(self.codeInByteArrayFormat[ele])
        print()
        return result

    def encodeInByteArrayFormat(self):
        self.codeInByteArrayFormat = {}
        self.helperInByteArrayFormat(self.root, [])
        return self.codeInByteArrayFormat

    def helperInByteArrayFormat(self, entry, stringBuilder):
        if entry.getLeft() is None and entry.getRight() is None:
            self.codeInByteArrayFormat[entry.getName()] = bytearray(stringBuilder)
            print(sys.getsizeof(stringBuilder))
            # self.sizeOfCompressionBinaryFormat.append(sys.getsizeof(stringBuilder))
            return
        stringBuilder.append(0)
        self.helperInByteArrayFormat(entry.getLeft(), stringBuilder)
        stringBuilder.pop(-1)

        stringBuilder.append(1)
        self.helperInByteArrayFormat(entry.getRight(), stringBuilder)
        stringBuilder.pop(-1)
        return    

    def encode(self):
        self.code = {}
        self.helper(self.root, [])
        return self.code

    def helper(self, entry, stringBuilder):
        if entry.getLeft() is None and entry.getRight() is None:
            self.code[entry.getName()] = ''.join(stringBuilder)
            print(sys.getsizeof(''.join(stringBuilder)))
            # self.sizeOfCompression.append(sys.getsizeof(''.join(stringBuilder)))
            return
        stringBuilder.append('0')
        self.helper(entry.getLeft(), stringBuilder)
        stringBuilder.pop(-1)

        stringBuilder.append('1')
        self.helper(entry.getRight(), stringBuilder)
        stringBuilder.pop(-1)
        return

    def decode(self, data):
        result = []
        start = self.root
        for ele in data:
            if start.getLeft() is None and start.getRight() is None:
                result.append(start.getName())
                start = self.root
                continue
            if ele == '1':
                start = start.getLeft()
            else:
                start = start.getRight()
        return ''.join(result)


class Preprocess:
    def __init__(self, years, urls):
        self.years = years
        self.urlsCompressedInstance = Compression(urls)

    def readAllOrigined(self):
        result = {}
        result['open'] = self.readOpenOriginedAll()
        result['cutomized'] = self.readCustomizedOriginedAll()
        return result

    def readOpenOriginedAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readOpenOriginedByYear(year)
        return result

    def readCustomizedOriginedAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readCustomizedOriginedByYear(year)
        return result

    def readOpenOriginedByYear(self, year):
        return self.readOriginedFile(year+ '_' + OPENFILE)

    def readCustomizedOriginedByYear(self, year):
        return self.readOriginedFile(year+ '_' + CUSTOMIZEDFILE)

    def readOriginedFile(self, filiename):
        result = {'url':[], 'cols':[], 'rows':[]}
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                result['url'].append(entry['url'])
                count = 2
                transt = []
                for discard,value in entry.items():
                    if count > 0 and isinstance(value, list):
                        count -= 1
                        for e in value:
                            transt.append(e)
                result['cols'].append(transt)
                transts = []
                for ele in transt:
                    transts.append(entry[ele])
                result['rows'].append(transts)
        return result

    def readAllCompressed(self):
        result = {}
        result['open'] = self.readOpenCompressedAll()
        result['cutomized'] = self.readCustomizedCompressedAll()
        return result

    def readOpenCompressedAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readOpenCompressedByYear(year)
        return result

    def readCustomizedCompressedAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readCustomizedCompressedByYear(year)
        return result

    def readOpenCompressedByYear(self, year):
        return self.readCompressedFile(year+ '_' + OPENFILE)

    def readCustomizedCompressedByYear(self, year):
        return self.readCompressedFile(year+ '_' + CUSTOMIZEDFILE)

    def readCompressedFile(self, filiename):
        result = {'url':[], 'cols':[], 'rows':[]}
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                result['url'].append(self.urlsCompressedInstance.encodeEnhanced(entry['url']))
                count = 2
                transt = []
                for discard,value in entry.items():
                    if count > 0 and isinstance(value, list):
                        count -= 1
                        for e in value:
                            transt.append(e)
                result['cols'].append(transt)
                transts = []
                for ele in transt:
                    transts.append(entry[ele])
                result['rows'].append(transts)
        return result

    def readAllCompressedInByteArrayFormat(self):
        result = {}
        result['open'] = self.readOpenCompressedAllInByteArrayFormat()
        result['cutomized'] = self.readCustomizedCompressedAllInByteArrayFormat()
        return result

    def readOpenCompressedAllInByteArrayFormat(self):
        result = {}
        for year in self.years:
            result[year] = self.readOpenCompressedByYearInByteArrayFormat(year)
        return result

    def readCustomizedCompressedAllInByteArrayFormat(self):
        result = {}
        for year in self.years:
            result[year] = self.readCustomizedCompressedByYearInByteArrayFormat(year)
        return result

    def readOpenCompressedByYearInByteArrayFormat(self, year):
        return self.readCompressedFileInByteArrayFormat(year+ '_' + OPENFILE)

    def readCustomizedCompressedByYearInByteArrayFormat(self, year):
        return self.readCompressedFileInByteArrayFormat(year+ '_' + CUSTOMIZEDFILE)

    def readCompressedFileInByteArrayFormat(self, filiename):
        result = {'url':[], 'cols':[], 'rows':[]}
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                result['url'].append(self.urlsCompressedInstance.encodeEnhancedInByteArrayFormat(entry['url']))
                count = 2
                transt = []
                for discard,value in entry.items():
                    if count > 0 and isinstance(value, list):
                        count -= 1
                        for e in value:
                            transt.append(e)
                result['cols'].append(transt)
                transts = []
                for ele in transt:
                    transts.append(entry[ele])
                result['rows'].append(transts)
        return result

def writeBinary(name, data):
    with open(name, 'wb') as r:
        keys = data.keys()
        for key in keys:
            kk = data[key].keys()
            for k in kk:
                for e in data[key][k]['url']:
                    r.write(e)
    return
def writeUrl(name, data):
    with open(name, 'w') as r:
        keys = data.keys()
        for key in keys:
            kk = data[key].keys()
            for k in kk:
                for e in data[key][k]['url']:
                    r.write(e)
                    # r.writelines(struct.pack(e)) # struct.error: total struct size too long
    return
def write(name, data):
    with open(name, 'w') as r:
        return r.write(str(data))
def read(name):
    with open(name, 'r') as r:
        return r.readline()
def trunc(data):
    data = data.replace("'", '')
    arr = data.split(',')
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    return arr
urls = trunc(read("urls.txt"))
years = trunc(read("years.txt"))
# print(urls)
# print(years)
p = Preprocess(years, urls)
# write("writeCompressed.txt", p.readAllCompressed())
# write("writeOriginal.txt", p.readAllOrigined())
writeUrl("writeCompressed.txt", p.readAllCompressed())
writeUrl("writeOriginal.txt", p.readAllOrigined())
writeBinary("writeCompressedInBinartArrayFormat.txt", p.readAllCompressedInByteArrayFormat())
# print(p.urlsCompressedInstance.getSizeOfOrigin())
# print(p.urlsCompressedInstance.getSizeOfCompression())
# print(p.urlsCompressedInstance.getSizeOfCompressionBinaryFormat())