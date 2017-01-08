

import scrapy
from lxml import html


class QuotesSpider(scrapy.Spider):
    name = "walls"

    def start_requests(self):

        urls = ['https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465']

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        for url in urls:
            yield scrapy.Request(url=url, headers=headers,callback=self.parse)

    def parse(self, response):
        	
        	data = html.fromstring(response.body.strip())
        	prd_names = ".//*[@id='tile-container']//*[@class='js-product-title']//*[@class='tile-heading']/div/text()"
        	for prd_details in data.xpath(prd_names):

        		print prd_details.strip(),'\n\n'