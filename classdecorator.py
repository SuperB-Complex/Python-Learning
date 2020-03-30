import time
import functools


class DelayFunc(object):
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)

def delay(duration):
    """
    a decorator which delays a function 
    also provide a method to execute without delay
    """
    return functools.partial(DelayFunc, duration)

@delay(3)
def runningMethod():
    print("the normal running")

runningMethod()
# Wait for 3 seconds...
# the normal running

runningMethod.eager_call()
# Call without delay
# the normal running


class logging(object):
    def __init__(self, level='INFO'):
        self.level = level
        
    def __call__(self, func): 
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper 

@logging(level='INFO')
def say(something):
    print("logging {}!".format(something))

say("I love you!")
# [INFO]: enter function say()
# logging I love you!!