from collections import OrderedDict

FILE = "packagesDependentRelationship.txt"


class Node():
    def __init__(self, package, version):
        self.atom = Atom(package, version)
        self.next = []

    def appendNext(self, input):
        self.next.append(input)
        return

    def getAtom(self):
        return self.atom

    def getNext(self):
        return self.next

    def __str__(self):
        if len(self.next) == 0:
            return "<%s>" % (self.atom)   
        else:
            strinBuilder = "["
            for item in self.next:
                sub = item.getAtom()
                strinBuilder += str(sub)
                strinBuilder += ";"
            strinBuilder += "]"
            return "<%s, %s>" % (self.atom, strinBuilder)

    def __eq__(self, object):
        condition1 = isinstance(object, Node)
        condition2 = (object.atom.__eq__(self.atom))
        condition3 = True
        lengthSelf, lengthObject = len(self.next), len(object.next)
        if lengthSelf != lengthObject:
            condition3 = False
        else:
            for index in range(0, lenngthSelf):
                if self.next[index].__eq__(object.next[index]) == False:
                    condition3 = False
                    break
                else:
                    continue
        return condition1 and condition2 and condition3

class Atom():
    def __init__(self, package, version):
        self.name = package
        self.version = version

    def __str__(self):
        return "(%s, %s)" % (self.name, self.version)

    def __eq__(self, object):
        condition1 = isinstance(object, Atom)
        condition2 = (object.name.strip() == self.name.strip())
        condition3 = (object.version.strip() == self.version.strip())
        return condition1 and condition2 and condition3


class DependenceGraph():
    def __init__(self):
        self.graph = self.buildGraph()

    def presentGraph(self):
        print(type(self.graph))
        for key, value in self.graph.items():
            print(str(value))
        return

    def buildGraph(self):
        nodes = self.initilizeNodes()
        return nodes

    def initilizeNodes(self):
        result, parentRecord, currentTopElement = {}, OrderedDict(), " "
        with open(FILE, 'r', encoding="utf-8") as of:
            for row in of.readlines():
                row = row.rstrip()
                if self.isTopElement(row) == True:
                    name, version = self.parseTopElement(row)
                    parentRecord = {}
                    parentRecord[name] = 0
                    currentTopElement = name
                    if name not in result:
                        result[name] = Node(name, version)
                    continue
                else:
                    name, version, count = self.parseAndCountSubElement(row)
                    newNode = result.get(name)
                    if newNode is None:
                        newNode = Node(name, version)
                    result[name] = newNode
                    lastName, lastCount = parentRecord.popitem()
                    if count > lastCount and lastCount == 0:
                        parentRecord[lastName] = lastCount
                    elif count > lastCount and lastCount > 0:
                        parentRecord[lastName] = lastCount
                        currentTopElement = lastName
                    elif count == lastCount:
                        pass
                    elif count < lastCount:
                        number = lastCount - count
                        for index in range(0, number + 1):
                            lastName, lastCount = parentRecord.popitem()
                        parentRecord[lastName] = lastCount
                        currentTopElement = lastName
                    parentRecord[name] = count
                    if self.checkDuplicated(newNode, result[currentTopElement]) == False:
                        newNode.appendNext(result[currentTopElement]) # str(result[currentTopElement]) result[currentTopElement] currentTopElement
        return result

    def checkDuplicated(self, source, target):
        nextList = source.getNext()
        for item in nextList:
            if item.__eq__(target) == False:
                continue
            elif item.__eq__(target) == True:
                return True
        return False

    def isTopElement(self, input):
        if "[" in input:
            return False
        else:
            return True

    def parseTopElement(self, input):
        array = input.split("==")
        return array[0], array[1]

    def parseSubElement(self, input):
        input = input.strip()
        array = input.split(" ")
        return array[1], array[-1][:-1]

    def parseAndCountSubElement(self, input):
        count, length = 0, len(input)
        for index in range(0, length):
            if input[index] == " ":
                continue
            else:
                count = index
                break
        input = input.strip()
        array = input.split(" ")
        return array[1], array[-1][:-1], int(count / 2)

DependenceGraph().presentGraph()
