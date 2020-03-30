import Constants
# user entry class
# ideal input(must make sure col corresponds to row):
"""
column:
[{'id':'myid','label':'mylabel','pattern':'mypattern','type':'mytype'},{'id':'myid1','label':'mylabel1','pattern':'mypattern1','type':'mytype1','role':'myrole1'},{...}]
row:
{'format':[{COLUMNFORMAT:[{'columnFormat1':10},{'columnFormat2':8}]},COLUMNSFORMAT:[{'columnFormat1':[1,2,3,4]},{'columnFormat2':[11,13,14]}]},{CELLFORMAT:['myRow','myColumn','myFormat']}],row':[{'a':'myA'},{'b':'myB'},{'c':'myC'},{'d':'myD},{'e':'myE'},...],'role':['roleValue1','roleValue2','roleValue3']}
"""
# possible input:
"""
column:
[{'label':'mylabel','type':'mytype','role':'myrole'},{'id':'myid1','label':'mylabel1','pattern':'mypattern1','type':'mytype1'},{...}]
row:
{'row':[{'a':'myA'},{'b':'myB'},{'c':'myC'},{'d':'myD},{'e':'myE'},...]}
"""
class NotExistException(Exception):

    """The not exist exception."""
    def ___init__(self):
        self.errorMessage = "Wrong : the element is not existed!"

    def __str__():
        return repr(self.errorMessage)

class ParameterMissingException(Exception):

    """The parameters missing exception."""
    def ___init__(self):
        self.errorMessage = "Wrong : you miss some parameters!"

    def __str__():
        return repr(self.errorMessage)

class ElementEmptyException(Exception):

    """The elements empty exception."""
    def ___init__(self):
        self.errorMessage = "Wrong : this element is empty!"

    def __str__():
        return repr(self.errorMessage)

class NotRequiredElementException(Exception):

    """The elements not required exception."""
    def ___init__(self):
        self.errorMessage = "Wrong : this element is not required!"

    def __str__():
        return repr(self.errorMessage)

class GenerateJSCode(object):

    # a dictionary holds 
    # 1.dataTable is a list(column(id, label, type, pattern), role(id, label, type, pattern, role), row(value, format)) 
    # 2.dataView(ignore cause don't know how to use) 
    # 3.option is a list(the first element should specify which chart)
    def __init__(self):
        self.elementsMap = {"dataTable":"", "option":"", "others":{"package":"", "callBackMethod":"", "chartType":"", "elementId":""}}

    def setDataTable(self, column, row):
        table = DataTable(column[0], column[1:], row)
        self.elementsMap["dataTable"] = table.getTable()
        return

    def switchChartOption(self, key, data):
        if key == PIECHART:
            return Option.pieChartOption(data)
        elif key == COLUMNCHART:
            return Option.columnChartOption(data)
        elif key == SCATTERCHART:
            return Option.scatterChartOption(data)

    def setOption(self, data):
        options = switchChartOption(data[0], data[1:])
        self.elementsMap["option"] = options
        return

    def checkExistOrPassValue(self, key, data):
        if data[key] is not None:
            self.elementsMap["others"][key] = data[key]
        else:
            raise NotExistException
        return

    def setOthers(self, data):
        """
        data: a dictonary
        """
        for (k, v) in data.item():
            checkExistOrPassValue(k, data)
        if len(data) < 4:
            raise ParameterMissingException
        return

class DataTable(object):

    def __init__(self, column, row):
        self.column = Column(column).getColumns()
        self.row = Row(row.has_key("format"), row, columnTemplate(column)).getRows()

    def columnTemplate(self, column):
        template, temp, index, i = [], [], [0, 0], 0
        previousIsRole = False
        for element in column:
            flag = 'role' in element
            if flag != previousIsRole:
                previousIsRole = flag
                template.append(temp)
                temp = []
                i = abs(i - 1)
            temp.append(index[i])
            index[i] += 1
        template.append(temp)
        return template

    def getTable(self):
        return "{cols:[" + self.column + "],rows:[" + self.row + "]}"

class Item(object):

    def __init__(self, length):
        if length == 0:
            raise ElementEmptyException

    """@abstractmethod
    def check(self, input):
        # raise NotImplementedError
        pass

    @abstractmethod
    def parse(self, item, result):
        # raise NotImplementedError
        pass"""

    @abstractmethod
    def parseElement(self, element, result):
        # raise NotIMplementedError
        pass

    def parseByTemplate(self, data, head, tail):
        """                     0     1      2    3      4        5    6       7        8     9      10     11   12       13       14   15  
        column template list: ["{", "id:'", '', "',", "label:'", '', "',", "pattern:'", '', "',", "type:'", '', "',", "p:{role:'", '', "'},", "},"]
        row template list: ['{c:[', "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", "{v:'", '', "',f:null},", ']},']
        row template list: ['{c:[', "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", "{v:'", '', "',f:'", '', "'},", ']},']
        """
        result = ""
        for mapElement in data:
            result = result.join(['', head])
            result = parseELement(mapElement, result)
            result = result[:-1].join(['', tail])
        result = result[:-1]
        return result

    """def emptyList(self):
        self.lst = []
        return"""

    """def generateTemplate(self, formatted, subTemplate, length, head, tail):
        result = [head]
        if formatted == True:
            subTemplate[-1] = "',f:'"
            subTemplate.append('')
            subTemplate.append("'},")
        for index in range(0, length):
            for ele in subTemplate:
                result.append(ele)
        result[-1] = result[-1][:-1]
        result.append(tail)
        return result"""

