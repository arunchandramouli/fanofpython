
import scrapy

from scrapy.http import FormRequest
import csettings

import time
from lxml import html
import datetime


base_url = "https://www.hercrentals.com"


collections_mapper = []

class Herc(scrapy.Spider):

    name = "jappy"

    def start_requests(self):
    	
        urls = ['https://f5.com/careers/search-jobs']

        for process_url in urls:
        	yield scrapy.Request(url=process_url,callback=self.automate)


    def automate(self,response):

    	print response ,response.url

    	get_source = html.fromstring(response.body.strip())

    	self.extract(get_source)



    def extract(self,get_source):

    	print get_source.xpath(csettings.job_url)
    	print get_source.xpath(csettings.job_desg)
    	print get_source.xpath(csettings.job_dept)
    	print get_source.xpath(csettings.job_loc)
    	print get_source.xpath(csettings.job_date_posted)