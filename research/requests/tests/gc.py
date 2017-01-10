import requests
from lxml import html
from selenium import webdriver
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

geturl = "https://careers.google.com/locations"

job_panel = ".//*[@id='job-search-form']/input[@class='page-header__job-search__input' and @type = 'search']"
page_xpath = "//*[@class='featured-wrapper']//div"
job_titles = "//*[@class='sr-content']//*[@class='sr-title text']/@title"
job_location = "//*[@class='sr-content-text']//*[@class='sr-content']//*[@class='summary']//*[contains(@class,'location')]/text()"

titles = "function(){ var names = document.getElementsByClassName('sr-title text'); for (var i = 0; i < names.length; i++){ console.log(names[i].getAttribute('title'))}}()"
driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')

print "Fetching url .... ",geturl
driver.get(geturl)


element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, job_panel)))



elem = driver.find_element_by_xpath(job_panel)
elem.send_keys("New York")
elem.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, page_xpath)))


''' Get Job-Related info'''
get_source = html.fromstring(driver.page_source)

for job_desg,job_loc in zip(get_source.xpath(job_titles),get_source.xpath(job_location)):

	print "DATA ==== ",job_desg,'******',job_loc


