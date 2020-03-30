import logging
import asyncio
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from bs4 import BeautifulSoup
import datetime
import time
import json

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',) #filename='ranking.log',


def initialSpider(url):
    if url is None:
        logging.debug("the url which is going to be initialized should not be None. ")
        raise ValueError
    try:
        DRIVER = webdriver.Chrome()
    except:
        time.sleep(10)
        DRIVER = initialSpider(url)
    else:
        # DRIVER.implicitly_wait(0)
        DRIVER.get(url)
        WAITER = WebDriverWait(DRIVER, 10, 0.5)
        return DRIVER, WAITER

def trimCompeleted(input):
    input = input.lstrip()
    input = input.rstrip()
    input = input.replace(' ', '')
    return input

def trimBOM(input):
    result = input
    if input[0] == b'\xef\xbb\xbf':
        result =  input[1:]
    else:
        result = input
    return result

def filterAndConvertValue(input):
    result = input
    if input is None:
        raise ValueError
    else:
        input = trimBOM(trimCompeleted(input)).lower()
        result = input
    return result

def filterAndConvertIndex(input, prefix=None):
    if input is None:
        return "####"
    result = input
    REPLACE = ['&', '-', '$(m)', '($m)†', '%']
    try:
        input = filterAndConvertValue(input)
    except ValueError:
        raise ValueError
    else:
        for element in REPLACE:
            if element in input:
                input.replace(element, '_')
        if prefix is not None:
            result = (prefix + input).lower()
    return result

