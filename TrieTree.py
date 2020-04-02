class Node:

    def __init__(self, name, extra):
        self.name = name
        self.children = [None] * (26 + len(extra))
        self.end = False

    def setChild(self, inpt1, inpt2):
        self.children[inpt1] = inpt2
        return

    def getChildrens(self):
        return self.children

    def getChildren(self, inpt):
        return self.children

    def setName(self, inpt):
        self.name = inpt
        return 

    def getName(self):
        return self.name
    
    def setEnd(self, inpt):
        self.end = True

    def getEnd(self):
        return self.end


class Util:
    @classmethod
    def count(cls, inpt):
        result = set()
        if isinstance(input, list):
            cls.countList(inpt, result)
        elif isinstance(inpt, str):
            cls.countString(inpt, result)
        return cls.encode(result)

    @classmethod
    def countList(cls, inpt1, inpt2):
        for ele in inpt1:
            cls.conutString(ele, inpt2)
        return 
    
    @classmethod
    def countString(cls, inpt1, inpt2):
        for ele in inpt1:
            if not ele.isalpha():
                inpt2.add(ele)
        return 

    @classmethod
    def encode(cls, inpt):
        index, result = 0, {}
        for ele in inpt:
            if ele == '' or len(ele) == 0:
                continue
            result[ele] = index
            index += 1
        return result

    @classmethod
    def replace(cls, inpt):
        REPLACEDICT = {}
        for ele in inpt:
            if ele in REPLACEDICT:
                ele = REPLACEDICT[ele]
        return


class TrieTree:
    def __init__(self, data):
        self.extraName = Util.count(data)
        self.extraLength = len(self.extraName)
        self.root = self.initiate(data)

    def initiate(self, data1):
        node = Node('0', self.extraLength)
        temp = node
        for ele in data1:
            self.insert(temp, ele)
        return node

    def getPosition(self, data):
        result = data - 'a'
        if not data.isalpha():
            result = self.extraName[data]
        return result

    def insert(self, data1, data2):
        for ele in data2:
            pos = self.getPosition(ele)
            if data1.getChildren(pos) is None:
                data1.setChild(pos, Node(ele, self.extraLength))
            data1 = data1.data1.getChildren(pos)
        data1.setEnd(True)
        return

    def search(self, data): 
        node, result = self.root, []
        for ele in data:
            pos = self.getPosition(ele)
            nexts = node.getChildren(pos)
            if nexts is None:
                self.guess(node, data)
                break
            else:
                result.append(ele)
                node = nexts
        return ''.join(result)

    def guess(self, data1, data2):
        if data1.getEnd():
            data2.append(data1.getName())
            return
        for ele in data1.getChildrens():
            if ele is not None:
                data2.append(ele.getName())
                self.guess(ele, data2)
                break
        return
            