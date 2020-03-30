import logging
import asyncio
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from bs4 import BeautifulSoup

import time
import json

# logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)


def initialSpider(url):
    DRIVER = webdriver.Chrome()
    DRIVER.implicitly_wait(0)
    DRIVER.get(url)
    return DRIVER

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/executive-education-customised-2019")
# rows = web.find_element_by_id("rankingstable").find_element_by_tag_name('tbody').find_elements_by_css_selector("tr")
# for row in rows[:-1]:
# 	cols = row.find_elements_by_css_selector("td.text")
# 	print(cols)
# 	print(len(cols))
# 	print(cols[0].find_element_by_tag_name("a").get_attribute("href"))
# web.close()

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/iese-business-school/executive-education-customised-2019#executive-education-customised-2019")
# tables = web.find_element_by_css_selector("div.entityinfohalfwidthcontainer").find_elements_by_tag_name('table')
# web.close()

# def filterAndConvertValue(input):
#     if input is None or input is null:
#         raise ValueError
#     else:
#         input = trimBOM(trimCompeleted(input))
#     return lower(input)

# def filterAndConvertIndex(input, prefix=None):
#     REPLACE = ['&', '-', '$(m)', '($m)†', '%']
#     try:
#         input = filterAndConvertValue(input)
#     except ValueError:
#         raise ValueError
#     else:
#         for element in REPLACE:
#             if element in input:
#                 input.replace(element, '_')
#         if prefix is not None or prefix is not null:
#             return lower(prefix + input)

# def parseOtherTable(driver, rows):
#     result = {}
#     for row in rows[:-1]:
#         try:
#             index = filterAndConvertIndex(row.find_element_by_css_selector("td.headcol").get_attribute('text'))
#             value = filterAndConvertValue(row.find_element_by_css_selector("td").find_element_by_css_selector("span").get_attribute('text'))
#         except ValueError:
#             index = '####'
#             value = '####'
#         else:
#             result[index] = value
#     if result is None or len(result) == 0:
#         raise ValueError
#     else:
#         return result

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/iese-business-school/executive-education-customised-2019#executive-education-customised-2019")
# tables = web.find_element_by_css_selector("div.entityinfohalfwidthcontainer").find_elements_by_tag_name('table')
# rows = tables[1].find_element_by_tag_name('tbody').find_elements_by_css_selector("tr.shade")
# for row in rows:
# 	# worked
# 	# cols = row.find_elements_by_css_selector("td") 
# 	# index = cols[0].text
# 	# value = cols[1].find_element_by_xpath(".//span").text
# 	# worked
# 	# index = row.find_element_by_css_selector("td.headcol").get_attribute('innerHTML')
# 	# cols = row.find_elements_by_css_selector("td") 
# 	# value = cols[1].find_element_by_css_selector("span").get_attribute('innerHTML')
# 	# worked
# 	# cols = row.find_elements_by_xpath(".//td")
# 	# index = cols[0].text
# 	# value = cols[1].find_element_by_xpath(".//span").text 
# 	# worked
# 	index = row.find_element_by_xpath(".//td").text
# 	cols = row.find_elements_by_css_selector("td") 
# 	value = cols[1].find_element_by_xpath(".//span").text
# 	# not worked
# 	# index = row.find_element_by_xpath(".//td[@class='headcol tnote']").text cann't find the element
# 	# cols = row.find_elements_by_css_selector("td") 
# 	# value = cols[1].find_element_by_xpath(".//span").text 
# 	print(index)
# 	print(value)
# # parseOtherTable(web, )
# web.close()

# def trimCompeleted(input):
#     input = input.lstrip()
#     input = input.rstrip()
#     input = input.replace(' ', '')
#     return input

# def trimBOM(input):
#     result = input
#     if input[0] == b'\xef\xbb\xbf':
#         result =  input[1:]
#     else:
#         result = input
#     return result

# def filterAndConvertValue(input):
#     result = input
#     if input is None:
#         raise ValueError
#     else:
#         input = trimBOM(trimCompeleted(input)).lower()
#         result = input
#     return result

# def filterAndConvertIndex(input, prefix=None):
#     result = input
#     REPLACE = ['&', '-', '$(m)', '($m)†', '%']
#     try:
#         input = filterAndConvertValue(input)
#     except ValueError:
#         raise ValueError
#     else:
#         for element in REPLACE:
#             if element in input:
#                 input.replace(element, '_')
#         if prefix is not None:
#             result = (prefix + input).lower()
#     return result

