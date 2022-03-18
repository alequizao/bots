import json
import sys
import requests 
import time
import os
url = 'http://78.47.38.152'
user = 'alequizao'
password = 'feliz1454'

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

data={
'id':000,
'attributes':{},
'groupId':0,
'name':'',
'uniqueId':'ALEX',
'status':'',
'lastUpdate':'',
'positionId':'',
'geofenceIds':[],
'phone':'',
'photo':'',
'placa':'',
'model':'',
'contact':'',
'category':'',
'disabled':''
}

payload = {'all': 'true', 'name': 'MARIA'}
response = requests.get(url + ':8082/api/devices', auth=(user, password),headers=headers, params=payload, timeout=100.000).content
print(response)
ddd = json.loads(response)[0:]
#while True:  

  #print(f"Placa: {i['name']}", ' - ', 'Status: ',i['status'])
  #print(f"{i['name']}",",",f"{i['status']}")


while True:
  for i in ddd:
    x = f"Placa: {i['name']}"
    arquivo = open('testando.html', 'a+') #abre o arquivo
    center = '<center>'
    p = '<bp>'
    pf = '</b>'
    ab = f"\nPlaca: {p} {i['name']}{pf}"
    cd = f" - Status: {p} {i['status']}{pf}"
    br = '<br>'
    ee = ab+cd+br
    arquivo.write(ee)
    arquivo.close()
    time.sleep(5)

os.system("cls")
