
import requests
from lxml import html
import json

    
meta = {"t":"sq","li":20,"l":"false","j":"New York","jcoid":"7c8c6665-81cf-4e11-8fc9-ec1d6a69120c"}

url = 'https://careers.google.com/jobs/#'
headers = {
'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
'upgrade-insecure-requests': "1",
'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125"
}

path = "//*[@class='srs']//*[@class='sr-content-container']//*[@class='sr-content-text']"
x = requests.get(url = url,headers=headers,params=meta)

newurl = x.url.replace("?","#")

x = requests.get(newurl.strip())

getdata = html.fromstring(x.content)

print x.url,'\n',newurl
print getdata.xpath(path)