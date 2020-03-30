import asyncio
import aiohttp
import json
from lxml import html

async def visitRead(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            page = await response.read()
            return page

# async def visitJson(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, timeout=30) as response:
#             # didn'r wokr got an error, MIME type
#             # page = await response.json()
#             # try second
#             # didn't work got an error, json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#             page = await response.json(content_type='text/html')
#             return page

async def visitText(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            assert response.status == 200
            page = await response.text()
            return page

async def visitContent(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            assert response.status == 200
            page = await response.content
            return page

def parsePage(data):
    tree = html.fromstring(data)
    tables = tree.xpath('//table')
    return str(tables)

async def writeFile(selection, url):
    if selection == 0:
        fname = "read.txt"
        temp = await visitRead(url)
        # lxml can't parse binary text of a string format
        # data = parsePage(str(temp))
        data = str(temp)
    # elif selection == 0:
    #     f = "json.txt"
    #     # try first
    #     # didn't work still got the mistype error, MIME type
    #     # temp = await visitJson(url)
    #     # data = json.loads(temp)
    #     data = await visitJson(url)
    elif selection == 1:
        fname = "text.txt"
        # find nothing
        data = parsePage(await visitText(url))
        # data = await visitText(url)
    elif selection == 2:
        fname = "content.txt"
        data = parsePage(await visitContent(url))
    with open(fname, 'w', encoding='utf-8') as of:
        of.write(data)

def run():
    # data = {}
    # read = visitRead(url)
    # json = visitJson(url)
    # text = visitText(url)
    # data = {read:"read.txt", json:"json.txt", text:"text.txt"}
    loop = asyncio.get_event_loop()
    tasks =[writeFile(index, URL) for index in range(0, 2)]
    loop.run_until_complete(asyncio.wait(tasks))

URL = "http://rankings.ft.com/businessschoolrankings/sda-bocconi/executive-education-customised-2019#executive-education-customised-2019"

run()