import requests
from lxml import html
from selenium import webdriver
import mechanize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




exp = "https://expedia.wd5.myworkdayjobs.com/search"

job_panel = "//div[contains(@id,'wd-FacetedSearchResultList')]"



title = "//div[contains(@role,'region')]//div[contains(@class,'WF0H WH-H')]//li[contains(@class,'WI3C WG0H')]//span[contains(@class,'gwt-InlineLabel')]//text()"


#gwt-Label WGKI

title_val = "//div[contains(@role,'region')]//div[contains(@class,'WF0H WH-H')]//li[contains(@class,'WI3C WG0H')]//span[contains(@class,'gwt-Label WGKI')]//text()"

wait_xpath = "//*[contains(@id,'wd-FacetedSearchResultList')]"

geturl = "https://expedia.wd5.myworkdayjobs.com/search"

driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')

driver.get(geturl)

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, wait_xpath)))



ht = html.fromstring(driver.page_source)

print ht.xpath(title),'\n\n',ht.xpath(title_val),'\n\n'

