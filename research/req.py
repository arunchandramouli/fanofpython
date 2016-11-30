import requests


'''
	An Example of parsing Ajax struck pages with Python Requests
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'_ga=GA1.2.1788499709.1480415218; _gat=1',
    'X-Requested-With': 'XMLHttpRequest'
}

URL = "https://www.sanwebe.com/assets/ajax-pagination-basic/"

session = requests.Session()
cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
data = session.get(URL,headers=headers,cookies=cookies)
print data.content

pages = {"page":2} # Run a For-Loop and address all pages
data = session.post(URL, data=pages, headers=headers)
print data.content