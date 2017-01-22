

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

pricing_area_wait = "//*[contains(@class,'pricingarea')]//span"

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

test_zipcodes = ["77022","75201","30303","10022","10005"]


optionschrome = webdriver.ChromeOptions()
optionschrome.add_argument("--start-maximized")




def driver_window_handles(driver,zipcode_enter_field):


		try:
			driver.find_element_by_xpath(zipcode_enter).click()
		except Exception:
			pass

		time.sleep(7)
		print driver.save_screenshot("tests1.png")
		driver.switch_to_window(driver.window_handles[0])	
		#driver.switch_to_alert()
		
		print driver.save_screenshot("tests.png")
		element = WebDriverWait(driver, 80).until(
		EC.visibility_of_element_located((By.XPATH, modal_dialog_wait)))

		hov = ActionChains(driver).move_to_element(element)
		hov.perform()

		driver.find_element_by_xpath(zipcode_enter_click).click()
		driver.find_element_by_xpath(zipcode_enter_click).send_keys(zipcode_enter_field)
		driver.find_element_by_xpath(zipcode_enter_submit).click()
		return

print geturl

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')
#driver = webdriver.Chrome('C:/Users/Home/Documents/chromedriver',chrome_options=optionschrome)


driver.get(geturl)


element = WebDriverWait(driver, 80).until(
    EC.presence_of_element_located((By.XPATH, wait_xpath)))


source = html.fromstring(driver.page_source.encode("utf-8"))

for elements in source.xpath(all_xpath):

	get_prd_url = base_url+elements
	driver.get(get_prd_url)
	element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, wait_xpath)))

	equiment_type = elements.split("/")[-1].strip()

	'''
		Get Categories URL
	'''
	source = html.fromstring(driver.page_source.encode("utf-8"))
	for elementscats in source.xpath(categories):

		elementscats_sub = elementscats.split("/")[-1].strip()

		get_prd_url = base_url+elementscats

		driver.get(get_prd_url)
		element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, wait_xpath)))

		for each_zip_code in test_zipcodes:

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
					time.sleep(1)
					source = html.fromstring(driver.page_source.encode("utf-8"))
					time.sleep(1)

					print equiment_type, elementscats_sub,subcats, each_zip_code, source.xpath(daily_price_value),source.xpath(daily_price_currency)
					print equiment_type, elementscats_sub,subcats,each_zip_code, source.xpath(weekly_price_value),source.xpath(weekly_price_currency)
					print equiment_type, elementscats_sub,subcats,each_zip_code, source.xpath(monthly_price_value),source.xpath(monthly_price_currency)