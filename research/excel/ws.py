
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html

geturl = 'https://www.wayfair.com/careers'

careers_depts = ".//*[@id='career_tabs']/ul[@class='career_departments heading_font_reg fl']//li/a[contains(@href,'analytics')]"
wait_xpath = ".//*[@class='career_info fr']"

positions_click = ".//*[@id='business_intelligence_1']//a[contains(text(),'positions')]"

positions_click_wait = ".//*[@id='bd']"

job_details = ".//*[@id='bd']//*[@id='careers_opportunities']//*[@id='all_jobs']//*[@class='jobCat pos_rel margin_lg_bottom']"

job_post_href = "//*[@class='jobCat pos_rel margin_lg_bottom']//*[contains(@class,'job_row accent_divider')]/a/@href"
job_post_title = "//*[@class='jobCat pos_rel margin_lg_bottom']//*[contains(@class,'job_row accent_divider')]/a/text()"
job_post_loc = "//*[@class='jobCat pos_rel margin_lg_bottom']//*[contains(@class,'job_row accent_divider')]/span/text()"


print 'Driver'
millis = int(round(time.time() * 1000))
driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
millis1 = int(round(time.time() * 1000))

print 'Driver-1', millis1 - millis

millis = int(round(time.time() * 1000))
driver.get(geturl)
millis1 = int(round(time.time() * 1000))
print "TIME 1 ==== ", millis1 - millis

print driver.current_url

millis = int(round(time.time() * 1000))
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bd")))

millis1 = int(round(time.time() * 1000))
print 'Done'

print "TIME 2 ==== ", millis1 - millis


driver.execute_script("document.getElementById('careers_opportunities').style.display = 'career_opportunities_content careers_tab'")

with open("tests.html",'w') as writer:
	writer.write(driver.page_source.encode('utf-8'))