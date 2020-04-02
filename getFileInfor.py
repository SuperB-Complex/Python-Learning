import time
import datetime
import os


# time format transfer
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)　　　　　　
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

# get the size of file in terms of B
def get_FileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize, 2)

# get the time of visiting the file
def get_FileAccessTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)

# get the time of creating the file
def get_FileCreateTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

# get the time of creating the file
def get_FileModifyTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)