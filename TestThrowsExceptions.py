import unittest
from Exceptions import *

class TestThrowsExceptions(unittest.TestCase):
    def testThrowsExceptions(self):
        e = Run()
        self.assertRaises(NotExistException, e.throwExceptions())