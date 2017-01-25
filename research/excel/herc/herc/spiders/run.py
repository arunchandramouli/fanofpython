
import scrapy

from scrapy.http import FormRequest


from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import datetime

geturl = 'https://www.hercrentals.com/content/herc/en/rentals.html'

base_url = "https://www.hercrentals.com"

all_elements = ".img-responsive.center-block"

all_xpath = "//*[contains(@class,'col-xs') and contains(@class,'col-sm') and contains(@class,'col-md') and contains(@class,'col-lg')]/a/@href"

categories = "//*[contains(@class,'col-xs') and contains(@class,'col-sm') and contains(@class,'col-md') and contains(@class,'col-lg') and contains(@class,'div_btn_col')]/a/@href"
subcats = "//*[@class='row']//*[@class='cstmDropDwn']//*[@id='specscatclass']//option/text()"
select_subcats = "//*[@class='row']//*[@class='cstmDropDwn']//*[@id='specscatclass']//option[text() ='%s']"


wait_xpath = "//*[@class='row']"

pricing_area_wait = "//*[contains(@class,'pricingarea')]//span//*"

daily_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='day']//strong/text()"
daily_price_value = "//*[contains(@class,'pricingarea')]//*[@id='day']//b/text()"

weekly_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='week']//strong/text()"
weekly_price_value = "//*[contains(@class,'pricingarea')]//*[@id='week']//b/text()"

monthly_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='month']//strong/text()"
monthly_price_value = "//*[contains(@class,'pricingarea')]//*[@id='month']//b/text()"

zipcode_enter = "//*[@class='row']//*[@class='editBranch']//*[@class='sb-note-txt']"
modal_dialog_wait = "//*[@class='newzipCart']"

zipcode_enter_submit = "//*[@id='myModalCart']//*[@class='modal-dialog']//*[@class='modal-content']//*[@class='form-group']//*[@class='newzipCart']"
zipcode_enter_click = "//*[@id='myModalCart']//*[@class='modal-dialog']//*[@class='modal-content']//*[@class='form-group']//*[@id='newzipcodecart']"

test_zipcodes = ["75201"]

collections_mapper = []

class Herc(scrapy.Spider):
    name = "jappy"

    def start_requests(self):

    	test = {"startDate":"012417","endDate":"013117","equipCatg":"410","equipClass":"2010","equipQty":"1","ZipCode":"10005"}

        urls = ['https://www.hercrentals.com/content/herc/en/rentals.html']

        print len(self.explore())

    def explore(self):


		driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')

		driver.get(geturl)


		element = WebDriverWait(driver, 80).until(
		    EC.presence_of_element_located((By.XPATH, wait_xpath)))

		source = html.fromstring(driver.page_source.encode("utf-8"))

		for elements in source.xpath(all_xpath):

			get_prd_url = base_url+elements
			driver.get(get_prd_url)
			element = WebDriverWait(driver, 30).until(
		    EC.presence_of_element_located((By.XPATH, wait_xpath)))

			equiment_type = elements.split("/")[-1].replace(".html","").strip()

			'''
				Get Categories URL
			'''
			source = html.fromstring(driver.page_source.encode("utf-8"))
			for elementscats in source.xpath(categories):

				elementscats_sub = elementscats.split("/")[-1].replace(".html","").strip()

				get_prd_url = base_url+elementscats

				driver.get(get_prd_url)
				element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, wait_xpath)))

				for each_zip_code in test_zipcodes:

					element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, wait_xpath)))

					source = html.fromstring(driver.page_source.encode("utf-8"))

					''' Find all Sub-Categories options'''

					try:
						for subcats in source.xpath(subcats):

							#Click on each element and find the price details

							if not subcats == "Select Equipment":

								time.sleep(1)
								
								collections_mapper.append({"Equipment_Type":equiment_type,"Equipment_Category":elementscats_sub,
									"Equipment_sub_cat":subcats,"Zip_Code":each_zip_code})

					except Exception as E:

						continue

		return collections_mapper