
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import json
import re
geturl = 'https://careers.google.com/locations/'

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')


print "Fetch .... ",geturl

driver.get(geturl)
driver.set_window_size(1120, 550)
inits = ".//*[@id='init-locations']"

loc_list = ".//*[@class='location-map__overlay__location-list']//li//span//text()"

locs = ".//*[@class='location-map__overlay__location-list']//li//strong//text()"

loc_href = "//*[contains(@class,'content-container')]//*[@class='map-tabs']//li"

wait_path = "//*[@id='a11y-main']//*"

element = WebDriverWait(driver,100).until(
		EC.presence_of_all_elements_located((By.XPATH, wait_path)))

source = html.fromstring(driver.page_source.encode("utf-8"))


for elems in driver.find_elements_by_xpath(inits):

	get_container = elems.get_attribute("data-locations")
	data = json.dumps(get_container)
	get_Data = data.replace('"[','').replace('"]','')
	



print '\n\n'

fin_container = []

for elements in driver.find_elements_by_xpath(loc_href):

	elements.click()

	element = WebDriverWait(driver,100).until(
		EC.presence_of_all_elements_located((By.XPATH, ".//*[@class='location-map__overlay__location-list']//li//*")))

	element = WebDriverWait(driver,10).until(
		EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'content-container')]//*[@class='map-tabs']//li//*")))

	source = html.fromstring(driver.page_source.encode("utf-8"))
	
	for data in source.xpath(loc_list):
		if not "(" in str(data) or not ")" in str(data):
			fin_container.append(str(data).strip())


	for data in source.xpath(locs):
		if not "(" in str(data) or not ")" in str(data):
			fin_container.append(str(data).strip())
			
	time.sleep(2)


print len(fin_container)
for data in fin_container:
	print data