# def parseRow(driver, row):
#     result = {}
#     try:
#         cols = row.find_elements_by_css_selector("td")
#         index = filterAndConvertIndex(cols[0].text)
#         value = filterAndConvertValue(cols[1].find_element_by_xpath(".//span").text)
#     except ValueError:
#         index = '####'
#         value = '####'
#     else:
#         result[index] = value
#     if result is None or len(result) == 0:
#         raise ValueError
#     return result
    
# def parseTable(driver, rows):
#     result = {}
#     for row in rows:
#         try:
#             temp = parseRow(driver, row)
#         except ValueError:
#             {'####':'####'}
#         else:
#             result.update(temp)
#     if result is None or len(result) == 0:
#         raise ValueError
#     return result

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/iese-business-school/executive-education-customised-2019#executive-education-customised-2019")
# tables = web.find_element_by_css_selector("div.entityinfohalfwidthcontainer").find_elements_by_tag_name('table')
# fisrtDict = parseRow(web, tables[0].find_element_by_tag_name('tbody').find_elements_by_css_selector("tr.shade")[0])
# secondDict = parseTable(web,  tables[1].find_element_by_tag_name('tbody').find_elements_by_css_selector("tr.shade"))
# thirdDict = parseTable(web, tables[2].find_element_by_tag_name('tbody').find_elements_by_css_selector("tr.shade"))
# result = {}
# result.update(fisrtDict)
# result.update(secondDict)
# result.update(thirdDict)
# # print(fisrtDict)
# # print(secondDict)
# # print(thirdDict)
# print(result)
# web.close()

# def asyncioFindElement1(driver, selection, subElement=None):
#     MAXTRYING = 3
#     while True:
#         try:
#             if selection == 1:
#                 val = subElement.find_element_by_tag_name('tbody')
#             if selection == 2:
#                 val = subElement.find_elements_by_css_selector("tr.shade")
#         except (NoSuchElementException, StaleElementReferenceException):
#             driver.refresh()
#             MAXTRYING -= 1
#             if MAXTRYING == 0:
#                 return None
#             elif MAXTRYING == 0:
#                 logging.debug("async def asyncioFindElement1(driver, selection, subElement=None):  ")
#                 if selection == 1:
#                     logging.debug("tbody: trying 5 times!!!!!!!!!!!!!")
#                 elif selection == 2:
#                     logging.debug("tr.shade: trying 5 times!!!!!!!!!!!!!")
#                 raise NoSuchElementException
#             elif MAXTRYING > 0:
#                 continue
#         else:
#             return val

# def waitLoading11(driver):
#     MAXTRYING, DIVCONTAINER11 = 5, 'div.entityinfocontainer'
#     while True:
#         try:
#             table = driver.find_element_by_css_selector(DIVCONTAINER11).find_elements_by_tag_name('table')
#         except:
#             driver.refresh()
#             MAXTRYING -= 1
#             if MAXTRYING == 0:
#                 logging.debug("async def waitLoading11(driver): trying 5 times!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                 raise NoSuchElementException
#             elif MAXTRYING > 0:
#                 continue
#         else:
#             return table

# def waitLoading1(driver):
#     MAXTRYING, DIVCONTAINER1 = 2, 'div.entityinfohalfwidthcontainer'
#     while True:
#         try:
#             table = driver.find_element_by_css_selector(DIVCONTAINER1).find_elements_by_tag_name('table')
#         except:
#             driver.refresh()
#             MAXTRYING -= 1
#             if MAXTRYING == 0:
#                 logging.debug("async def waitLoading1(driver): trying 5 times!!!!!! now trying async def waitLoading11(driver) ")
#                 try:
#                     table = waitLoading11(driver)
#                 except NoSuchElementException:
#                     raise NoSuchElementException
#                 else:
#                     return table
#             elif MAXTRYING > 0:
#                 continue
#         else:
#             return table
 
