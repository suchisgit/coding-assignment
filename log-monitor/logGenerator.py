from random import randint
import datetime
import time
import csv
import sys

def generateValidThousandIPs():
    ips=[]
    defaultPortionOfIp='192.168.'
    for thrirdPart in range(1,5):
        for fourthPart in range(1,256):
            if thrirdPart == 4 and fourthPart>235:
                break
            ipaddress = defaultPortionOfIp+str(thrirdPart)+'.'+str(fourthPart)
            ips.append(ipaddress)
    return ips

def populateFileOneDayData(year,month,date,ips):
    start_time=datetime.datetime.now()
    column_names=['Timestamp','IP','cpu_id','usage']
    for ip in ips:
        path = DATA_PATH+str(ip)+".txt"
        fo=open(path,"w+")
        fo.write("cpu-0 \n")
        for hour in range(0,24):
            for min in range(0,60):
                date_time = datetime.datetime(year, month, date, hour, min)
                unix_time = int(time.mktime(date_time.timetuple()))
                fo.write(str(unix_time)+" "+str(ip)+" "+str(0)+" "+str(randint(0, 100))+"\n")
        fo.write("cpu-1 \n")
        for hour in range(0,24):
            for min in range(0,60):
                date_time = datetime.datetime(year, month, date, hour, min)
                unix_time = int(time.mktime(date_time.timetuple()))
                fo.write(str(unix_time)+" "+str(ip)+" "+str(1)+" "+str(randint(0, 100))+"\n")
        print("File Created..."+str(path))

    end_time=datetime.datetime.now()

print("Hello!!!")
DATA_PATH = sys.argv[1] + '/'
thousand_ips=generateValidThousandIPs()
year=2014
month=10
date=31
populateFileOneDayData(year,month,date,thousand_ips)
