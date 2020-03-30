""">>> ss = "PYTHON3"
>>> s = iter(ss)
>>> for S in s:
...     print(S)
... 
P
Y
T
H
O
N
3"""


""">>> while next(s) is not None:
...     print(next(s))
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration"""


""">>> while True:
...     try:
...         print(next(s))
...     except StopIteration:
...         print("stop now")
...         break
... 
P
Y
T
H
O
N
3
stop now"""


class IT_SQUARE:
    def __init__(self, x):
        self.x = x

    def __next__(self):
        self.x = self.x ** 2
        if self.x > 9999999999999:
            raise StopIteration
        
        else:
            return self.x

    def __iter__(self):
        return self
 
IT1 = IT_SQUARE(2)
 
while True:
    try:
        print(IT1.__next__())
    except StopIteration:
        break
