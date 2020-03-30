from lxml import etree
readResult = ''
# file = open('columnChart.html', 'r')
# read byte by byte
"""with open('columnChart.html', 'rt') as file:
    for line in file:
        readResult.join(line)"""
# read lien by line
with open('columnChart.html', 'rt') as file:
    line = file.readline()
    while line:
        readResult = readResult.join(line)
        line = file.readline()
file.close()
print(readResult)
documents = etree.HTML(readResult)
tdList = documents.xpath('//table/tr/td[1]/text()')

print(tdList)
file = open('chartOptions.txt', 'wt')
for ele in tdList:
    file.write('%s\n' % (ele.upper()))
file.close()
