
import sys
import datetime

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import logging

'''
	Logging Facilities
'''

logging.basicConfig(level=logging.INFO)
core_logger = logging.getLogger("Citadel")

baseurl = "https://sites.google.com/site/gamedatalibrary/software-by-year/"



'''
	Xpath for extracting games related information
'''

page_load = "//*[@id='body']//*"

page_load_games_full_content = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']/div/a[1]"

iframe_game_data = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']//*[contains(@class,'sites-embed-content')]/iframe"

iframe_body = "//*[@dir='ltr']//*"

inner_iframe_awesome_table = "//*[@dir='ltr']//*[contains(@class,'tabcontent')]/iframe"


inner_iframe_awesome_table_middle_container = "//*[@id='middleContainer']//table//tr//td"

inner_iframe_awesome_table_rows = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//tbody/tr[contains(@class,'google-visualization-table')]"


inner_iframe_awesome_table_rows_curr_td = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//tbody/tr[contains(@class,'google-visualization-table')][%s]/td"


inner_iframe_awesome_table_headers = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//thead/tr/th[contains(@class,'google-visualization-table')]"

inner_iframe_awesome_table_rows_count_1 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[1]"

inner_iframe_awesome_table_rows_count_2 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[2]"

inner_iframe_awesome_table_rows_count_3 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[3]"

inner_iframe_awesome_table_rows_pag_next = "//*[@id='middleContainer']//*[@id='count']//*[@id='pagination']//*[contains(@class,'goog-inline')]//*[@class='google-visualization-table-page-next']"

collections_mapper= []

table_mapper = []


def get_list_urls_to_process(driver,page_source_lxml):

	try:

		url_container = []

		for each_href in driver.find_elements_by_xpath(page_load_games_full_content):			
			url_container.append(each_href.get_attribute("href"))
		return url_container

	except Exception as E:
		core_logger.critical(E)
		return []



def launch_driver():

	try:

		driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
		driver.maximize_window()

		return driver

	except Exception as E:
		raise Exception(E)
		



def get_prd_year(prd_url):

	'''
		Parameters
			prd_url -> Full URL . Ex - https://sites.google.com/site/gamedatalibrary/software-by-year/1995-weekly

		return
			Year part -> 1995
	'''


	try:

		return str(prd_url).split("/")[-1].split("-")[0].strip()


	except Exception as E:

		core_logger.critical("Cannot fetch Product Year for Product URL %s "%prd_url)

		return None



''' 
	For a given year , return an array of week start dates - It should return an array of all weeks in an year
'''
def determine_week_start_dates(total_weeks ,year_of_product,array_of_weeks = []):

	
	'''
		Parameters

			total_weeks -> Total no. weeks given in the Table
			year_of_product -> Product Release year

		return

			-> an array of week start dates - It should return an array of all weeks in an year
	'''

	''' Make sure to make it void each time the function is called '''

	if not array_of_weeks == [] : array_of_weeks = []

	set_start_year = datetime.date(int(year_of_product),1,1)

	for each_week_number in range(1,total_weeks+1):

		array_of_weeks.append(set_start_year + datetime.timedelta(weeks=int(each_week_number)))

	return array_of_weeks





def fetch_game_iframe_src(driver,href_list):


	'''
		Parameters
			driver -> Webdriver
			href_list -> The List of URLs to process 
		Yield
			The HREF of outer main iframe
			
	'''




	'''
		Go to each href and obtain game related information
	'''

	for each_href in href_list:

		try:

			core_logger.info("Fetching product page  .... %s "%each_href)

			core_logger.info("\n\n\n\n")

			get_prd_year_val = get_prd_year(each_href)

			setattr(sys.modules[__name__],'get_prd_year_val',get_prd_year_val)

			core_logger.info("Fetching product page based on year .... %s "%get_prd_year_val)

			core_logger.info("\n\n\n\n")			

			driver.get(each_href)

			element = WebDriverWait(driver, 100).until(
			EC.presence_of_element_located((By.XPATH,page_load)))

			iframe_contents = driver.find_element_by_xpath(iframe_game_data).get_attribute("src")

			yield iframe_contents


		except Exception as E:

			core_logger.critical("Exception on processing URL %s "%each_href)
			core_logger.critical (E)
			core_logger.critical("Processing Next ... ")
			continue


'''
	Load the main Iframe
'''
def load_iframe_game(driver,iframe_contents):


	'''
		Parameters
			driver -> Webdriver
			iframe_contents -> The HREF containing the main Outer IFrame
		Yield
			The HREF of Iframe
			
	'''


	'''
		Load the iframe
	'''

	for each_href in iframe_contents:

		try:

			core_logger.info("Fetching iframe %s "%each_href)
			core_logger.info("\n\n\n\n")

			driver.get(each_href)

			element = WebDriverWait(driver, 100).until(
			EC.presence_of_element_located((By.XPATH,iframe_body)))

			inner_iframe_awesome_table_src = driver.find_element_by_xpath(inner_iframe_awesome_table).get_attribute("src")

			yield inner_iframe_awesome_table_src

		except Exception as E:

			core_logger.critical("Exception on processing URL %s "%each_href)
			core_logger.critical(E)
			core_logger.critical("Processing Next ... ")
			continue


'''
	load the Iframe and extract the table from each page
	CLick on each page and process for all pages
'''

