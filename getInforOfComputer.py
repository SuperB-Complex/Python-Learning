import psutil

# get info of CPU
def GetCpuInfo():
    physicalCPU = psutil.cpu_count(logical=False)  # 1 represents the number of physical CPU
    physicalVirtualCPU = psutil.cpu_count()  # the number of physical and virtual CPU
    useRate = round((psutil.cpu_percent(1)), 2)  # cpu using rate
    list = [physicalCPU, physicalVirtualCPU, useRate]
    return list

# get info of memory
def GetMemoryInfo():
    memory = psutil.virtual_memory()
    totalMemory = round(( float(memory.total) / 1024 / 1024 / 1024), 2)  # total memory size
    usedMemory = round(( float(memory.used) / 1024 / 1024 / 1024), 2)  # used memory size
    avaibleMemory = round(( float(memory.free) / 1024 / 1024 / 1024), 2)  # avaiable memory size
    useRate = round((float(memory.used) / float(memory.total) * 100), 2)  # memory using rate
    ret_list = [totalMemory, usedMemory, avaibleMemory, useRate]
    return ret_list

# get info of disk
def GetDiskInfo():
    list = psutil.disk_partitions() # disk list
    ilen = len(list) # the number of disk partition
    i=0
    retlist1=[]
    retlist2=[]
    while i< ilen:
        diskinfo = psutil.disk_usage(list[i].device)
        totalDisk = round((float(diskinfo.total)/1024/1024/1024),2) # total size
        usedDisk = round((float(diskinfo.used) / 1024 / 1024 / 1024), 2) # used size
        freeDisk = round((float(diskinfo.free) / 1024 / 1024 / 1024), 2) # resst size
        useRate = diskinfo.percent # disk using rate
        retlist1=[i, list[i].device, totalDisk, usedDisk, freeDisk, useRate]  # disk name
        retlist2.append(retlist1)  
        i = i + 1
    return retlist2

print(GetCpuInfo())
print(GetMemoryInfo())
print(GetDiskInfo())
'''
[6, 12, 1.4]
[15.92, 10.43, 5.49, 65.54]
[[0, 'C:\\', 475.64, 262.48, 213.16, 55.2], [1, 'D:\\', 510.77, 410.22, 100.55, 80.3], [2, 'E:\\', 400.0, 210.55, 189.45, 52.6]]
'''