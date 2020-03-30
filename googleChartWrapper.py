from __future__ import division

# fine tuned
class DataTable(object):
    def __init__(self, description, querySet, p=None):        
        '''
        input:
        description includes name of columns and roles
        querySet is results of queries
        output:
        description: supposed to be formatted data, a string of a list
                     ex: 
                        nice format:
                        "cols:[{id:'',label:'Month',pattern:'',type:'string'},
                        {id:'',label:'Sales',pattern:'',type:'number'},
                        
                        {id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},
                        {id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},
                        {id:'',label:'Expenses',pattern:'',type:'number'}],"
        value: supposed to be formatted data, a string of a list
               ex: 
               nice format:
               "rows:[{c:[{v:'April',f:null},{v:1000,f:null},{v:900,f:null},{v:1100,f:null},{v:400,f:null}]},
               {c:[{v:'May',f:null},{v:1170,f:null},{v:1000,f:null},{v:1200,f:null},{v:460,f:null}]},
               {c:[{v:'June',f:null},{v:660,f:null},{v:550,f:null},{v:800,f:null},{v:1120,f:null}]},
               {c:[{v:'July',f:null},{v:1030,f:null},{v:null,f:null},{v:null,f:null},{v:540,f:null}]}],"
        '''
        self.description = descriptionToListString(description)
        self.value = querySetToListString(querySet, description)
        self.p = null
        if not p:
            self.p = p

    def descriptionToListString(self, description):
        '''
        description: 2-dimensional tuple
                     in each tuple, 1st element is name, 2nd element is type
                     ex: (('', 'task', '', 'string', false), ('', 'hours', '', 'number', true), ('', '', '', 'number', 'interval', 8), ('', '', '', 'number', 'interval', 8), ('', 'count', '', 'number'))
        '''
        value = ["cols:["]
        self.numberOfColumn = len(description)
        self.valueOfOption = {}
        targetLabel = ''
        
        self.flag = []
        for index, item in enmurate(description):
            self.flag.append(False)
            temp = ["{id:'", item[0], "',label:'", item[1], "',pattern:'", item[2], "',type:'", item[3], "'"]
            if item[4] == True:
                targetLabel = item[1]
            if 5 < len(item):
                tempp = [",p:{role:'", item[4], "'}"]
                temp.append(''.join(tempp))
                self.valueOfOption.update({index:item[5]})
                self.flag.append(True)
            temp.append("},")
            value.append("".join(temp))
        valueString = "".join(value)[:-1]
        valueString = valueString + "],"
        return valueString

    def querySetToListString(self, querySet, description):
        '''
        querySet: results of queries
        '''
        value = ["rows:["]
        for item in querySet.iterator():
            temp = ["{c:["]
            for index in range(0, self.numberOfColumn):
                temp.append("{v:'")
                if self.flag[index] == True:
                    temp.append(self.valueOfOption[index])
                    temp.append("',f:null},")
                    continue
                temp.append(item.description[index][1])
                temp.append("',f:null},")
            tempString = "".join(temp)[:-1]
            value.append(tempString)
            value.append("]},")
        valueString = "".join(value)[:-1]
        valueString.join("],")
        return valueString

    def dataTableJsonString():
        value = ["{"]
        value.append(self.description)
        value.append(self.value)
        value.append(self.p)
        value.append("}")
        return "".join(value)

"""
class Dataview(object):
    def __init__(self, dataTable=None, columns=None, rows=None):
        '''
        dataTable: instance of class DataView
        columns: a dictionary of necessary properties
        rows: a dictionary of necessary properties 
        '''
        self.dataTable = dataTable
"""

class Option(object):
    options = ''

    @classmethod cls, 
    def dictionaryToString(cls, m):
        return ','.join('{!s}={!r}'.format(k, v) for (k, v) in m.items())

    @classmethod
    def pieChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of pie chart
        ex:
        {legend: 'none',pieSliceText: 'none',
        pieStartAngle: 135,
        tooltip: { trigger: 'none' },
        slices: {
            0: { color: 'yellow' },
            1: { color: 'transparent' }
        }}
        '''
        #return cls()
        return dictionaryToString(options, '')

    @classmethod
    def columnChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of column chart
        '''
        #return cls()
        return dictionaryToString(options, '')

    @classmethod
    def scatterChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of scatter chart
        '''
        #return cls()
        return dictionaryToString(options, '')

class JScode(object):
    def __init__(self, package, callBackMethod, chartType, elementId, dataTable, option, dataView=None):
        '''
        package: which package you are going to load
        callBackMethod: the name of callBackMethod
        chartType: the type of chart
        elementId: the id of a specific element
        dataTable: an instance of class DataTable
        dataView: an instance of class DataView
        option: an instance of class Option
        '''
        self.package = package
        self.callBackMethod = callBackMethod
        self.chartType = chartType
        self.elementId = elementId
        self.dataTable = dataTable
        self.option = option
        if not dataView:
            self.dataView = dataView
    
    def jsCodeGenerate(self):
        script = '''<script type="text/javascript">google.charts.load("current", {packages:['corechar{package}']});
                    google.charts.setOnLoadCallback({callBackMethod});
                    function {callBackMethod}() {var json_data = new google.visualization.DataTable(google.visualization.{chartType}}(document.getElementById('{elementId}')), {option});
                                                 json_table.draw({dataTable}, {option});}</script>'''
        html =   '''<div id="{elementId}"></div>'''
        return 
    
        

