import os
import sys
from subprocess import call
from urllib import    request, parse
import json
import random
#节假日数据
def jjrdate():
    showapi_appid = "apiid"  #appid
    showapi_sign = "api_sign"   #api_sign
    url="http://route.showapi.com/894-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
     ,('day', "")
     
  ])
 
    req = request.Request(url)
    with request.urlopen(req, data=send_data.encode('utf-8')) as f:
      str_res = f.read().decode('utf-8')
      svb_res = json.loads(str_res)
      date = svb_res["showapi_res_body"]
    return date
#闹钟
def aclock():
        
    jdate = jjrdate()
    gzr = int(jdate["type"])
#判断是否工作日
    if gzr == 1:
        return_code = call("/usr/bin/mpg123 ./music/music" + str(random.randint(1,4)) + ".mp3 ", shell=True)
if __name__=='__main__': 
    aclock()
