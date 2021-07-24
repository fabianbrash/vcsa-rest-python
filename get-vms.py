import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from operator import length_hint

vc_name = 'vc'
vc_user = 'user'
vc_pass = 'pass'

s=requests.Session()
s.verify=False

app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "https://localhost:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/v1/vms")
def return_vms():
    get_vc_session(vc_name,vc_user,vc_pass)
    resp = get_vms(vc_name)
    data = json.loads(resp.text)
    return data

# Lets get our token

def get_vc_session(vc_name,vc_user,vc_pass):
    s.post('https://'+vc_name+'/rest/com/vmware/cis/session',auth=(vc_user,vc_pass))
    return s

def get_vms(vc_name):
    vms=s.get('https://'+vc_name+'/rest/vcenter/vm')
    return vms

#get_vc_session(vc_name,vc_user,vc_pass)

#res = get_vms(vc_name)

#allvms = json.loads(res.text)

#print(allvms)

#print(len(allvms['value']))

# Lets try and loop through all of them

#for i in allvms['value']:
  #print(i)
  #print('Name:'+i['name']+' CPU Count:',i['cpu_count'])
  #print(f"Name: {i['name']} CPU Count: {i['cpu_count']} Power State: {i['power_state']} Memory(GB): {(i['memory_size_MiB'])/1024}")
