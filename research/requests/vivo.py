
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import requests


geturl = 'http://www.sunbeltgear.com/Browse/SearchResults.aspx?'



driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
#driver = webdriver.Chrome("D:/Code/chromedriver")

url = "https://www.vivo.com.br/portalweb/appmanager/env/web#"

driver.get(url)

time.sleep(2)
#driver.set_window_size(1400,1000)
driver.maximize_window()
