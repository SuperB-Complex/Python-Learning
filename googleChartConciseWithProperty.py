# from Constants import *

from .Constants import *
from abc import abstractmethod

# user entry class
# ideal input(must make sure col corresponds to row):
"""
{
'column'(About column, if you didn't keep the order of your column and your order of your field of your QuerySet, you must keep 'id' is identical to the name of your field of your QuerySet.):
	[{'id':'myid','label':'mylabel','pattern':'mypattern','type':'mytype'},
	{'id':'myid1','label':'mylabel1','pattern':'mypattern1','type':'mytype1','role':'myrole1'},
	{...}],
'rows'(About 'format', if you didn't use 'FUNCTIONFORMAT', please make sure you are aware of the rules of each format privided by Google Chart.
                if you are not much awared of the rules, please use 'FUNCTIONFORMAT', to be detailed description please refer to https://developers.google.com/chart/interactive/docs/reference#formatters_1
                if considering the efficiency, recommending not use 'FUNCTIONFORMAT'. The performance difference will be obvious when it comes to 1000+ rows of data.):
	{'format':[{'type':FORMATTYPE,'cparameter':{,,,},'func':[NAMEOFFUNCTION:(,,,),'cols':[,,,],...]},
               {'type':FORMATTYPE,'cparameter':{,,,},'func':[NAMEOFFUNCTION:(,,,),'cols':[,,,],...]}]},
	'row'(type is QuerySet):[{'a':'myA'},{'b':'myB'},{'c':'myC'},{'d':'myD},{'e':'myE'},...],
	'roleValue'(a value suffix with three '_' means set this column with this value;store by rows;):[['value___'],['r1v1', 'r2v2', 'r3v3',...],[...],...]},
'option':{'legend': 'none', 'pieSliceText': 'none', 'pieStartAngle': 135, 'tooltip': { 'trigger': 'none' }, 'slices': {0: { 'color': 'yellow' }, 1: { 'color': 'transparent' }}},
"package":"...", 
"callBackMethod":"...", 
"chartType":"..., 
"elementId":"...", 
"functionFormatted":"..."
};
"""
# the most concise input:
"""
{
'column'(About column, if you didn't keep the order of your column and your order of your field of your QuerySet, you must keep 'id' is identical to the name of your field of your QuerySet.):
	[{'id':'myid','label':'mylabel','pattern':'mypattern','type':'mytype'},
	{...}],
'rows'(About 'format', if you didn't use 'FUNCTIONFORMAT', please make sure you are aware of the rules of each format privided by Google Chart.
	'row'(type is QuerySet):[{'a':'myA'},{'b':'myB'},{'c':'myC'},{'d':'myD},{'e':'myE'},...]},
"package":"...", 
"callBackMethod":"...", 
"chartType":"..., 
"elementId":"...", 
"functionFormatted":"..."
};
"""


class NotExistException(Exception):
    """The not exist exception."""

    def ___init__(self):
        self.errorMessage = "Wrong : the element is not existed!"

    def __str__(self):
        return repr(self.errorMessage)


class ParameterMissingException(Exception):
    """The parameters missing exception."""

    def ___init__(self):
        self.errorMessage = "Wrong : you miss some parameters!"

    def __str__(self):
        return repr(self.errorMessage)


class ElementEmptyException(Exception):
    """The elements empty exception."""

    def ___init__(self):
        self.errorMessage = "Wrong : this element is empty!"

    def __str__(self):
        return repr(self.errorMessage)


class NotRequiredElementException(Exception):
    """The elements not required exception."""

    def ___init__(self):
        self.errorMessage = "Wrong : this element is not required!"

    def __str__(self):
        return repr(self.errorMessage)


class GoogleChart(object):
    """
    outputs JS code of google chart
    only supports four type:
        pie chart, column chart, bar chart, scatter cahrt
    the ideal input is listed as the above
    """

    template = """google.charts.load('current', {{packages:['{_pkg}']}});
    google.charts.setOnLoadCallback({_callBackMethod});
    function {_callBackMethod}() {{
    var data = new google.visualization.DataTable({_dataTable}); 
    var chart = new google.visualization.{_chartType}(document.getElementById('{_elementId}'));
    chart.draw(data{_option});
    }}"""

    @classmethod
    def draw(cls, data):
        """
        input:
            data is a dictoinary.
            its format should be:
                {"column":"...", -- must
                 "rows":"...", -- must
                 "option":"...",  -- optional
                 "package":"...",  -- must
                 "callBackMethod":"...",  -- must
                 "chartType":"...",  -- must
                 "elementId":"..." -- must
                }
        """
        generateJSCode = GenerateJSCode()

        generateJSCode.dataTable = data
        if data.get("option", 0) != 0:
            GenerateJSCode.option = data["option"]
        generateJSCode.pkg = data["pkg"]
        generateJSCode.callBackMethod = data["callBackMethod"]
        generateJSCode.chartType = data["chartType"]
        generateJSCode.elementId = data["elementId"]
        return cls.template.format_map(vars(GenerateJSCode))

