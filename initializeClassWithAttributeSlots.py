class A():
    __slots__ = ['abc', 'bca', 'cab']

    def __init__(self, abc, bca, cab):
        self.abc = abc
        self.bca = bca
        self.cab = cab

a = A(1, 2, 3)