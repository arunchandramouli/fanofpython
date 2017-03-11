
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

geturl = 'https://www.wayfair.com/careers#section=opportunities'

jobs_div = "//div[contains(@class,'job_row accent_divider')]"

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')

driver.get(geturl)

print driver.current_url

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bd"))
)

time.sleep(6)

#inner_html = driver.execute_script("return document.getElementsByClassName('jobCat pos_rel margin_lg_bottom')")

inner_html = driver.execute_script("return document.getElementsByClassName('fl jobTitle cleanlink wf_primarylighttext heading_font_reg')")

inner_html2 = driver.execute_script("return document.getElementsByClassName('fr jobLocation ltbodytext')")

for elements in inner_html:
	print elements.find_element_by_xpath("/text()"),'\n\n',elements.find_element_by_xpath("/@href")