
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
#driver.set_window_size(1920, 1080)
#driver.set_window_size(1124, 850)

time.sleep(2)

load_content = "//*[@class='content']"


basic_modal = "//*[contains(@class,'bg_center_modal')]//*[@class='bg_campo']//*[@id='campoRegional' and @type ='text']"

select_drp = "//*[contains(@class,'bg_center_modal')]//*[@id='box_scroll']//*[@class='viewport']//li/a[@class='ui-corner-all-custom']"

select_btn_no = "//*[contains(@class,'bg_center_modal')]//*[@class='lista_bt']//a[@class='bt_cliente_n']"

vivo_control = "//*[@class='content']//*[@class='noClass']//*[@class='vivo_tem']//*[@class='vivo_tem_movel']//*[@class='vtm_item']//*[@class='vtm_item_controle']"

selection_submit_wait_bfr_frame = "//*[@class='modal-dialog']//*[@class='modal-content']"

selection_submit_wait = "//*[@id='myModal']//*[@class='modal-dialog']//*[@class='modal-content']"

selection_submit = "//*[@id='myModal']//*[@class='modal-dialog']//*[@class='modal-content']//*[@class='modal-body']//*[@class='estado']//*[@id='formUfDdd']//*[@type='submit' and @id ='btnSubmitDDDUF']"

main_wait = "//*[@id='vivoBookPrincipal']//*"

cdModal_iframe = "//*[@id='cdModal']/iframe"

print "LOAD .... "

element = WebDriverWait(driver, 200).until(
	    EC.presence_of_element_located((By.XPATH, load_content)))



with open("vivo1.html","w") as writer:
	writer.write(driver.page_source.encode("utf-8").strip())


print driver.current_url

time.sleep(5)

print "LOAD 1.... "

driver.save_screenshot("data.png")

driver.find_element_by_xpath(basic_modal).send_keys("Sao Paulo")

time.sleep(5)

print "LOAD 2.... "

driver.save_screenshot("data1.png")

driver.find_element_by_xpath(select_drp).click()

element = WebDriverWait(driver, 20).until(
	    EC.presence_of_element_located((By.XPATH, select_btn_no)))

time.sleep(2)

print "LOAD 3.... "

driver.save_screenshot("data2.png")

driver.find_element_by_xpath(select_btn_no).click()

element = WebDriverWait(driver, 20).until(
	    EC.presence_of_element_located((By.XPATH, load_content)))

print "load_content"

element = WebDriverWait(driver, 50).until(
	    EC.presence_of_element_located((By.XPATH, main_wait)))

print "main_wait"

time.sleep(2)

print "LOAD 4.... "

driver.save_screenshot("data3.png")

driver.find_element_by_xpath(vivo_control).click()


time.sleep(2)

print "LOAD 5.... "

driver.save_screenshot("data4.png")



element = WebDriverWait(driver, 50).until(
	    EC.presence_of_element_located((By.XPATH, selection_submit_wait_bfr_frame)))


time.sleep(2)

print "LOAD 6.... "

driver.save_screenshot("data5.png")

time.sleep(5)


driver.switch_to.frame(driver.find_element_by_xpath(cdModal_iframe))

time.sleep(5)

print "LOAD 6.1 "
driver.save_screenshot("data5_1.png")

time.sleep(2)

									
driver.find_element_by_xpath(selection_submit).click()

print "LOAD 7.... "

driver.save_screenshot("data6.png")

with open("viv2.html","w") as writer:
	writer.write(driver.page_source.encode("utf-8").strip())

driver.quit()