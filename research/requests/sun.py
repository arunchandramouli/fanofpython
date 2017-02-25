
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


geturl = 'https://www.ubereats.com/chicago/'

print geturl

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs',service_args=service_args)
#driver = webdriver.Chrome('D:/Code/chromedriver')

print driver

driver.maximize_window()

driver.get(geturl)

print True

time.sleep(15)

print True

driver.save_screenshot("data.png")

print driver.current_url,'\n\n'


driver.execute_script("document.getElementById('address-selection-input').click()")
driver.execute_script("document.getElementById('address-selection-input').click()")

driver.execute_script("document.getElementById('address-selection-input').value = 'chicago'")
driver.execute_script("document.getElementById('address-selection-input').value = 'chicago'")

driver.find_element_by_xpath("//*[contains(@id,'address-selection-input')]").send_keys("San Francisco")
time.sleep(10)

#driver.execute_script("document.getElementById('address-selection-input').click()")
#driver.execute_script("document.getElementById('address-selection-input').click()")

time.sleep(10)
driver.save_screenshot("data1.png")
time.sleep(4)

print "Button Click "

get_drp_values = driver.find_elements_by_xpath("//*[contains(@class,'dropdown')]//*[contains(@class,'base')]/a[contains(@class,'prediction')]")

get_drp_values[0].click()

#driver.execute_script("document.getElementsByClassName('submitButton_2QnNsD btn btn--primary text-input--joined')[0].click()")
#driver.find_element_by_xpath("//*[contains(@class,'submitButton') and @type='submit']").click()
#driver.find_element_by_xpath("//*[contains(@class,'submitButton') and @type='submit']").click()

time.sleep(15)
driver.save_screenshot("data1.png")

print driver.current_url
#driver.quit()



with open("itwillwork.html","w") as writeme:
	writeme.write(driver.page_source.encode("utf-8").strip())
