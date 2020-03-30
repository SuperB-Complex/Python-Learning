import heapq

map = {'a':1,'b':11,'c':10,'d':-9,'e':-10}

class PriorityMiniDict:
    def __init__(self, inpt):
        self.origin = inpt
        self.container = list(inpt.keys())
        self.length = len(inpt)
        self.heapify()

    def heapify(self):
        for index in reversed(range(0, (self.length >> 1))):
            self.bubbleDown(index)
        return

    def peek(self):
        return self.container[0]

    def pop(self):
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
        return

    