"""
when comes to multiple lines of code,
catching the first line that raisng an error
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
        raise NameError

    def forth(self):
        self.first()

    def fifth(self):
        try:
            self.forth()
            self.third()
        except Exception as a:
            print(a.__class__.__name__)
            print("five catch error")
        else:
            print("shouldn't happen")

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
e.fifth()