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
# possible input:
"""
column:
[{'label':'mylabel','type':'mytype','role':'myrole'},
{'id':'myid1','label':'mylabel1','pattern':'mypattern1','type':'mytype1'},{...}]
row:
{'row':[{'a':'myA'},{'b':'myB'},{'c':'myC'},{'d':'myD},{'e':'myE'},...]}
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
    """need to take care of the chartType to match with 'new google.visualization.'
       also need to take care of the formatting code!
    """

    template = """google.charts.load('current', {{packages:['{pkg}']}});
    google.charts.setOnLoadCallback({callBackMethod});
    function {callBackMethod}() {{
    var data = new google.visualization.DataTable({dataTable}); 
    var chart = new google.visualization.{chartType}(document.getElementById('{elementId}'));
    chart.draw(data{option});
    }}"""
    # template = """google.charts.load('current', {{packages:[{pkg}]}});
    # """

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
        """jsCode = GenerateJSCode()
        jsCode.setDataTable(data["column"], data["rows"])
        print(data.get("option", 0))
        if data.get("option", 0) != 0:
            jsCode.setOption(data["option"])
        jsCode.setOthers(
            {"pkg": data["pkg"], "callBackMethod": data["callBackMethod"], "chartType": data["chartType"],
             "elementId": data["elementId"]})
        maps = jsCode.getElementsMap()
        print("maps = ")
        print(maps)
        print(type(maps))
        print("data = ")
        print(data)
        print(type(data))
        print("data['pkg']")
        print(data["pkg"])
        pkg = data["pkg"]
        # tempRes = "google.charts.load('current', {packages:" + "p" + "});"
        return cls.template.format_map(vars())
        # return tempRes"""

        GenerateJSCode.setDataTable(data["column"], data["rows"])
        print(data.get("option", 0))
        if data.get("option", 0) != 0:
            GenerateJSCode.setOption(data["option"])
        print("options from data: ")
        # print(data["option"])
        print(GenerateJSCode.option)
        GenerateJSCode.setPkg(data["pkg"])
        GenerateJSCode.setCallBackMethod(data["callBackMethod"])
        GenerateJSCode.setChartType(data["chartType"])
        GenerateJSCode.setElementId(data["elementId"])
        # tempRes = "google.charts.load('current', {packages:" + "p" + "});"
        # print(vars(GenerateJSCode))
        return cls.template.format_map(vars(GenerateJSCode))
        # return tempRes

"""class GenerateJSCode(object):

    # a dictionary holds
    # 1.dataTable is a list(column(id, label, type, pattern), role(id, label, type, pattern, role), row(value, format))
    # 2.dataView(unnecessary right now)
    # 3.option is a list(the first element should specify which chart)
    def __init__(self):
        # self.elementsMap = {"dataTable": "", "option": "",
        #                    "others": {"package": "", "callBackMethod": "", "chartType": "", "elementId": "",
        #                               "functionFormatted": ""}}
        self.dataTable, self.option, self.pkg, self.callBackMethod, self.charType, self.elementId, self.functionFormatted = '', '', '', '', '', '', ''

    def setDataTable(self, column, row):
        table = DataTable(column, row)
        if 'format' in row:
            self.setFunctionFormatted(row["format"])
        # self.elementsMap["dataTable"] = table.getTable()
        self.dataTable = table.getTable()
        return

    @staticmethod
    def switchChartOption(key, data):
        if key == PIECHART:
            return Option.pieChartOption(data)
        elif key == COLUMNCHART:
            return Option.columnChartOption(data)
        elif key == SCATTERCHART:
            return Option.scatterChartOption(data)

    def setOption(self, data):
        # if data is not None:
        options = self.switchChartOption(data[0], data[1])
        # self.elementsMap["option"] = options
        self.option = options
        return

    def checkExistOrPassValue(self, key, data):
        if data[key] is not None:
            self.elementsMap["others"][key] = data[key]
        else:
            raise NotExistException
        return

    def setOthers(self, data):
        # data: a dictonary
        for (k, v) in data.items():
            self.checkExistOrPassValue(k, data)
        if len(data) < 4:
            raise ParameterMissingException
        return

    def setFunctionFormatted(self, data):
        self.elementsMap["functionFormatted"] = Format.parseFunctionFormat(data)
        return

    def getElementsMap(self):
        return self.elementsMap"""

