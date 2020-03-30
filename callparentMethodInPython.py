class Parent:
    def heir(self, selection):
        print("this is parent class")
        if selection == 0:
            print("parent select number 0")
        elif selection == 1:
            print("parent select number 1")
        elif selection == 2:
            print("parent select number 2")
        elif selection == 3:
            print("parent select number 3")
        


class childOne(Parent):
    def heir(self, selection):
        print("this is child 1 class")
        if selection == 0:
            super().heir(0)
            super().heir(1)
            super().heir(2)
        elif selection == 1:
            super().heir(3)
            super().heir(2)
            super().heir(1)


class childTwo(Parent):
    def heir(self, selection):
        print("this is child 2 class")
        if selection == 0:
            super().heir(3)
        elif selection == 1:
            super().heir(2)


class Assemble:
    def __init__(self, instance=Parent()):
        self.instance = instance

    def test(self, selection):
        self.instance.heir(selection)

c1 = childOne()
c2 = childTwo()
a1 = Assemble(c1)
a1.test(1)
a2 = Assemble(c2)
a2.test(1)
