
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html

geturl = 'https://jobs.wayfaircareers.com/jobs?page=%s'

baseurl = "https://jobs.wayfaircareers.com"

page_wait = "//*[contains(@class,'search-resu')]//*[contains(@class,'job-search') and contains(@class,'container')]//*[contains(@class,'job-result')]//*"
job_position = "//*[contains(@class,'job-result')]//*[@class='job-information']//*[contains(@class,'job-result')]/h4/a/span/text()"
job_href = "//*[contains(@class,'job-result')]//*[@class='job-information']//*[contains(@class,'job-result')]/h4/a/@href"
job_loc = "//*[contains(@class,'job-result')]//*[@class='job-information']//*[contains(@class,'job-result') and contains(@class,'location')]/p/span[contains(@id,'job-location')]/text()"
job_category = "//*[contains(@class,'job-result')]//*[@class='job-information']//*[contains(@class,'job-result') and contains(@class,'category')]/p/span[contains(@itemprop,'occupational')]/text()"

next_page = ".//*[@id='pagination-container']/ul[contains(@class,'pagination')]/li/a[contains(@class,'page-link')]"
icon_arrow = ".//*[@id='pagination-container']/ul[contains(@class,'pagination')]/li/a[contains(@class,'page-link')]//span[contains(@class,'icon-arrow')]"
arrow_disabled = ".//*[@id='pagination-container']/ul[contains(@class,'pagination')]/li[contains(@class,'disabled')]//span[contains(@class,'next')]//span[contains(@class,'icon-arrow')]"
total_jobs = "//*[@class='search-meta']//*[@id='search-results-indicator']/text()"


driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
driver.maximize_window()
collections_mapper= []




def traverse_all_pages():

	curr_page_no = 1

	while True:

		driver.get(geturl%str(curr_page_no))
		
		print driver.current_url

		time.sleep(4)
		
		element = WebDriverWait(driver, 10).until(
		    EC.presence_of_all_elements_located((By.XPATH,page_wait))
		)
		print True,"\n\n"

		get_source = html.fromstring(driver.page_source.encode("utf-8").strip())


		for position,job_url,getjob_loc,job_cat in zip(get_source.xpath(job_position),get_source.xpath(job_href),get_source.xpath(job_loc),get_source.xpath(job_category)):

			try:	

				ref_id = job_url.split("/")[-1].strip()

				get_data_jobs = {"Position":position.strip(),"URL":str(baseurl)+str(job_url),"RefID":ref_id,"Location":getjob_loc,"Category":job_cat}
				print get_data_jobs,"\n\n"
				collections_mapper.append(get_data_jobs)

			except Exception as E:
				print E
				continue			

		curr_page_no += 1

		if driver.find_elements_by_xpath(arrow_disabled):

			print "All Pages Processed and job Information had been extracted! "
			break



if __name__ == "__main__":

	traverse_all_pages()

