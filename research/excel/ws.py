

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import datetime

x = datetime.datetime.now()

geturl = 'https://www.wayfair.com/careers'

print geturl

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')

print driver

driver.get(geturl)

element = WebDriverWait(driver, 80).until(
    EC.presence_of_element_located((By.ID, "bd")))

print element


with open('driver2.html','w') as writer:

	writer.write(driver.page_source.encode('utf-8'))

print driver.execute_script("document.getElementById('careers_opportunities')")

print driver.execute_script("document.getElementById('careers_opportunities').innerHTML")


print datetime.datetime.now() - x


with open('driver.html','w') as writer:

	writer.write(driver.page_source.encode('utf-8'))