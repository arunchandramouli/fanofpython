import requests

'''URL = 'https://www.yourlibrary.ca/account/index.cfm'
payload = {
    'barcode': 'your user name/login',
    'telephone_primary': 'your password',
    'persistent': '1'  # remember me
}

session = requests.session()
r = requests.post(URL, data=payload)
print r.cookies

'''

URL = "https://yourlibrary.bibliocommons.com/search"

#http://stackoverflow.com/questions/12756443/fill-and-submit-html-form

payload = {
	
	'combox_doc_doctype':'AGREEMENT',
	'edt_fromm':'01',
	'edt_fromd':'01',
	'edt_fromy':'1800',

	'edt_tom':'01',
	'edt_tod':'01',
	'edt_toy':'2000',

}

load = {
	

	'q' : 'sciences',
	'sa': 'Go'
}

session = requests.session()
r = requests.post(URL, params=load,verify=False)

'''
	['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
	 '__getstate__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__',
	  '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', 
	  '_content_consumed', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 
	  'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'ok', 'raise_for_status', 'raw', 
	  'reason', 'request', 'status_code', 'text', 'url']
'''


print r.reason,'\n\n',r.json,'\n\n',r.request,'\n\n',r.status_code,'\n\n',r.text,'\n\n',r.url,'\n\n',r.content,'\n\n',r.connection,'\n\n',