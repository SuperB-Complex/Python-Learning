import json 
import heapq
import struct
import sys
import abc
# from test import CollectData, Util

OPENFILE, CUSTOMIZEDFILE, DB = "open.json", "customised.json", "db_"

class Reader(abc.ABC):
    def __init__(self, years, urls):
        self.years = years
        self.urls = urls

    def readAll(self):
        result = {}
        result['open'] = self.readOpenAll()
        result['cutomized'] = self.readCustomizedAll()
        return result

    def readOpenAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readOpenByYear(year)
        return result

    def readCustomizedAll(self):
        result = {}
        for year in self.years:
            result[year] = self.readCustomizedByYear(year)
        return result

    def readOpenByYear(self, year):
        return self.readFile(year+ '_' + OPENFILE)

    def readCustomizedByYear(self, year):
        return self.readFile(year+ '_' + CUSTOMIZEDFILE)

    @abc.abstractmethod
    def readFile(self, filiename):
        pass

    def divide(self, filiename):
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                suffix = OPENFILE
                if 'customised' in entry['url']:
                    suffix = CUSTOMIZEDFILE
                name = DB + entry['year'] + '_' + suffix
                with open(name, 'a') as w:
                    w.write(row)
                    w.write('\n')
        return

    def readUrlFromSingleJsonSource(self, filiename):
        result = set()
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                result.add(entry['url'])
        return result


class OriginalReader(Reader):
    def __init__(self, years, urls):
        super().__init__(years, urls)

    def readFile(self, filiename):
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


class TransUrlReader(OriginalReader):
    def __init__(self, year, urls):
        super().__init__(year, urls)

    def readFile(self, filiename):
        result = {'url':[], 'cols':[], 'rows':[]}
        with open(filiename, 'r') as f:
            for row in f.readlines():
                entry = dict(json.loads(row))
                result['url'].append(self.urls[entry['url']])
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


years = ['2010','2018','2019','2016','2014','2008','2011','2013','2012','2009','2007','2015','2017']
def readOneLine(name):
    result = []
    with open(name, 'r') as f:
            for row in f.readlines():
                result.append(row)
    return result[0]
def parseToList(data):
    array = data.split("','")
    array[0] = array[0][2:]
    array[-1] = array[-1][:-2]
    return array
def findYear(inpt):
    for indxe in reversed(range(0, len(inpt))):
        if inpt[indxe:indxe + 1].isdigit() and indxe >= indxe - 3:
            return inpt[indxe - 3 : indxe + 1]
def categoryByTypeYear(urls, years):
    result = {'o':{}, 'c':{}}    
    for url in urls:
        year = findYear(url)
        if 'open' in url:
            if year not in result['o']:
                result['o'][year] = []
            result['o'][year].append(url)
        elif 'customised' in url:
            if year not in result['c']:
                result['c'][year] = []
            result['c'][year].append(url)
    return result
urls = categoryByTypeYear(parseToList(readOneLine("urls.txt")), years)
print()
# CollectData.initiate()
# urls = Util().getTotalUrls()
# years = Util().getTotalYears()

o = OriginalReader(years, urls)
t = TransUrlReader(years, urls)
print(o.readAll())
# print(t.readAll()) # lack of parameters