# def parseData(driver):
#     try:
#         tables =  waitLoading1(driver)
#     except NoSuchElementException:
#         logging.debug(" waitLoading1(driver) data is too long!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#         return {}
#     else:
#         MAX = 2
#         while tables is None:
#             MAX -= 1
#             if MAX < 0:
#                 restQueue.put(driver.current_url)
#                 break
#             else:
#                 driver.refresh()
#                 time.sleep(2)
#                 logging.debug("async def parseData(driver): table: is None!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                 tables =  waitLoading1(driver)
#         if tables is not None:
#             try:
#                 firstTable =  asyncioFindElement1(driver, 1, tables[0])
#             except NoSuchElementException:
#                 logging.debug("async def parseData(driver): tbody0: trying 5 times!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                 raise NoSuchElementException
#             else:
#                 MAX = 2
#                 while firstTable is None:
#                     MAX -= 1
#                     if MAX < 0:
#                         restQueue.put(driver.current_url)
#                         break
#                     else:
#                         driver.refresh()
#                         time.sleep(2)
#                         logging.debug("async def parseData(driver): tbody0: is None!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                         firstTable =  asyncioFindElement1(driver, 1, tables[0])
#                 if firstTable is not None:
#                     try:
#                         firstRow =  asyncioFindElement1(driver, 2, firstTable)
#                     except NoSuchElementException:
#                         logging.debug("async def parseData(driver): tbody0: tr.shade: trying 5 times!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                         raise NoSuchElementException
#                     else:
#                         MAX = 2
#                         while firstRow is None:
#                             MAX -= 1
#                             if MAX < 0:
#                                 restQueue.put(driver.current_url)
#                                 break
#                             else:
#                                 driver.refresh()
#                                 time.sleep(2)
#                                 logging.debug("async def parseData(driver): tbody0 tr.shade: is None!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                                 firstRow =  asyncioFindElement1(driver, 2, firstTable)
#                         if firstRow is not None:
#                             fisrtDict = parseRow(driver, firstRow[0])
#                         else:
#                             return None
#                 else:
#                     return None

#             try:
#                 secondTable =  asyncioFindElement1(driver, 1, tables[1])
#             except NoSuchElementException:
#                 logging.debug("async def parseData(driver): tbody1: trying 5 times!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                 raise NoSuchElementException
#             else:
#                 MAX = 2
#                 while secondTable is None:
#                     MAX -= 1
#                     if MAX < 0:
#                          restQueue.put(driver.current_url)
#                         break
#                     else:
#                         driver.refresh()
#                         time.sleep(2)
#                         logging.debug("async def parseData(driver): tbody1: is None!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                         secondTable =  asyncioFindElement1(driver, 1, tables[1])
#                 if secondTable is not None:
#                     try:
#                         secondRows =  asyncioFindElement1(driver, 2, secondTable)
#                     except NoSuchElementException:
#                         logging.debug("async def parseData(driver): tbody1: tr.shade: trying 5 times!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                         raise NoSuchElementException
#                     else:
#                         MAX = 2
#                         while secondRows is None:
#                             MAX -= 1
#                             if MAX < 0:
#                                  restQueue.put(driver.current_url)
#                                 break
#                             else:
#                                 driver.refresh()
#                                 time.sleep(2)
#                                 logging.debug("async def parseData(driver): tbody1: tr.shade: is None!!!!!! the current url is %s !!!!!!!" % (driver.current_url))
#                                 secondRows =  asyncioFindElement1(driver, 2, secondTable)
#                         if secondRows is not None:
#                             secondDict = parseTable(driver, secondRows)
#                         else:
#                             return None
#                 else:
#                     return None

