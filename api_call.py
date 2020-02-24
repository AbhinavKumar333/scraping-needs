import requests
import json
import time
url = "https://ca-restapis.embibe.com/learning_objects"
querystring = {"event":"save","uuid":"a60043a4-c662-458e-ac49-77f8cc16a194"}
headers = {
    'Content-Type': "application/json",
    'Authorization': ""
    # 'User-Agent': "PostmanRuntime/7.20.1",
    # 'Accept': "*/*",
    # 'Cache-Control': "no-cache",
    # 'Postman-Token': "436453d8-a3e4-4f21-969b-74b679681b2e,3e8ecc2b-295d-4553-b67b-5b628998d5e6",
    # 'Host': "ca-restapis.embibe.com",
    # 'Accept-Encoding': "gzip, deflate",
    # 'Content-Length': "830",
    # 'Connection': "keep-alive",
    # 'cache-control': "no-cache"
    }

# file = 'scrapped content - rs-aggarwal-class-11-maths-solutions'
file = 'math-6'
jsonfile = open(file+'.json', 'r')
jsn = jsonfile.read().split('\n')
err=[]
okstat=[]
c=0
for j in jsn:
    if(j==""):
        break
    c+=1
    response = requests.request("POST", url, data=j, headers=headers, params=querystring)
    stat = response.text
    print stat
    r = json.loads(stat)
    # print(r)
    if(r['_status']=='OK'):
        okstat.append(r['id'])
    if(r['_status']=='ERR'):
        c-=1
        err.append(j)
    time.sleep(.1)
    print c
    # break
okjson = open(file+'.txt', 'w')
for ok in okstat:
    json.dump(ok, okjson)
    okjson.write('\n')

errjson = open('error.json', 'a')
for er in err:
    json.dump(er, errjson)
    errjson.write('\n')