class GenerateJSCode(object):
    dataTable, option, pkg, callBackMethod, chartType, elementId, functionFormatted = '', '', '', '', '', '', ''

    @classmethod
    def setDataTable(cls, column, row):
        table = DataTable(column, row)
        if 'format' in row:
            cls.setFunctionFormatted(row["format"])
        cls.dataTable = table.getTable()

    @classmethod
    def switchChartOption(cls, key, data):
        print("this is key : ")
        print(key)
        if key == PIECHART:
            return Option.pieChartOption(data)
        elif key == COLUMNCHART:
            return Option.columnChartOption(data)
        elif key == SCATTERCHART:
            return Option.scatterChartOption(data)
        elif key == BARCHART:
            return Option.columnChartOption(data)

    @classmethod
    def setOption(cls, data):
        options = cls.switchChartOption(data[0]["type"], data[1])# Option.dictionaryToString(data[1])# cls.switchChartOption(data[0], data[1])
        print(options)
        cls.option = options
        return

    @classmethod
    def setPkg(cls, data):
        cls.pkg = data
        return

    @classmethod
    def setCallBackMethod(cls, data):
        cls.callBackMethod = data
        return

    @classmethod
    def setChartType(cls, data):
        cls.chartType = data
        return

    @classmethod
    def setElementId(cls, data):
        cls.elementId = data
        return

    @classmethod
    def setFunctionFormatted(cls, data):
        cls.functionFormatted = data
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
        # raise NotIMplementedError
        pass
        """for item in mapElement.items():
            check(k)
            result = parse(item, result)
        return result"""

    def parseByTemplate(self, data, head, tail):
        """                     0     1      2    3      4        5    6       7        8     9      10     11   12       13       14   15
        column template list: ["{", "id:'", '', "',", "label:'", '', "',", "pattern:'", '', "',", "type:'", '', "',", "p:{role:'", '', "'},", "},"]
        row template list: ['{c:[', "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", ']},']
        row template list: ['{c:[', "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", ']},']
        """
        result = ""
        for indexR, mapElement in enumerate(data):
            result = result.join(['', head])
            print(indexR)
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
            print(data)
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
            # print(result)
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
        # result = self.parseByTemplate(self.column, self.template[0], self.template[-1])
        """result = ""
        head, tail = self.template[0], self.template[-1]
        for mapElement in self.column:
            result = result.join(['', head])
            # result = parseELement(mapElement, result)
            for item in mapElement.items():
                # check(k)
                if item[0] not in COLMAP:
                    raise NotRequiredElementException
                else:
                    return 
                result = parse(item, result)
            result = result[:-1].join(['', tail])
        result = result[:-1]"""
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
        # print(self.columnTemplate)
        self.lengthOfColumnTemplate = len(self.columnTemplate)
        self.customerized = False
        if "roleValue" in row:
            self.customerized = True
            self.roleValue = self.legitimize(row["roleValue"])
            # print(self.roleValue)
        self.template = ["{'v':'", '',
                         "','f':null},"]  # super().generateTemplate(formatted, ["{v:'",'',"',f:null},"], super().length, "{c:[", "]},")

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
        # print(result)
        return result

    def parseMapElement(self, mapElement, result, indexR):
        if not self.customerized:
            for item in mapElement.items():
                result = self.parse(item[1], result)
        elif self.customerized:
            for index in range(0, self.lengthOfColumnTemplate, 2):
                for (k, v) in self.columnTemplate[index].items():
                    # print(mapElement[v])
                    result = self.parse(mapElement[v], result)
                if index + 1 < self.lengthOfColumnTemplate:
                    for (k, v) in self.columnTemplate[index].items():
                        # print("r=%d, c=%d, [%d, %d]" % (len(self.roleValue), len(self.roleValue[0]), indexR, k - 1))
                        result = self.parse(self.roleValue[indexR][k - 1], result)
            # self.roleValue.pop(0)
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
        print("--------------------------dictionaryToString function processing...")
        res = '{' + ','.join('{!s}:{!r}'.format(k, v) for (k, v) in m.items()) + '}'
        print("--------------------------%s" % res)
        return ','.join(['', res])

    @classmethod
    def pieChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of pie chart
        ex:
        {legend: 'none',
        pieSliceText: 'none',
        pieStartAngle: 135,
        tooltip: { trigger: 'none' },
        slices: {
            0: { color: 'yellow' },
            1: { color: 'transparent' }
        }}
        output：{legend:'none',pieSliceText:'none',pieStartAngle:135,tooltip:{'trigger': 'none'},slices:{0: {'color': 'yellow'}, 1: {'color': 'transparent'}}}
        '''
        # return cls()
        return cls.dictionaryToString(options)

    @classmethod
    def columnChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of column chart
        '''
        # return cls()
        return cls.dictionaryToString(options)

    @classmethod
    def scatterChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of scatter chart
        '''
        # return cls()
        return cls.dictionaryToString(options)

        # {'legend': 'none','pieSliceText': 'none','pieStartAngle': 135,'tooltip': { 'trigger': 'none' },'slices': {0: { 'color': 'yellow' },1: { 'color': 'transparent' }}}
