class HashTable:
    """
    self.slots列表用来存储键, self.data列表用来存储值.
    当我们通过键查找值时,键在 self.slots中的index即为值
    在 self.data中的index
    """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
 
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots)) #计算 hashvalue
      
        #如果 slots当前 hashvalue 位置上的值为None,则将新值插入
        if self.slots[hashvalue] == None: 
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # 如果 slots 当前 hashvalue 位置上的值为key,则用新值替代旧值
            if self.slots[hashvalue] == key: 
                self.data[hashvalue] = data  
            else: # 如果 slots 当前 hashvalue 位置上的值为其他值的话，则开始探测后面的位置
                nextslot = self.rehash(hashvalue,len(self.slots)) # 重新 rehash，实际相当于探测 hashvalue后一个位置
                # 如果后一个位置不为空，且不等于当前值即被其他值占用，则继续探测后一个
                while self.slots[nextslot] != None and self.slots[nextslot] != key: 
                    nextslot = self.rehash(nextslot,len(self.slots))
                    
                # 如果后一个值为空，则插入；为原来的值，则替换
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace
            
    
    """余数法计算 hashvalue"""
    def hashfunction(self,key,size): 
         return key%size
    
    """使用 +1 法来重新 rehash"""
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
 
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
 
        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and  not found and not stop:
            if self.slots[position] == key: #如果slots当前位置上的值等于 key,则找到了对应的 value
                found = True
                data = self.data[position]
            else: # 否则的话，rehash后继续搜寻下一个可能的位置
                position=self.rehash(position,len(self.slots))
            if position == startslot: # 如果最后又回到了第一次搜寻的位置，则要找的 key不在 slots中
                stop = True
        return data
 
    def __getitem__(self,key):
        return self.get(key)
 
    def __setitem__(self,key,data):
        self.put(key,data)




#!/usr/bin/python
# -*- coding: utf-8 -*-

num = 10


# 一个数据节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def data_equals(self, data):
        return self.data == data


class HashTable(object):
    def __init__(self):
        self.value = [None] * num

    def insert(self, data):
        if self.search(data):
            return True

        i = data % num
        node = Node(data)
        if self.value[i] is None:
            self.value[i] = node
            return True
        else:
            head = self.value[i]
            while head.get_next() is not None:
                head = head.get_next()
            head.set_next(node)
            return True

    def search(self, data):
        i = data % num
        if self.value[i] is None:
            return False
        else:
            head = self.value[i]
            while head and not head.data_equals(data):
                head = head.get_next()
            if head:
                return head
            else:
                return False

    def delete(self, data):
        if self.search(data):
            i = data % num
            if self.value[i].data_equals(data):
                self.value[i] = self.value[i].get_next()
            else:
                head = self.value[i]
                while not head.get_next().data_equals(data):
                    head = head.get_next()
                head.set_next(head.get_next().get_next())
            return True
        else:
            return False

    def echo(self):
        i = 0
        for head in self.value:
            print str(i) + ':\t',
            if head is None:
                print None,
            else:
                while head is not None:
                    print str(head.get_data()) + ' ->',
                    head = head.get_next()
                print None,
            print ''
            i += 1
        print ''


if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.insert(10)
    hashTable.insert(11)
    hashTable.insert(1)
    hashTable.echo()
    hashTable.delete(1)
    hashTable.echo()



#python3.6
from collections import namedtuple

class SimpleArray(object):
    #简单的数组类实现

    def __init__(self, mix):
        self.container = [None for i in range(mix)]

    def __len__(self):
        return len(self.container)

    def __setitem__(self, key, value):
        return self.container.__setitem__(key,value)

    def __getitem__(self, item):
        return self.container.__getitem__(item)

    def __delitem__(self, key):
        return self.container.__setitem__(key, None)

    def __str__(self):
        return str(self.container)


class SimpleDict(object):
    #简单的字典类实现

    Init_length = 8 # 初始化的大小
    Load_factor = 2/3 # 扩容因子

    def __init__(self):
        self._array_len = SimpleDict.Init_length
        self._array = SimpleArray(self._array_len)
        self._used = 0
        self.dictObj = namedtuple("dictObj","key value") # 这里其实可以用数组也可以的，namedtuple是为了让代码更可读

    def __getitem__(self, item):
        key = self._hash(item)
        dictObj = self._array[key]
        if dictObj is not None and dictObj.key == item:
            return dictObj.value
        else:
            for new_key in self._second_hash(key):
                if self._array[new_key] is not None and item == self._array[new_key].key:
                    return self._array[new_key].value

    def __setitem__(self, key, value):
        # 计算是否需要扩容
        if (self._used / self._array_len) > SimpleDict.Load_factor:
            self._new_array()

        #根据键的hash值来计算得出位置索引
        hash_key = self._hash(key)
        new_key = self._second_hash(hash_key)

        while True:
            if self._array[hash_key] is None or key == self._array[hash_key].key:
                break

            # 发生哈希碰撞根据二次探查函数得出下一个索引的位置
            hash_key = next(new_key)

            if abs(hash_key) >= self._array_len:
                self._new_array()
                hash_key = self._hash(key)


        # 找到空位将键值对象放入
        self._array[hash_key] = self.dictObj(key, value)
        self._used += 1

    def __delitem__(self, key):
        hash_key = self._hash(key)
        if key != self._array[hash_key].key:
            for new_key in self._second_hash(hash_key):
                if key == self._array[new_key].key:
                    hash_key = new_key

        self._array[hash_key] = None
        self._used -= 1

    def _hash(self, key):
        # 计算哈希值
        return hash(key) & (self._array_len-1)

    def _second_hash(self, hash_key):
        # 简单的二次探查函数实现
        count = 1
        for i in range(self._array_len):
            new_key = hash_key + count**2
            if abs(new_key) < self._array_len:
                yield new_key
    
            new_key = hash_key - count**2
            if abs(new_key) < self._array_len:
                yield new_key
    
            count += 1

    def _new_array(self):
        # 扩容
        old_array = self._array
        self._array_len = self._array_len * 2 # 扩容2倍大小
        self._array = SimpleArray(self._array_len)
        for i in range(len(old_array)):
            dictObj = old_array[i]
            if dictObj is not None:
                self[dictObj.key] = dictObj.value

    def __str__(self):
        result = ", ".join("%s:%s"%(obj.key, obj.value)
                           for obj in self._array
                           if obj is not None)
        return "{" + result + "}"



if __name__ == '__main__':
    d = SimpleDict()
    for i in range(20):
        d[str(i)] = i
    print(d)
    print(d["10"])
    del d["11"]
    print(d)