
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
			core_logger.info("Fetching product page based on year .... %s "%each_href)

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

			element = WebDriverWait(driver, 1000).until(
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

			element = WebDriverWait(driver, 1000).until(
			EC.presence_of_all_elements_located((By.XPATH,inner_iframe_awesome_table_middle_container)))


			''' Fetch the Table and send it for further processing downstream '''
			
			yield driver.find_elements_by_xpath(inner_iframe_awesome_table_headers),driver.find_elements_by_xpath(inner_iframe_awesome_table_rows)


		except Exception as E:

			core_logger.critical("Exception on processing URL %s "%each_href)
			core_logger.critical (E)
			core_logger.critical("Processing Next ... ")
			continue



'''
	Load the table and analyze Rows to extract game related data
'''
def process_games_records_iframe(driver,inner_iframe_awesome_table):

		'''
			Parameters
				driver -> Webdriver
				inner_iframe_awesome_table -> Full table containing Game related info
		'''



		for get_headers_FromTable,get_rows_FromTable in inner_iframe_awesome_table:

			core_logger.info("Fetch the table and analyze the rows ... ")
			core_logger.info("\n\n\n\n")
			core_logger.info("Fetch the Header text ... ")
			core_logger.info("\n\n\n\n")
			core_logger.info(len(get_rows_FromTable))
			core_logger.info("\n\n\n\n")
			core_logger.info(len(get_headers_FromTable))
			core_logger.info("\n\n\n\n")


			#print get_headers_FromTable,'\n\n',get_rows_FromTable,'\n\n'
			headers_text = [elements.text.strip() for elements in get_headers_FromTable]
			#rows_td = [elements.find_element_by_xpath("/td").text.strip() for elements in get_rows_FromTable]

			for elements in get_rows_FromTable:

				print elements,'\n\n\n\n',len(elements),'\n\n\n\n'
	
				print [element.text for element in elements.get_attribute("td")],'\n\n\n'
				break


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
	
	process_games_records_iframe(driver,load_awesome_table(driver,load_iframe_game(driver,fetch_game_iframe_src(driver,all_years_games_urls))))








if __name__ == "__main__":

	print "Launching Driver ... "
	driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()
	print driver

	print "Process Records !"
	process_records(driver)