class GenerateJSCode(object):

    @property
    def dataTable(self):
        return self._dataTable

    @dataTable.setter
    def dataTable(self, data):
        table = DataTable(data["column"], data["rows"])
        row = data["rows"]
        if 'format' in row:
            self.setFunctionFormatted(row["format"])
        self._dataTable = table.getTable()

    def switchChartOption(cls, key, data):
        if key == PIECHART:
            return Option.pieChartOption(data)
        elif key == COLUMNCHART:
            return Option.columnChartOption(data)
        elif key == SCATTERCHART:
            return Option.scatterChartOption(data)
        elif key == BARCHART:
            return Option.columnChartOption(data)

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self, data):
        options = self.switchChartOption(data[0]["type"], data[1])
        self._option = options
        return

    @property
    def pkg(self):
        return self._pkg

    @pkg.setter
    def pkg(self, data):
        self._pkg = data
        return

    @property
    def callBackMethod(self):
        return self._callBackMethod

    @callBackMethod.setter
    def callBackMethod(self, data):
        self._chartType = data
        return

    @property
    def chartType(self):
        return self._chartType

    @chartType.setter
    def chartType(self, data):
        self._chartType = data
        return

    @property
    def elementId(self):
        return self._elementId

    @elementId.setter
    def elementId(self, data):
        self._elementId = data
        return

    @property
    def functionFormatted(self):
        return self._funcFormatted

    @functionFormatted.setter
    def functionFormatted(self, data):
        self._funcFormatted = data
        return

class DataTable(object):

    def __init__(self, column, row):
        self.column = Column(column).getColumns()
        self.row = Row(row, self.columnTemplate(column)).getRows()

    def columnTemplate(self, column):
        template, temp, index, i, count = {}, {}, [0, 0], 0, 0
        previousIsRole = False
        for element in column:
            flag = 'role' in element
            if flag != previousIsRole:
                previousIsRole = flag
                template[count] = temp
                count += 1
                temp = {}
                i = abs(i - 1)
            temp[index[i] + 1] = element['label']
            index[i] += 1
        template[count] = temp
        return template

    def getTable(self):
        return "{'cols':[" + self.column + "],'rows':[" + self.row + "]}"


class Item(object):

    def __init__(self, length):
        if length == 0:
            raise ElementEmptyException

    def check(self, input):
        if not COLMAP.has_key(input):
            raise NotRequiredElementException
        else:
            return

    def parse(self, item, result):
        key = item[0]
        value = item[1]
        index = COLMAP[key]
        self.template[index - 1] = ''.join(['', value])
        intermediate = ''.join(self.template[index - 2: index + 1])
        result = result.join(['', intermediate])
        return result

    @abstractmethod
    def parseMapElement(self, element, result, indexR):
        raise NotImplementedError

    def parseByTemplate(self, data, head, tail):
        result = ""
        for indexR, mapElement in enumerate(data):
            result = result.join(['', head])
            result = self.parseMapElement(mapElement, result, indexR)
            result = result[:-1].join(['', tail])
        result = result[:-1]
        return result


class Column(Item):
    """
    every column has 4 elements: id, label, pattern, type
    id seems useless
    label will be passed form user input + must
    pattern will be passed from user input + default is ''
    type will be passed from user input + must
    a special column, role, has 5 elements: id, label, pattern, type, role
    id is ''
    label is ''
    pattern is ''
    type will be passed from user input + must
    role will be passed from user input + must
    """

    def __init__(self, column):
        super(Column, self).__init__(len(column))
        self.column = column
        self.template = ["{", "'id':'", '', "',", "'label':'", '', "',", "'pattern':'", '', "',", "'type':'", '', "',",
                         "'p':{'role':'", '', "'},", "},"]

    def check(self, data):
        if data not in COLMAP:
            raise NotRequiredElementException
        else:
            return

    def parse(self, item, result):
        key = item[0]
        value = item[1]
        index = COLMAP[key]
        self.template[index - 1] = ''.join(['', value])
        intermediate = ''.join(self.template[index - 2: index + 1])
        result = result.join(['', intermediate])
        return result

    def parseMapElement(self, mapElement, result, indexR):
        for item in mapElement.items():
            self.check(item[0])
            result = self.parse(item, result)
        return result

    def parseByTemplate(self, data, head, tail):
        """                     0     1      2    3      4        5    6       7        8     9      10     11   12       13       14   15
        column template list: ["{", "id:'", '', "',", "label:'", '', "',", "pattern:'", '', "',", "type:'", '', "',", "p:{role:'", '', "'},", "},"]
        row template list: ['{c:[', "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", ']},']
        row template list: ['{c:[', "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", ']},']
        """
        result = ""
        for mapElement in data:
            result = result.join(['', head])
            result = self.parseMapElement(mapElement, result)
            result = result[:-1].join(['', tail])
        result = result[:-1]
        return result

    def getColumns(self):
        """
        the formatted output is(ignore space and '\n'):
        "{id:'',label:'Month',pattern:'',type:'string'},
         {id:'',label:'Sales',pattern:'',type:'number'},
         {id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},
         {id:'',label:'',pattern:'',type:'number',p:{role:'interval'}},
         {id:'',label:'Expenses',pattern:'',type:'number'}"
        """
        result = super().parseByTemplate(self.column, self.template[0], self.template[-1])
        return result


