"""
test file for module googleChartWrapper
"""
'''
haven't handle exceptions
'''

from googleChartWrapper import DataTable
from googleChartWrapper import Option
from googleChartWrapper import JScode
import unittest
try:
    import json
except ImportError:
    import simplejson as json

class DataTableTest(unittest.TestCase):
    def setUp(self):
        inputTuple = (('', 'task', '', 'string'), ('', 'hours', '', 'number'), ('', '', '', 'number', 'interval'), ('', '', '', 'number', 'interval'), ('', 'count', '', 'number'))
        rightOutput = "cols:[{id:'',label:'task',pattern:'',type:'string'},{id:'',label:'hours',pattern:'',type:'number'},{id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},{id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},{id:'',label:'count',pattern:'',type:'number'}],"
        
        self.dataTable = DataTable(inputTuple)

    def testDescriptionToListString(self):
        self.assertEqual(rightOutput, DataTable.descriptionToListString(inputTuple))


if __name__ == "__main__":
  unittest.main()