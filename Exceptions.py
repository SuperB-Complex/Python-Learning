class NotExistException(Exception):

    """The not exist exception."""
    def ___init__(self):
        self.errorMessage = "Wrong : the element is not existed!"

    def __str__():
        return repr(self.errorMessage)

class Run(object):
    def __init__(self):
        pass
    def throwExceptions(self):
        raise NotExistException