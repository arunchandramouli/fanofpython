from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
import json
import csettings

x = datetime.datetime.now()


geturl = 'https://f5.com/careers/search-jobs?page=%s'

process_container = []

driver = webdriver.PhantomJS(executable_path='C:/PhantomJs/bin/phantom2/phantomjs')

page = -1

while True:

		page += 1

		curr_page = geturl%str(page)
		print "Processing %s "%curr_page

		driver.get(curr_page)

		element = WebDriverWait(driver,10).until(
		EC.presence_of_all_elements_located((By.XPATH, csettings.wait_xpath_search)))

		if driver.find_elements_by_xpath(csettings.quit_xpath):

			print "Process Completed"
			break


		element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.XPATH, csettings.wait_xpath)))

		getsource = html.fromstring(driver.page_source.encode("utf-8").strip())


		for job_url, job_desg,job_dept,job_loc,job_date_posted in zip(getsource.xpath(csettings.job_url),
			getsource.xpath(csettings.job_desg),getsource.xpath(csettings.job_dept),
			getsource.xpath(csettings.job_loc),getsource.xpath(csettings.job_date_posted)):        

			print {"job_url":job_url,"job_desg":job_desg,"job_dept":job_dept,"job_loc":job_loc,"job_date_posted":job_date_posted},'\n\n'

			with open('results.html','a') as code:

				code.write(json.dumps({"job_url":job_url,"job_desg":job_desg,"job_dept":job_dept,"job_loc":job_loc,"job_date_posted":job_date_posted}))
				code.write("\n")
				process_container.append({"job_url":job_url,"job_desg":job_desg,"job_dept":job_dept,"job_loc":job_loc,"job_date_posted":job_date_posted})
