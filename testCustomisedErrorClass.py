class FatalError(Exception):
    message = ""

    @classmethod
    def error(cls, message):
        cls.message = message

def inner():
    try:
        out()
    except FatalError as error:
        print(FatalError.message)
        er = "error from functiono inner()"
        FatalError.message += er
        raise FatalError
    else:
        print("nothing happened")

def out():
    try:
        outer()
    except FatalError as error:
        print(FatalError.message)
        er = "error from function out()"
        FatalError.message += er
        raise FatalError
    else:
        print("nothing happened")

def outer():
    er = "error from function outer()"
    FatalError.message = er
    raise FatalError

try:
    inner()
except FatalError as error:
    print(error.message)
"""
error from function outer()
error from function outer()error from function out()
error from function outer()error from function out()error from functiono inner()
"""