import requests
from common_function import CommonFunction
from pprint import pprint
import json


searchwhat =  input('What To Snatch?')
searchkey = input('From Who?')

if searchwhat == 'usertaglist':
    if searchkey is not None and searchkey != '':
        apikey =CommonFunction().fetch_cur_apikey()
        url="http://127.0.0.1:8889/instapi/v2.0/GetUserTag"
        insta_id = '0000000001'
        headers = {'content-type': 'application/json'}
        dict_request = {
        "token":apikey,
        "insta_id":insta_id,
        "searchkey":searchkey
        }
        timeout=40

        response =requests.post(url, json.dumps(dict_request), timeout=timeout, headers=headers, verify=False)
        pprint(response.status_code)
        pprint(response.json())
    else:
        print("Warning nothing To Snatch")

elif searchwhat == "usermedia":
    if searchkey is not None and searchkey != '':
        apikey =CommonFunction().fetch_cur_apikey()
        url="http://127.0.0.1:8889/instapi/v2.0/GetUserMedia"
        insta_id = '0000000001'
        headers = {'content-type': 'application/json'}
        dict_request = {
        "token":apikey,
        "insta_id":insta_id,
        "searchkey":searchkey
        }
        timeout=40

        response =requests.post(url, json.dumps(dict_request), timeout=timeout, headers=headers, verify=False)
        pprint(response.status_code)
        pprint(response.json())
    else:
        print("Warning nothing To Snatch")

elif searchwhat == "tagmedia":
    if searchkey is not None and searchkey != '':
        apikey =CommonFunction().fetch_cur_apikey()
        url="http://127.0.0.1:8889/instapi/v2.0/GetTagMedia"
        insta_id = '0000000001'
        headers = {'content-type': 'application/json'}
        dict_request = {
        "token":apikey,
        "insta_id":insta_id,
        "searchkey":searchkey
        }
        timeout=40

        response =requests.post(url, json.dumps(dict_request), timeout=timeout, headers=headers, verify=False)
        pprint(response.status_code)
        pprint(response.json())
    else:
        print("Warning nothing To Snatch")
else:
    print("specify what to search if usermedia or userlist")