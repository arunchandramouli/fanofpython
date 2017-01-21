
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html

geturl = 'https://careers.google.com/locations/'

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantom2/phantomjs')
print True
driver.get(geturl)

print driver.page_source.encode('utf-8')
