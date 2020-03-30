import json
import requests
import aiohttp
import time
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
# stateQueue = asyncio.Queue()

def getURL():
    info, result = "", []
    with open("customised.txt", "r", encoding="utf-8") as f:
        for row in f.readline():
            info += row
    array = info.split("}{")
    array[0] += "}"
    array[-1] = "{" + array[-1] 
    for item in array[1:-1]:
        item = "{" + item + "}"
        item = json.loads(item)
        result.append(item['url'])
    return result

def normallyRequestWeb(urls):
    states = []
    for url in urls:
        result = requests.get(url, headers=HEADER)
        code = result.status_code
        print(code)
        states.append(code)
    writeFile("normallyRequestWeb.txt", states) 

# async def updateStateQueue(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=HEADER) as response:
#             # await stateQueue.put(response.status)
#             # print(response.status)
#             pass

# async def asyncallyRequestWeb(urls):
#     task = []
#     for url in urls:
#         task.append(asyncio.ensure_future(updateStateQueue(url)))
#     await asyncio.wait(task)

def writeFile(fileName, data):
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write(str(data))

def getRequestingTime():
    urls = getURL()
    start = time.time()
    normallyRequestWeb(urls)
    end = time.time()
    duration = end - start
    print("duration is %ss" % (str(duration)))

getRequestingTime() # 120s
# loop = asyncio.get_event_loop()
# urls = getURL()
# start = time.time()
# loop.run_until_complete(asyncallyRequestWeb(urls))
# end = time.time()
# duration = end - start
# print("duration is %ss" % (str(duration)))
# try:
#     start = time.time()
#     loop.run_until_complete(asyncallyRequestWeb(getURL()))
# except:
#     print("something goes wrong while executing function asyncallyRequestWeb")
# finally:
#     # writeFile("asyncallyRequestWeb.txt", stateQueue)
#     loop.close()
#     end = time.time()
#     duration = end - start
#     print("duration is %ss" % (str(duration)))

async def get_body(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            assert response.status == 200
            html = await response.read()
            return response.status

async def get_results(url):
    code = await get_body(url)
    return 'Completed'

async def handle_tasks(task_id, work_queue):
    while not work_queue.empty():
        current_url = await work_queue.get()
        try:
            task_status = await get_results(current_url)
        except Exception as e:
            logging.exception('Error for {}'.format(current_url), exc_info=True)

def eventloop(urls):
    q = asyncio.Queue()
    [q.put_nowait(url) for url in urls]
    loop = asyncio.get_event_loop()
    tasks = [handle_tasks(task_id, q) for task_id in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

start = time.time()
urls = getURL()
eventloop(urls)
end = time.time()
duration = end - start
print("duration is %ss" % (str(duration))) # 25s