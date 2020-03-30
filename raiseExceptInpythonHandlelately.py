"""
the exception will be throwed to the outer caller if you didn't catch it.
"""


class E:
    def first(self):
        raise ValueError

    def second(self):
        try:
            self.first()
        except:
            print("catch error")
        else:
            print("unlikly to appear")

    def third(self):
        self.first()

    def forth(self):
        self.third()

    def fifth(self):
        self.forth()

    def sixth(self):
        self.forth()

    def seventh(self):
        try:
            self.sixth()
        except ValueError:
            print("seven catch error")
        else:
            print("unlikly to appear")


e = E()
e.seventh()