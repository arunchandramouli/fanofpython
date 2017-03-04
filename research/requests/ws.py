
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html

baseurl = "https://sites.google.com/site/gamedatalibrary/software-by-year/"



'''
	Xpath for extracting games related information
'''

page_load = "//*[@id='body']//*"

page_load_games_full_content = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']/div/a[1]"

iframe_game_data = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']//*[contains(@class,'sites-embed-content')]/iframe"

iframe_body = "//*[@dir='ltr']//*"

inner_iframe_awesome_table = "//*[@dir='ltr']//*[contains(@class,'tabcontent')]/iframe"


inner_iframe_awesome_table_middle_container = "//*[@id='middleContainer']//*"

inner_iframe_awesome_table_rows = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table/tbody/tr[contains(@class,'google-visualization-table')]"



inner_iframe_awesome_table_headers = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table/thead/tr/th[contains(@class,'google-visualization-table')]"




collections_mapper= []




def get_list_urls_to_process(driver,page_source_lxml):

	try:

		url_container = []

		for each_href in driver.find_elements_by_xpath(page_load_games_full_content):			
			url_container.append(each_href.get_attribute("href"))
		return url_container

	except Exception as E:
		print E
		return []



def launch_driver():


	driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()

	return driver



def fetch_game_iframe_src(driver,href_list):


	'''
		Go to each href and obtain game related information
	'''

	for each_href in href_list:


		print "Fetching product page based on year .... %s "%each_href,"\n\n"

		driver.get(each_href)

		element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.XPATH,page_load)))

		iframe_contents = driver.find_element_by_xpath(iframe_game_data).get_attribute("src")

		yield iframe_contents



def load_iframe_game(driver,iframe_contents):


	'''
		Load the iframe
	'''

	for each_href in iframe_contents:

		print "Fetching iframe %s "%each_href,"\n\n"

		driver.get(each_href)

		element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.XPATH,iframe_body)))

		inner_iframe_awesome_table_src = driver.find_element_by_xpath(inner_iframe_awesome_table).get_attribute("src")

		yield inner_iframe_awesome_table_src



def load_awesome_table(driver,inner_iframe_awesome_table_src):

	'''
		Load the Awesome Table
	'''

	for each_href in inner_iframe_awesome_table_src:

		print "Fetching Awesome table - Game %s "%each_href,"\n\n"
		driver.get(each_href)		


		print True

		time.sleep(15)

		print True

		driver.save_screenshot("data.png")

		print driver.current_url,'\n\n'
		

		'''element = WebDriverWait(driver, 1000).until(
		EC.presence_of_all_elements_located((By.XPATH,inner_iframe_awesome_table_middle_container)))'''



def process_records(driver):

	'''
		Load the Home Page
	'''

	driver.get(baseurl)

	element = WebDriverWait(driver, 100).until(
	EC.presence_of_element_located((By.XPATH,page_load)))


	'''
	Get all links to yearly games data
	'''

	print ("Get all links to yearly games data")
	all_years_games_urls = get_list_urls_to_process(driver,driver.page_source.encode("utf-8").strip())

	'''
		Fetch each href and obtain game related info
	'''
	print ("Fetch each href and obtain iframe src")
	
	load_awesome_table(driver,load_iframe_game(driver,fetch_game_iframe_src(driver,all_years_games_urls)))








if __name__ == "__main__":

	print "Launching Driver ... "
	driver = webdriver.PhantomJS('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()
	print driver

	print "Process Records !"
	process_records(driver)