async def asyncioFindElement(driver, waiter, selection, subElement=None, MAXTRYING=5, SLEEP=1):
    waiter = WebDriverWait(driver, 10, 0.5)
    try:
        val = None
        if selection == 1:
            logging.debug("------------------going to select asyncioFindElement(1)")
            val = subElement.find_elements_by_xpath("//tr[@class='headerrow']/th/h2/a[starts-with(@href, '/businessschoolrankings/executive-education-')]")
            logging.debug("------------------finish select asyncioFindElement(1)")
        elif selection == 2:
            logging.debug("------------------going to select asyncioFindElement(2)")
            val = subElement.find_elements_by_css_selector("td")
            logging.debug("------------------finish select asyncioFindElement(2)")
        elif selection == 3:
            logging.debug("------------------going to select asyncioFindElement(3)")
            val = subElement.find_element_by_xpath(".//span")
            logging.debug("------------------finish select asyncioFindElement(3)")
        elif selection == 4:
            logging.debug("------------------going to select asyncioFindElement(4)")
            val = subElement.find_element_by_tag_name('tbody')
            logging.debug("------------------finish select asyncioFindElement(4)")
        elif selection == 5:
            logging.debug("------------------going to select asyncioFindElement(5)")
            val = subElement.find_elements_by_css_selector("tr.shade")
            logging.debug("------------------finish select asyncioFindElement(5)")
        elif selection == 6:
            logging.debug("------------------going to select asyncioFindElement(6)")
            val = subElement.find_elements_by_tag_name("tr")
            logging.debug("------------------finish select asyncioFindElement(6)")
        elif selection == 7:
            logging.debug("------------------going to select asyncioFindElement(7)")
            val = subElement.find_element_by_xpath(".//td[@class='text ']/a") # find_element_by_css_selector("td.text").find_element_by_tag_name("a").get_attribute("href")
            logging.debug("------------------finish select asyncioFindElement(7)")
    except:
        driver.refresh()
        time.sleep(SLEEP * 2)
        if MAXTRYING == 0:
            logging.debug("async def asyncioFindElement(driver, selection, subElement=None):  %s !!!!!!!" % (driver.current_url))
            if selection == 1:
                logging.debug("//tr[@class='headerrow']/th/h2/a[starts-with(@href, '/businessschoolrankings/executive-education-')]: trying 5 times!!!!!!!!!!!!!")
            elif selection == 2:
                logging.debug("td: trying 5 times!!!!!!!!!!!!!")
            elif selection == 3:
                logging.debug("span: trying 5 times!!!!!!!!!!!!!")
            elif selection == 4:
                logging.debug("tbody: trying 5 times!!!!!!!!!!!!!")
            elif selection == 5:
                logging.debug("tr.shade: trying 5 times!!!!!!!!!!!!!")
            elif selection == 6:
                logging.debug("tr: trying 5 times!!!!!!!!!!!!!")
            elif selection == 7:
                logging.debug("td.text.a.href: trying 5 times!!!!!!!!!!!!!")
            # raise NoSuchElementException
            return None
        elif MAXTRYING > 0:
            return await asyncioFindElement(driver, waiter, selection, subElement, MAXTRYING - 1, SLEEP + 1)
    else:
        if val is None:
            currentURL = driver.current_url
            if selection == 1:
                logging.debug("//tr[@class='headerrow']/th/h2/a[starts-with(@href, '/businessschoolrankings/executive-education-')]:: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 2:
                logging.debug("td: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 3:
                logging.debug("span: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 4:
                logging.debug("tbody: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 5:
                logging.debug("tr.shade: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 6:
                logging.debug("tr: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
            elif selection == 7:
                logging.debug("td.text.a.href: is None!!!!!! the current url is %s !!!!!!!" % (currentURL))
        return val

async def loadingNextPage(driver, waiter):
    try:
        nextLink = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nextlink")))
    except:
        try:
            waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".lastlink_disabled")))
        except:
            logging.debug("no next link + no last link disabled")
            return None
        else:
            driver.close()
            return None
    else:
        return nextLink

async def putRealUrl(driver, waiter, row):
    try:
        col = await asyncioFindElement(driver, waiter, 7, row) 
    except NoSuchElementException:
        logging.debug("async def collectRealUrl(driver): loading real url is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))                    
        return
    else:
        if col is not None:
            url = col.get_attribute("href") 
            if url is not None:
                await realQueue.put(url)
                logging.debug(" putting data ----------- %s ----------- into real queue" % (str(url)))
            else:
                restBaseQueue.put(driver.current_url)
                logging.debug("might be severe error, cause a link does not have a href")
        else:
            restBaseQueue.put(driver.current_url)
            logging.debug("might be severe error, cause a column is None")

async def waitLoading(driver, waiter, selection):
    RANKTABLEID, CSS  = 'rankingstable', '.entitytable '
   
    if selection == 1:
        logging.debug("------------------going to wait waitLoading(1)")
        waiting = waiter.until(EC.presence_of_element_located((By.ID, RANKTABLEID)))
        logging.debug("------------------finish waiting waitLoading(1)")
        if waiting == False:
            logging.debug("loading table[id='rankingstable'] is too long!!!!!!!!!!!!!!")
            return None
        else:
            table = driver.find_element_by_id(RANKTABLEID).find_element_by_tag_name('tbody')
            return table

    elif selection == 2:
        logging.debug("going to wait waitLoading(2)")
        waiting = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS)))
        logging.debug("finish waiting waitLoading(2)")
        if waiting == False:
            logging.debug("loading table[class='entitytable'] is too long!!!!!!!!!!!!!!!")
            return None
        else:
            table = driver.find_elements_by_css_selector("table.entitytable")
            return table

async def updatePage(driver, waiter):
    while True:
        logging.debug("------------------going to call waitLoading(1)")
        table = await waitLoading(driver, waiter, 1)
        logging.debug("------------------finish call waitLoading(1)")
        if table is None:
            await restBaseQueue.put(driver.current_url)
        else:
            await getBaseURL(driver, waiter, table)
            logging.debug("------------------going to call loadingNextPage()")
            nextLink = await loadingNextPage(driver, waiter)
            logging.debug("------------------finish call loadingNextPage()")
            if nextLink is None:
                logging.debug("no next page or severe structure change")
                break    
            else:
                nextLink.click()    
    for index in range(0, PREWORKER):
        await baseQueue.put(None)
    # await baseQueue.join()

async def getBaseURL(driver, waiter, table):
    logging.debug("------------------going to call asyncioFindElement(1)")
    headLists = await asyncioFindElement(driver, waiter, 1, table) #  table.find_elements_by_xpath("//tr[@class='headerrow']/th/h2/a[starts-with(@href, '/businessschoolrankings/executive-education-')]")
    logging.debug("------------------finish call asyncioFindElement(1)")
    for element in headLists[:-1]:
        val = element.get_attribute("href") 
        if val is not None:
            await baseQueue.put(val)
            logging.debug(" putting data ----------- %s ----------- into base queue" % (str(val)))
        else:
            logging.debug("might be severe error, cause a link does not have a href")

# ------------------------------------------------sub cusomer--------------------------------------------------
async def collectRealUrl():
    while True:
        url = await baseQueue.get()
        logging.debug("the base queue is getting data----------- %s -----------" % (str(url)))
        if url is None:
            logging.debug("the base queue is getting None~~~~~~~~~~~~~~~~~~~~~")
            baseQueue.task_done()
            break
        await parseRealUrl(url)
        baseQueue.task_done()
    await realQueue.put(None) 
    # await realQueue.join()

async def parseRealUrl(url):
    driver, waiter = initialSpider(url)
    tables = await waitLoading(driver, waiter, 1)
    if tables is None:    
        restBaseQueue.put(driver.current_url)
        logging.debug("async def collectRealUrl(driver): loading table too long!!!!!!!!!!!!!")
    else:
            try:
                rows = await asyncioFindElement(driver, waiter, 6, tables) 
            except NoSuchElementException:
                logging.debug("async def collectRealUrl(driver): loading row is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
                return
            else:
                if rows is not None:
                    for row in rows[:-1]:
                        await putRealUrl(driver, waiter, row)
                else:
                    restBaseQueue.put(driver.current_url)
    driver.close()

async def collectRealData():
    while True:
        url = await realQueue.get()
        if url is None:
            logging.debug("the real queue is getting None~~~~~~~~~~~~~~~~~~~~~")
            realQueue.task_done()
            break
        else:
            logging.debug("the real queue is getting %s " % (str(url)))
            await parseRealData(url)
            realQueue.task_done()

async def parseRealData(url):
    driver, waiter = initialSpider(url)
    data = await parseTable(driver, waiter)
    driver.close()
    if data is None:
        await restRealQueue.put(url)
    else:
        if "open" in url:
            await writeOpenFile(data)
        elif "customised" in url:
            await writeCustomizedFile(data)

async def parseTable(driver, waiter):
    tables = await waitLoading(driver, waiter, 2)
    if tables is None:
        return None
    else:
        result = {"url": driver.current_url}
        one = await parseYearRankingTable(driver, waiter, tables[0])
        if one is None:
            return None
        elif one is not None:
            two = await parseNormalTable(driver, waiter, tables[1])
            if two is None:
                return None
            elif two is not None:
                three = await parseNormalTable(driver, waiter, tables[2])
                if three is None:
                    return None
                elif three is not None:
                    result.update(one)
                    result.update(two)
                    result.update(three)
                    logging.debug(result)
                    return result
    
async def parseYearRankingTable(driver, waiter, table):
    try:
        tbody = await asyncioFindElement(driver, waiter, 4, table)
    except:
        logging.debug("async def parseYearRankingTable(driver, waiter, table): loading tbody is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
        return None
    else:
        try:
            rows = await asyncioFindElement(driver, waiter, 6, tbody) 
        except NoSuchElementException:
            logging.debug("async def parseYearRankingTable(driver, waiter, table): loading row is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
            return None
        else:
            return await parseRow(driver, waiter, rows[1])

async def parseNormalTable(driver, waiter, table):
    try:
        rows = await asyncioFindElement(driver, waiter, 6, table) 
    except NoSuchElementException:
        logging.debug("async def parseNormalTable(driver, waiter, table): loading row is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
        return None
    else:
        return await parseRows(driver, waiter, rows[1:])

async def parseRows(driver, waiter, rows):
    result = {}
    for row in rows:
        temp = await parseRow(driver, waiter, row)
        result.update(temp)
    return result

async def parseRow(driver, waiter, row):
    result = {}
    try:
        cols = await asyncioFindElement(driver, waiter, 2, row) 
    except NoSuchElementException:
        logging.debug("async def parseRow(driver, waiter, row): loading column is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
        return "####"
    else:
        index = filterAndConvertIndex(cols[0].text)
        try:
            valueRaw = await asyncioFindElement(driver, waiter, 3, cols[1])
        except:
            logging.debug("async def parseRow(driver, waiter, row): loading another column is too long!!!!! the current url is %s !!!!!!!" % (driver.current_url))
            return {"####": "####"}
        else:
            result[index] = filterAndConvertValue(valueRaw.text)
            logging.debug(result)
            return result

async def writeOpenFile(data):
    with open('open.json', 'a', encoding='utf-8') as of:
        json.dump(data, of)

async def writeCustomizedFile(data):
    with open('customised.json', 'a', encoding='utf-8') as cf:
        json.dump(data, cf)

def writeToFile(data, file):
    with open(file, 'a', encoding='utf-8') as of:
        of.write(str(data))
        # while True:
        #     item = await data.get()
        #     if item is not None:
        #         of.write(data + "\n")
        #     else:
        #         break
    return 

PREWORKER, REALWORKER = 5, 5

# async def main():
#     BASEURL = 'http://rankings.ft.com/businessschoolrankings/rankings'
#     web, waiter = initialSpider(BASEURL)
#     baseURL = [asyncio.create_task(updatePage(web, waiter))]
#     collateDatas = [asyncio.create_task(collectRealUrl()) for index in range(0, PREWORKER)]
#     collectRealDatas = [asyncio.create_task(collectRealData()) for index in range(0, REALWORKER)]

#     await asyncio.gather(*collectRealDatas, *collateDatas, *baseURL)  

    # worker = collectRealDatas + collateDatas + baseURL
    # await realQueue.join()
    # await baseQueue.join()
    # [task.cancel() for task in worker]

async def main(loop):
    BASEURL = 'http://rankings.ft.com/businessschoolrankings/rankings'
    web, waiter = initialSpider(BASEURL)
    baseURL = [loop.create_task(updatePage(web, waiter))]
    collateDatas = [loop.create_task(collectRealUrl()) for index in range(0, PREWORKER)]
    collectRealDatas = [loop.create_task(collectRealData()) for index in range(0, REALWORKER)]
    await asyncio.wait(collectRealDatas + collateDatas + baseURL)

baseQueue = asyncio.Queue()
realQueue = asyncio.Queue()
restBaseQueue = asyncio.Queue()
restRealQueue = asyncio.Queue()
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    logging.debug(baseQueue)
    logging.debug(realQueue)
    logging.debug(restBaseQueue)
    logging.debug(restRealQueue)
    writeToFile(baseQueue, 'baseQueue.json')
    writeToFile(realQueue, 'realQueue.json')
    writeToFile(restBaseQueue, 'restBaseQueue.json')
    writeToFile(restRealQueue, 'restBaseQueue.json')
    event_loop.close()
