class ShowFunName():
    def __init__(self, func):
        self._func = func
 
    def __call__(self, a):
        print('function name:', self._func.__name__)
        return self._func(a)
 
 
@ShowFunName
def Bar(a):
    return a
 
print(Bar('python'))
# function name: Bar
# python


class ShowClassName(object):
    def __init__(self, cls):
        self._cls = cls
 
    def __call__(self, a):
        print('class name:', self._cls.__name__)
        return self._cls(a)
 
 
@ShowClassName
class Foobar(object):
    def __init__(self, a):
        self.value = a
 
    def fun(self):
        print(self.value)
 
a = Foobar('python')
# class name: Foobar