#             try:
#                 thirdTable =  asyncioFindElement1(driver, 1, tables[2])
#             except NoSuchElementException:
#                 logging.debug("async def parseData(driver): tbody2: trying 5 times!!!!!!!!!!!!!")
#                 raise NoSuchElementException
#             else:
#                 MAX = 2
#                 while thirdTable is None:
#                     MAX -= 1
#                     if MAX < 0:
#                          restQueue.put(driver.current_url)
#                         break
#                     else:
#                         driver.refresh()
#                         time.sleep(2)
#                         logging.debug("async def parseData(driver): tbody2: is None!!!!!!!!!!!!!")
#                         thirdTable =  asyncioFindElement1(driver, 1, tables[2])
#                 if thirdTable is not None:
#                     try:
#                         thirdRows =  asyncioFindElement1(driver, 2, thirdTable)
#                     except NoSuchElementException:
#                         logging.debug("async def parseData(driver): tbody2: tr.shade: trying 5 times!!!!!!!!!!!!!")
#                         raise NoSuchElementException
#                     else:
#                         MAX = 2
#                         while thirdRows is None:
#                             MAX -= 1
#                             if MAX < 0:
#                                  restQueue.put(driver.current_url)
#                                 break
#                             else:
#                                 driver.refresh()
#                                 time.sleep(2)
#                                 logging.debug("async def parseData(driver): tbody2: tr.shade: is None!!!!!!!!!!!!!")
#                                 thirdRows =  asyncioFindElement1(driver, 2, thirdTable)
#                         if thirdRows is not None:
#                             thirdDict = parseTable(driver, thirdRows)
#                         else:
#                             return None
#                 else:
#                     return None
#             result = {}
#             result.update(fisrtDict)
#             result.update(secondDict)
#             result.update(thirdDict)
#             return result
#         else:
#             return None

# def parseRow(driver, row):
#     result = {}
#     try:
#         cols = row.find_elements_by_css_selector("td")
#         index = filterAndConvertIndex(cols[0].text)
#         value = filterAndConvertValue(cols[1].find_element_by_xpath(".//span").text)
#     except ValueError:
#         index = '####'
#         value = '####'
#     else:
#         result[index] = value
#     if result is None or len(result) == 0:
#         raise ValueError
#     return result
    
# def parseTable(driver, rows):
#     result = {}
#     for row in rows:
#         try:
#             temp = parseRow(driver, row)
#         except ValueError:
#             result = {'####':'####'}
#         else:
#             result.update(temp)
#     if result is None or len(result) == 0:
#         raise ValueError
#     return result

# def trimCompeleted(input):
#     input = input.lstrip()
#     input = input.rstrip()
#     input = input.replace(' ', '')
#     return input

# def trimBOM(input):
#     result = input
#     if input[0] == b'\xef\xbb\xbf':
#         result =  input[1:]
#     else:
#         result = input
#     return result

# def filterAndConvertValue(input):
#     result = input
#     if input is None:
#         raise ValueError
#     else:
#         input = trimBOM(trimCompeleted(input)).lower()
#         result = input
#     return result

# def filterAndConvertIndex(input, prefix=None):
#     result = input
#     REPLACE = ['&', '-', '$(m)', '($m)†', '%']
#     try:
#         input = filterAndConvertValue(input)
#     except ValueError:
#         raise ValueError
#     else:
#         for element in REPLACE:
#             if element in input:
#                 input.replace(element, '_')
#         if prefix is not None:
#             result = (prefix + input).lower()
#     return result

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/stockholm-school-of-economics/executive-education-customised-2019#executive-education-customised-2019")
# parseData(web)

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/executive-education-customised-2017")
# table = web.find_element_by_id("rankingstable").find_element_by_tag_name('tbody')
# rows = table.find_elements_by_tag_name("tr")
# for row in rows[:-1]:
#     col = row.find_element_by_xpath(".//td[@class='text ']/a")
#     print(row)
#     print(col.get_attribute("href"))
# web.close()

# web = initialSpider("http://rankings.ft.com/businessschoolrankings/duke-corporate-education/executive-education-customised-2014#executive-education-customised-2014")
# tables = web.find_elements_by_css_selector("table.entitytable")
# print(tables)
# web.close()

web = initialSpider("http://rankings.ft.com/businessschoolrankings/essec-business-school/executive-education-customised-2019#executive-education-customised-2019")
tables = web.find_elements_by_css_selector("table.entitytable")
# print(tables)
tbody1 = tables[0].find_element_by_tag_name("tbody")
tbody2 = tables[1].find_element_by_tag_name("tbody")
tbody3 = tables[2].find_element_by_tag_name("tbody")
# print(tbody1)
# print(tbody2)
# print(tbody3)
rows1 = tbody1.find_elements_by_css_selector("td.headcol")
rows2 = tbody2.find_elements_by_css_selector("td.headcol")
rows3 = tbody3.find_elements_by_css_selector("td.headcol")
print(rows1)
print(rows2)
print(rows3)
for row in rows1:
    print(row.text)
for row in rows2:
    print(row.text)
for row in rows3:
    print(row.text)
web.close()