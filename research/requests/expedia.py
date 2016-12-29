import requests
from lxml import html
from selenium import webdriver
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

geturl = 'https://expedia.wd5.myworkdayjobs.com/search'

jobs_outer_div = ".//*[@id='wd-FacetedSearchResultList-facetSearchResultList.jobProfile.data']/div[@class='WF0H WH-H']"

total_jobs = ".//*[@id='wd-FacetedSearchResultList-facetSearchResultList.jobProfile.data']/div[@class='WF0H WH-H']//ul//li[contains(@id,'wd-CompositeWidget-templatedListItem')]"

wait_xpath = ".//*[@id='wd-FacetedSearchResultList-facetSearchResultList.jobProfile.data']"

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')

total_jobs_count = "//span[@class='WP-H']//span[@class='gwt-InlineLabel WA0H WB0H']//text()"


driver.get(geturl)

print driver.current_url




element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,wait_xpath))
)


get_source = html.fromstring(driver.page_source)

count_jobs = int(get_source.xpath(total_jobs_count)[0].split(" ")[0])

print count_jobs

set_curr_jobs_pointer = 0

while  set_curr_jobs_pointer <= count_jobs:	

	
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	time.sleep(5)

	element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,wait_xpath))
	)

	get_source = html.fromstring(driver.page_source)


	set_curr_jobs_pointer = len(get_source.xpath(total_jobs))