def load_awesome_table(driver,inner_iframe_awesome_table_src):

	'''
		Parameters
			driver -> Webdriver
			inner_iframe_awesome_table_src -> The HREF containing the Ifrane
		Yield
			The table from the Iframe
	'''


	'''
		Load the Awesome Table
	'''

	for each_href in inner_iframe_awesome_table_src:

		try:

			core_logger.info("Fetching Awesome table - Game %s "%each_href)
			core_logger.info("\n\n\n\n")

			driver.get(each_href)		

			element = WebDriverWait(driver, 100).until(
			EC.presence_of_all_elements_located((By.XPATH,inner_iframe_awesome_table_middle_container)))

			get_no_pages_total = driver.find_elements_by_xpath(inner_iframe_awesome_table_rows_count_3)[0]

			count_get_no_pages_total = get_no_pages_total.text
	
			core_logger.info("Total n.o. pages to process .... %s "%count_get_no_pages_total)
			core_logger.info("\n\n\n\n\n")

			counter_pages = 1

			''' Fetch records for all the pages '''

			while True:

				''' Fetch the Table and send it for further processing downstream '''			


				core_logger.info("Fetching page count index ..... ")
				core_logger.info("\n\n\n\n")

				get_no_pages_curr = driver.find_elements_by_xpath(inner_iframe_awesome_table_rows_count_2)[0]

				core_logger.info("Currently displaying records upto index %s  "%get_no_pages_curr.text)

				core_logger.info("\n\n\n\n\n")

				time.sleep(3)						

				''' 
					Exit if all the pages had been processed
				'''

				if not get_no_pages_curr.text == count_get_no_pages_total:


					'''
						Click the next arrow - pagination
						Do not click the '>' for the first time
					'''

					if not counter_pages == 1:


						core_logger.info("Clicking '>' arrow to access the next page .... please wait ")
						core_logger.info("\n\n\n\n")

						driver.find_element_by_xpath(inner_iframe_awesome_table_rows_pag_next).click()

						element = WebDriverWait(driver, 100).until(
									EC.presence_of_all_elements_located((By.XPATH,inner_iframe_awesome_table_middle_container)))


					counter_pages += 1

					yield driver.find_elements_by_xpath(inner_iframe_awesome_table_headers),driver.find_elements_by_xpath(inner_iframe_awesome_table_rows)


				else :

					core_logger.info("Processing Final records ... page ...  !")
					yield driver.find_elements_by_xpath(inner_iframe_awesome_table_headers),driver.find_elements_by_xpath(inner_iframe_awesome_table_rows)
					break



		except Exception as E:

			core_logger.critical("Exception on processing URL - Awesome table data --  %s "%each_href)
			core_logger.critical (E)
			core_logger.critical("Processing Next ... ")
			continue



'''
	Load the table and analyze Rows to extract game related data
	Fetch the Headers and Rows from each page and pass for further processing ...
'''
def fetch_headers_rows_table_content(driver,inner_iframe_awesome_table):

		'''
			Parameters
				driver -> Webdriver
				inner_iframe_awesome_table -> Full table containing Game related info
		'''



		for get_headers_FromTable,get_rows_FromTable in inner_iframe_awesome_table:

			try:

				core_logger.info("Fetch the table and analyze the rows ... ")
				core_logger.info("\n\n\n\n")
				core_logger.info("Fetch the Header text ... ")
				core_logger.info("\n\n\n\n")
				core_logger.info(" Total number of rows in the page %s - " %len(get_rows_FromTable))
				core_logger.info("\n\n\n\n")
				core_logger.info(" Total number of columns in the page %s - " %len(get_headers_FromTable))
				core_logger.info("\n\n\n\n")

				''' 
					Fetch all the table columns 
				'''
				headers_text = [elements.text.strip() for elements in get_headers_FromTable]


				''' 
					Filter the Headers to the weeks alone, we need to identify how many weeks are there 
				'''
				headers_text_weeks = filter(lambda data : "week" in str(data).lower() , headers_text)

				''' Determine the total n.o. Weeks '''
				get_total_weeks = len(headers_text_weeks)

				'''
					 Return an Array of datetime objects representing the starting date of weeks for the given year 

					 *** Make sure to process only once for a given year

				'''
				get_week_startdates = determine_week_start_dates(total_weeks = get_total_weeks,
																 year_of_product = getattr(sys.modules[__name__],'get_prd_year_val'))



				for counter in range(1,len(get_rows_FromTable)+1):

					core_logger.info("Processing Table Row n.o. -  %s "%counter)
					core_logger.info("\n\n\n\n")

					fetch_td_curr_xpath = inner_iframe_awesome_table_rows_curr_td%counter

					get_row_value = driver.find_elements_by_xpath(fetch_td_curr_xpath)

					print [element.text for element in get_row_value],'\n\n\n\n'
					break


			except Exception as E:

				core_logger.critical (E)
				core_logger.critical("Processing Next ... ")
				continue
'''
	Process records for each year - Software Weekly
'''

def process_records(driver):

	'''
		Parameters
			driver -> Webdriver
	'''

	'''
		Load the Home Page
	'''

	driver.get(baseurl)

	element = WebDriverWait(driver, 1000).until(
	EC.presence_of_element_located((By.XPATH,page_load)))


	'''
	Get all links to yearly games data
	'''

	core_logger.info("Get all links to yearly games data")
	core_logger.info("\n\n\n\n")

	all_years_games_urls = get_list_urls_to_process(driver,driver.page_source.encode("utf-8").strip())

	'''
		Fetch each href and obtain game related info
	'''
	core_logger.info("Fetch each href and obtain iframe src")
	core_logger.info("\n\n\n\n")
	
	fetch_headers_rows_table_content(driver,load_awesome_table(driver,load_iframe_game(driver,fetch_game_iframe_src(driver,all_years_games_urls))))








if __name__ == "__main__":

	print "Launching Driver ... "
	driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()

	print "Process Records !"
	process_records(driver)