class Column(Item):

    """
    every column has 4 elements: id, label, pattern, type
    id will be granted to be unique
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
        super().__init__(len(column)) 
        self.column = column
        self.template = ["{", "id:'", '', "',", "label:'", '', "',", "pattern:'", '', "',", "type:'", '', "',", "p:{role:'", '', "'},", "},"]

    def parseElement(self, mapElementelement, result):
        for item in mapElement.items():
            check(k)
            result = parse(item, result)
        return result

    def check(self, input):
        if COLMAP.has_key(input) == False:
            raise NotRequiredElementException
        else:
            return 

    def parse(self, item, result):
        key = item[0]
        value = item[1]
        index = COLMAP[key]
        self.template[index - 1] = ''.join(['', value])
        intermediate = ''.join(self.template[index - 2 : index + 1])
        result = result.join(['', intermediate])  
        return result 

    def getColumns():
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
    def __init__(self, formatted, row, columnTemplate):
        super().__init__(len(row)) 
        self.formatted = formatted
        self.row = row["row"]
        self.columnTemplate = columnTemplate
        self.lengthOfColumnTemplate = len(self.columnTemplate)
        self.customerized = False
        if self.lengthOfColumnTemplate > 1:
            self.customerized = True
            self.roleValue = row["role"]
        self.template = ["{v:'", '', "',f:null},"]# super().generateTemplate(formatted, ["{v:'",'',"',f:null},"], super().length, "{c:[", "]},") 
        if formatted == True:
            # self.template = ["{v:'", '', "',f:'", '', "'},"]
            # self.format = legitimize(row["format"])
            self.format = row["format"]

    def parseElement(self, mapElementelement, result):
        if self.formatted == False and self.customerized == False:
            for item in mapElement.items():
                result = parseUnformetted(item, result)
        elif self.formatted == False and self.customerized == True:
            for index in range(0, self.lengthOfColumnTemplate):
                currentListOfIndex = 
        elif self.formatted == True and self.customerized == False:
            parsedFormat = Format(self.format).parse(self.template)
        else:
            
        return result

    def parseUnformetted(self, item, result):
        value = item[1]
        self.template[1] = ''.join(['', value])
        result = result.join(['', self.template])
        return result

    """def legitimize(self, data):
        realLength = len(data)
        length = len(self.row)
        if realLength < length:
            distance = length - realLength
            for index in range(1, distance + 1):
                data.append(data[-1])
        elif realLength > length:
            data = data[:length]
        return data"""

    def getRows():
        """
        the formatted output is(ignore space and '\n'):
        "{c:[{v:'April',f:null},{v:1000,f:null},{v:900,f:null},{v:1100,f:null},{v:400,f:null}]},
         {c:[{v:'May',f:null},{v:1170,f:null},{v:1000,f:null},{v:1200,f:null},{v:460,f:null}]},
         {c:[{v:'June',f:null},{v:660,f:null},{v:550,f:null},{v:800,f:null},{v:1120,f:null}]},
         {c:[{v:'July',f:null},{v:1030,f:null},{v:null,f:null},{v:null,f:null},{v:540,f:null}]}"
        """
        result =  super().parseByTemplate(self.row, "{c:[", "]},")
        return result

class Format(object):

    def __init__(self, format):
        self.format = format

    def parse(self, baseTemplate):
        for 

class Option(object):

    @classmethod 
    def dictionaryToString(cls, m):
        return ','.join('{!s}={!r}'.format(k, v) for (k, v) in m.items())

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
        '''
        #return cls()
        return dictionaryToString(options)

    @classmethod
    def columnChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of column chart
        '''
        #return cls()
        return dictionaryToString(options)

    @classmethod
    def scatterChartOption(cls, options):
        '''
        options: a dictionary of necessary properties of scatter chart
        '''
        #return cls()
        return dictionaryToString(options)



        # {'legend': 'none','pieSliceText': 'none','pieStartAngle': 135,'tooltip': { 'trigger': 'none' },'slices': {0: { 'color': 'yellow' },1: { 'color': 'transparent' }}}