
import scrapy
from lxml import html
import json
class GC_CAREERS(scrapy.Spider):
    name = "google"
    
    meta = {"t":"sq","li":"20","l":"false","j":"New%20York","jcoid":"7c8c6665-81cf-4e11-8fc9-ec1d6a69120c"}

    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125"
    }

    def start_requests(self):
        urls = ['https://careers.google.com/jobs/#jcoid=7c8c6665-81cf-4e11-8fc9-ec1d6a69120c&j=New+York&l=false&t=sq&li=20']

        for url in urls:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.parse)

    def parse(self, response):
    	get_source = html.fromstring(response.body.strip())
    	print get_source.xpath("//*[@class='sr-content']")
    	print response.url