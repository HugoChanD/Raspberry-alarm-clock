import time
import os
import sys
from subprocess import call
from urllib 
import request, parse
import json
 

def jjr():
    showapi_appid="xxxxxxxxxx"  #替换此值
    showapi_sign="xxxxxxxxxx"   #替换此值
    url="http://route.showapi.com/894-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
     ,('day', "")
     
  ])

# When get up ?
h = 7
m = 10
 
loop = True
while(loop):
    # now
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
 
    # get up ?
    if h == hour and m == minute:
        return_code = call("/usr/bin/mpg123 我只在乎你.mp3", shell=True)
        loop = False
 
    # display current time
    timestr = "%04d-%02d-%02d %02d:%02d:%02d\r" \
            % (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5])
    sys.stdout.write(timestr)
    sys.stdout.flush()
    time.sleep(1)
    # end
