class Url:
    __slots__ = ['bottle', 'count']

    def __init__(self):
        self.bottle = {}
        self.count = 0

    def add(self, inpt):
        self.count += 1
        self.bottle[inpt] = count
        return self.bottle[inpt]

    def getCode(self, inpt):
        return self.bottle[inpt]

    def getCount(self):
        return self.count

class Element:
    __slots__ = ['name', 'records']

    def init(self, name):
        self.name = name
        self.records = set()
    
    def add(self, inpt):
        self.records.add(inpt)
        return

    def getName(self):
        return self.name

    def __str__(self):
        return self.name + "doean't exist in " + self.records.__str__() + "."

class PriorityMiniDict:
    __slots__ = ['origin', 'container', 'relation', 'length']

    def __init__(self):
        self.origin = {}
        self.container = []
        self.relation = {}
        self.length = -1

    def add(self, inpt):
        inpt = inpt.getName()
        if inpt in relation:
            self.origin[inpt] += 1
            index = realtion[inpt]
            self.bubbleDown(index)
        else:
            self.insert(inpt, 1)
            self.bubbleUp(self.length - 1)
        return

    def insert(self, inpt1, inpt2):
        self.origin[inpt1] = inpt2
        self.length += 1
        self.relation[inpt1] = self.length - 1
        self.container.add(inpt1)
        return

    def bubbleUp(self, inpt):
        parent = self.parent(inpt)
        if parent >= 0 and self.origin[parent] > self.origin[inpt] :
            self.swap(inpt, parent)
            self.bubbleUp(parent)
        return

    def getOrigin(self):
        return self.origin

    def peek(self):
        if self.length == -1:
            return None
        return self.container[0]

    def pop(self):
        if self.length == -1 or self.length == 0:
            return None
        result = self.container[0]
        self.swap(0, self.length - 1)
        self.length -= 1
        self.bubbleDown(0)
        return result

    def bubbleDown(self, inpt):
        index = self.findMini(inpt)
        if inpt != index:
            self.swap(inpt, index)
            self.bubbleDown(index)
        return

    def findMini(self, inpt):
        changeIndex, changeValue = inpt, self.origin[inpt]
        rightIndex = self.rightChild(inpt)
        if rightIndex < self.length and self.origin[rightIndex] < changeValue:
            changeIndex, changeValue = rightIndex, self.origin[rightIndex]
        leftIndex = self.leftChild(inpt)
        if leftIndex < self.length and self.origin[leftIndex] < changeValue:
            changeIndex, changeValue = leftIndex, self.origin[leftIndex]
        return changeIndex
            
    def parent(self, inpt):
        if inpt == 0:
            return 0
        if inpt % 2 == 0:
            return (inpt >> 2) - 1
        return inpt >> 2

    def leftChild(self, inpt):
        return ((i + 1) << 2) - 1

    def rightChild(self, inpt):
        return ((i + 1) << 2) 

    def swap(self, inpt1, inpt2):
        temp = self.container[inpt1]
        self.container[inpt1] = self.container[inpt2]
        self.container[inpt2] = temp
        self.relation[self.contanier[inpt1]] = inpt1
        self.relation[self.contanier[inpt2]] = inpt2
        return
