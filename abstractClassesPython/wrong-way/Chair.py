class Chair():
    def __init__(self):
    	print('Chair\'s __init__ is called')
    def get_size(self):
        raise NotImplementedError
chair = Chair()
# the code will not break until the abstact function is called
chair.get_size()

class BigChair(Chair):
	def __init__(self):
		super().__init__()
		print('BigChair\'s __init__ is called')
bigChair = BigChair()
"""
the following line will cause raising the error.
Chair's __init__ is called
Traceback (most recent call last):
  File "Chair.py", line 8, in <module>
    chair.get_size()
  File "Chair.py", line 5, in get_size
    raise NotImplementedError
NotImplementedError
"""
bigChair.get_size()