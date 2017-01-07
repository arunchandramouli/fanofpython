
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


driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')

driver.get(geturl)

print driver.current_url

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bd"))
)



driver.find_element_by_xpath(careers_depts).click()


element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,wait_xpath))
)

print driver.current_url



driver.find_element_by_xpath(positions_click).click()


element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH,positions_click_wait))
)

print driver.current_url



get_source = html.fromstring(driver.page_source)

for divs in get_source.xpath(job_details):

	print divs.xpath(job_post_href),'\n\n',divs.xpath(job_post_title),'\n\n',divs.xpath(job_post_loc),'\n\n\n'