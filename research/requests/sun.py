
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import requests


# https://proxy-list.org/english/index.php
# http://proxylist.hidemyass.com/search-1291972#listable

service_args = [
    '--proxy=138.68.161.198:3128',
    '--proxy-type=https',
    ]


geturl = 'https://view-awesome-table.com/-KN_Cx0vVZhh-kH6WOPS/view'

print geturl

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
#driver = webdriver.Chrome('D:/Code/chromedriver')

print driver

driver.maximize_window()

driver.get(geturl)

print True

time.sleep(15)

print True

driver.save_screenshot("data.png")

print driver.current_url,'\n\n'
