

import scrapy
from lxml import html
import re

class QuotesSpider(scrapy.Spider):
    name = "walls"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):

        urls = ['https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465']


        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parse)

    def parse(self, response):

            data = html.fromstring(response.body.strip())
            final_href = data.xpath(".//*[@id='paginator-container']/div/ul/li[last()]/a/@href")[0]
            no_pages = int(re.search("page=(.+?)&",final_href).group(1))

            group_url = "https://www.walmart.com/browse/auto-tires/car-truck-tires/91083_1077064_1063465?page=%s"

            for page_num in xrange(1,2):
                yield scrapy.Request(url = group_url%page_num, headers=self.headers,callback=self.prd_details)


    def prd_details(self,response):


            data = html.fromstring(response.body.strip())
            prd_names = ".//*[@id='tile-container']//*[@class='js-product-title']//*[@class='tile-heading']/div/text()"
            prd_price = ".//*[@id='tile-container']//*[@class='tile-price']//*[@class='price price-display']/text()[normalize-space()]"
            prd_price_post_decimal = ".//*[@id='tile-container']//*[@class='tile-price']//*[@class='price price-display']//*[@class='sup'][last()]/text()[normalize-space()]"
            price_curr = ".//*[@id='tile-container']//*[@class='tile-price']//*[@class='price price-display']//*[@class='sup'][last()-1]/text()[normalize-space()]"

            for prd_details,price_details,prd_price_post_decimals,curr in zip(data.xpath(prd_names),data.xpath(prd_price),data.xpath(prd_price_post_decimal),data.xpath(price_curr)):

                print prd_details.strip(),'\n',price_details.strip()+"."+prd_price_post_decimals.strip()+curr.strip(),'\n\n'
