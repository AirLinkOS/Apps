#!/usr/bin/env python

import time,datetime,json
import http.client,ssl
from urllib.parse import urlparse

AOS_HOST = "https://192.168.1.1"
AOS_USER = 'apiuser'
AOS_PWD  = #TODO: define a password for REST API user
CONFIG_FILE = '/config/data.json'

def logMessage(message="", trace=False):
   print("%s: %s" % (time.asctime(), message))

def parseConfig():
   getData = []
   setData = {}
   try:
      conf_file = open(CONFIG_FILE)
      config = json.load(conf_file, strict=False)
      conf_file.close()
   except:
      logMessage('Failed to read config file at path: %s', CONFIG_FILE)
      exit(-1)
   if config:
      logMessage('Found config file with contents: ' + str(config))
      getData = config['get']
      setData = config['set']
   else:
      logMessage('Failed to parse config file')
      exit(-1)
   return getData, setData

'''
  a helper function to perform the REST request for auth, get, and set operations.
'''
def doHttp(host, url, body, headers):
    url_info = urlparse(host)
    if url_info.scheme == "https":
        context = ssl._create_unverified_context()
        con = http.client.HTTPSConnection(url_info.netloc, 443,  context=context, timeout=5)
    else:
        con = http.client.HTTPConnection(url_info.netloc, 80)

    try: 
       con.request("POST", url, body, headers)
       response = con.getresponse()
       data = response.read()
       #logMessage(response.status)       
       return data
    finally:
        con.close() 

def doAuth():
   headers = {
      'accept': 'application/vnd.api+json',
      'Content-Type': 'application/vnd.api+json'
   }

   url = '/api/v1/auth/tokens'
   data = { "login": AOS_USER ,  "password": AOS_PWD}
   json_body = json.dumps(data) 
   result = doHttp(AOS_HOST, url, json_body, headers)
   dict_data = json.loads(result)
   token=dict_data["data"]["access_token"]
   logMessage(token)
   return(token)

def doGet(auth, getData): 
   suffix = 'Bearer ' + str(auth)
   headers = {
      'Authorization' : suffix,
      'accept': 'application/vnd.api+json',
      'Content-Type': 'application/vnd.api+json'
   }
   url = '/api/v1/db/get'
   data = [ { "fields": getData }]
   json_body = json.dumps(data) 
   result = doHttp(AOS_HOST, url, json_body, headers)
   dict_data = json.loads(result)   
   logMessage('/api/v1/db/get results:')
   logMessage(json.dumps(dict_data, indent=2))

def doSet(auth, setData):
   suffix = 'Bearer ' + str(auth)
   headers = {
      'Authorization' : suffix,
      'accept': 'application/vnd.api+json',
      'Content-Type': 'application/vnd.api+json'
   }
   url = '/api/v1/db/set'
   data = [{"values": setData}]
   json_body = json.dumps(data) 
   result = doHttp(AOS_HOST, url, json_body, headers)
   dict_data = json.loads(result)
   logMessage('/api/v1/db/set results:')
   logMessage(json.dumps(dict_data, indent=2))
   
def runtest():
   getData, setData = parseConfig()
   authtoken = doAuth()
   if getData:
      doGet(authtoken, getData)
   if setData:
      doSet(authtoken, setData)   
    
if __name__ == "__main__":
    runtest()
