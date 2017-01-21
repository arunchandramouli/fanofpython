


from selenium import webdriver
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

pricing_area_wait = "//*[contains(@class,'pricingarea')]//span"

daily_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='day']//strong/text()"
daily_price_value = "//*[contains(@class,'pricingarea')]//*[@id='day']//b/text()"

weekly_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='week']//strong/text()"
weekly_price_value = "//*[contains(@class,'pricingarea')]//*[@id='week']//b/text()"

monthly_price_currency = "//*[contains(@class,'pricingarea')]//*[@id='month']//strong/text()"
monthly_price_value = "//*[contains(@class,'pricingarea')]//*[@id='month']//b/text()"

zipcode_enter = ".//*[@id='newzipcodecart']"
zipcode_enter_submit = ".//*[@class='newzipCart']"
zipcode_enter_click = "//*[@class='editBranch']//p[@class='sb-note-txt']"



def driver_window_handles(driver):

	print "Window"
	driver.find_element_by_xpath(zipcode_enter_click).click()
	time.sleep(3)

	driver.switch_to_window(driver.window_handles[0])
	print True
	driver.save_screenshot("True"+".png")
	driver.find_element_by_xpath(zipcode_enter_click).send_keys("10005")
	driver.find_element_by_xpath(zipcode_enter_submit).click()
	return




print geturl

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')

print driver

driver.get(geturl)

print driver.current_url

element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, wait_xpath)))



source = html.fromstring(driver.page_source.encode("utf-8"))

for elements in source.xpath(all_xpath):

	get_prd_url = base_url+elements
	driver.get(get_prd_url)
	element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, wait_xpath)))

	print driver.current_url

	'''
		Get Categories URL
	'''
	source = html.fromstring(driver.page_source.encode("utf-8"))
	for elementscats in source.xpath(categories):
		get_prd_url = base_url+elementscats

		driver.get(get_prd_url)
		element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, wait_xpath)))

		print driver.current_url

		driver_window_handles(driver)

		element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, wait_xpath)))

		source = html.fromstring(driver.page_source.encode("utf-8"))

		''' Find all Sub-Categories options'''
		for subcats in source.xpath(subcats):
			
			#Click on each element and find the price details

			if not subcats == "Select Equipment":
			
				driver.find_element_by_xpath(select_subcats%subcats).click()

				'''
					Get Sub-Categories List
				'''

				# Wait for the Pricing Area div to load
				element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, pricing_area_wait)))

				print 'Select'
				time.sleep(3)
				source = html.fromstring(driver.page_source.encode("utf-8"))
				time.sleep(3)

				print source.xpath(daily_price_value),source.xpath(daily_price_currency)
				print source.xpath(weekly_price_value),source.xpath(weekly_price_currency)
				print source.xpath(monthly_price_value),source.xpath(monthly_price_currency)

				driver.save_screenshot(subcats+".png")