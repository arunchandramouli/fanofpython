

import scrapy
from lxml import html
import re

class QuotesSpider(scrapy.Spider):
    name = "gcs"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    job_pos = "//*[@class='featured-wrapper']//*[@class='featured']//*[@class='srs']//*[@class='sr-title text']//span[@itemprop='name title']/text()"

    def start_requests(self):

        urls = ['https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&j=Hyderabad']


        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parse)

    def parse(self, response):

            data = html.fromstring(response.body.strip())
            print "data ==== ",data.xpath(self.job_pos)
            for posts in data.xpath(self.job_pos):
                print posts,'\n'
