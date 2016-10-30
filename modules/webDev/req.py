
'''
	Aim :: Using requests module for REST - Representational State Transfer

'''

import requests, httplib


r = requests.get('https://api.github.com/events')

'''
	'json', 'links', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'
'''

print r.json, '\n',r.links, '\n',r.ok, '\n',r.raise_for_status(), '\n',r.raw, '\n',r.request, '\n',r.status_code,'\n',r.url, '\n\n'


payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print r.url, '\n\n ',r.text , '\n\n ', r.encoding

params = {'arun':'Gold','Kumar':'C'}

r = requests.post('http://httpbin.org/post', data = params)

r = requests.get('http://httpbin.org/get', params=params)

print r.json(), '\n\n' ,

r = requests.get('http://httpbin.org/get')

print r.json()