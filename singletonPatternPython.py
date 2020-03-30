class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


class MySingleton(Singleton):
    def foo(self):
        pass


a = MySingleton()
b = MySingleton()
print(str(a.__eq__(b))) # True


class ImprovedSingleton:
    __instance = None
    def __new__(cls, a1, a2, a3, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ImprovedSingleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


class MySingletonWithParameters(ImprovedSingleton):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


c = MySingletonWithParameters(1, 2, 3)
d = MySingletonWithParameters(4, 5, 6)
print(str(c.__eq__(d))) # True