
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
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
driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
print 'Driver-1'
x = datetime.datetime.now()
driver.get(geturl)

print "TIME ==== ", x - datetime.datetime.now()

print driver.current_url

x = datetime.datetime.now()
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bd")))

print 'Done'

print "TIME ==== ", x - datetime.datetime.now()

with open("tests.html",'w') as writer:
	writer.write(driver.page_source.encode('utf-8'))