class Row(Item):
    """
    every row has 2 elements: v(value), f(format)
    v will be passed from user input + must
    f will be passed from user input + default is ''
    """

    def __init__(self, row, columnTemplate):
        super(Row, self).__init__(len(row))
        self.row = row["row"]
        self.columnTemplate = columnTemplate
        self.lengthOfColumnTemplate = len(self.columnTemplate)
        self.customerized = False
        if "roleValue" in row:
            self.customerized = True
            self.roleValue = self.legitimize(row["roleValue"])
        self.template = ["{'v':'", '', "','f':null},"]

    def legitimize(self, data):
        realLength = len(data)
        length = len(self.row)
        if realLength < length:
            distance, empty = length - realLength, ['']
            for time in range(1, len(data[0])):
                empty.append('')
            for index in range(1, distance + 1):
                data.append(empty)
        elif realLength > length:
            data = data[:length]
        return data

    def parse(self, value, result):
        self.template[1] = ''.join(['', value])
        result = result.join(['', ''.join(self.template)])
        return result

    def parseMapElement(self, mapElement, result, indexR):
        if not self.customerized:
            for item in mapElement.items():
                result = self.parse(item[1], result)
        elif self.customerized:
            for index in range(0, self.lengthOfColumnTemplate, 2):
                for (k, v) in self.columnTemplate[index].items():
                    result = self.parse(mapElement[v], result)
                if index + 1 < self.lengthOfColumnTemplate:
                    for (k, v) in self.columnTemplate[index].items():
                        result = self.parse(self.roleValue[indexR][k - 1], result)
        return result

    def getRows(self):
        """
        the formatted output is(ignore space and '\n'):
        "{c:[{v:'April',f:null},{v:1000,f:null},{v:900,f:null},{v:1100,f:null},{v:400,f:null}]},
         {c:[{v:'May',f:null},{v:1170,f:null},{v:1000,f:null},{v:1200,f:null},{v:460,f:null}]},
         {c:[{v:'June',f:null},{v:660,f:null},{v:550,f:null},{v:800,f:null},{v:1120,f:null}]},
         {c:[{v:'July',f:null},{v:1030,f:null},{v:null,f:null},{v:null,f:null},{v:540,f:null}]}"
        """
        result = super().parseByTemplate(self.row, "{'c':[", "]},")
        return result


class Format(object):

    @classmethod
    def parseFunctionFormat(cls, functionFormattedList):
        """
        {'format':[{'type':FORMATTYPE,'cparameter':{,,,},'func':[NAMEOFFUNCTION:(,,,),'cols':[,,,],...]},
                   {'type':FORMATTYPE,'cparameter':{,,,},'func':[NAMEOFFUNCTION:(,,,),'cols':[,,,],...]}]}
        """
        temp, result, index = [], "", 0
        for mapElement in functionFormattedList:
            typ = mapElement["type"]
            if mapElement.get("cparameter") is not None:
                cparameter = mapElement["cparameter"]
            else:
                cparameter = ""
            initializer = "var formatter_{index}=new google.visualization.{typ}({cparameter});".format_map(vars())
            rec = []
            if mapElement.get("func") is not None:
                for funcs in mapElement["func"]:
                    funcString = "formatter_{index}.{name}({para});"
                    for propertities in funcs.items():
                        name = propertities[0]
                        para = ','.join(propertities[1])
                        funcString = funcString.format_map(vars())
                        break
                    rec.append(funcString)
                    for col in funcs["cols"]:
                        rec.append("formatter_{index}.format(data,{col});".format_map(vars()))
            temp.append(initializer)
            temp.append(''.join(rec))
            index += 1

        result = ''.join(temp)
        return result


class Option(object):

    @classmethod
    def dictionaryToString(cls, m):
        res = '{' + ','.join('{!s}:{!r}'.format(k, v) for (k, v) in m.items()) + '}'
        return ','.join(['', res])

    @classmethod
    def pieChartOption(cls, options):
        return cls.dictionaryToString(options)

    @classmethod
    def columnChartOption(cls, options):
        return cls.dictionaryToString(options)

    @classmethod
    def scatterChartOption(cls, options):
        return cls.dictionaryToString(options)
