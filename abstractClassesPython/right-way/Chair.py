import abc 
class Chair(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def load(self, input):
        return
    @abc.abstractmethod
    def save(self, output, data):
        return
 
class BigChair(Chair):
    def load(self, input):
        return input
    def save(self, output, data):
        return output
 
class ColorChair(Chair):
    def load(self, input):
        return input
    def save(self, output, data):
        return output
 
if __name__ == '__main__':
    print(issubclass(BigChair, Chair))     # print True
    print(isinstance(BigChair(), Chair))   # print True
    print(issubclass(ColorChair, Chair))     # print True
    print(isinstance(ColorChair(), Chair))   # print True