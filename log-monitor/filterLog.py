import datetime
import time
import sys

def convertDateTimeToUnixFormat(year,month,date,hour,min):
    date_time = datetime.datetime(year, month, date, hour, min)
    unix_time = int(time.mktime(date_time.timetuple()))
    return unix_time

def convertUnixTimeToDateTime(unix_time):
    unixToDatetime = datetime.datetime.fromtimestamp(unix_time) # Unix Time
    return unixToDatetime

def formatDate(input):
    slices=input.split()
    date=slices[0]
    time=slices[1]
    year,month,day = date.split('-')
    hour,min = time.split(':')
    return int(year),int(month),int(day),int(hour),int(min)

def binarySearch(ar,target):
    l=len(ar)
    lo=0
    hi=l-1
    while(lo<hi):
        m=lo+(hi-lo)//2
        if ar[m]<target:
            lo=m+1
        else:
            hi=m
    return lo


start_time=str(sys.argv[3])+" "+str(sys.argv[4])
end_time=str(sys.argv[5])+" "+str(sys.argv[6])
ip_address=sys.argv[1]
cpu_id=int(sys.argv[2])

DATA_PATH = sys.argv[7]+'/'
st_year,st_month,st_day,st_hour,st_min = formatDate(start_time)
et_year,et_month,et_day,et_hour,et_min = formatDate(end_time)
unix_st=convertDateTimeToUnixFormat(st_year,st_month,st_day,st_hour,st_min)
unix_et=convertDateTimeToUnixFormat(et_year,et_month,et_day,et_hour,et_min)
filepath=DATA_PATH+ip_address+".txt"
file1 = open(filepath,'r')
Lines = file1.readlines()
no_of_lines=len(Lines)
timeStampArr=[]
cpuUsageArr=[]
if cpu_id==0:
    for lineNumber in range(1,1441):
        linedata=Lines[lineNumber].split()
        timeStampArr.append(int(linedata[0]))
        cpuUsageArr.append(int(linedata[3]))
else:
    for lineNumber in range(1442,2882):
        linedata=Lines[lineNumber].split()
        timeStampArr.append(int(linedata[0]))
        cpuUsageArr.append(int(linedata[3]))
index1=binarySearch(timeStampArr,int(unix_st))
index2=binarySearch(timeStampArr,int(unix_et))
print("CPU"+str(cpu_id)+" usage on "+str(ip_address)+":")
s=''
for i in range(index1,index2):
    ti=str(convertUnixTimeToDateTime(timeStampArr[i]))[:-3]
    cpu_util=str(cpuUsageArr[i])
    s+="("+ti+","+cpu_util+"%),"
print(s[:-1])
