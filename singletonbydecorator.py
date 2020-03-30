instances = {} # global variable
def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]     # update the global variable

def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)
    return onCall

@singleton        # Person = singleton(Person)
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
 
@singleton        # Spam = singleton(Spam)
class Spam:
    def __init__(self,val):
        self.attr = val
        
bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())
 
sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())
 
X = Spam(42)
Y = Spam(99)
