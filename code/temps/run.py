# -*- coding: UTF-8 -*-


import urlparse

'''
	Aim :: Scrap Game related data from the Japanese Gamedata Library

	Fetch the details of sales of each game against a range of years, on a weekly basis

	Form a table and load it into a csv file, which will then pushed to the SQL Server

	The table shall consist of following columns;

	System , Title , Sales, Week, Publisher , Release Date

	System -> Type of System on which the Game Runs

	Title -> Name of the Game

	Sales -> In figures, the amount of sales and corresponding earnings

	Week -> Weekstart date , say an year has 52 weeks , fr eg - List the sales for each week

	Publisher -> Name of the Publishing company

	Release -> The Date when the Game was officially released to the Public


	Source URL :: https://sites.google.com/site/gamedatalibrary/


		
		Note :: We will focus and fetch only required products
		as per the need

************************************************************************************


'''


'''
	***** FINAL TABLE FORMAT  *****

	sYSTEM , TITLE , SALES , WEEK , PUBLISHER , RELEASEDATE
'''



'''
	SECTION IMPORTS
'''

import os
import sys
import datetime
import re
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import html
import logging

from collections import OrderedDict
import csettings



'''
	Logging Facilities
'''

logging.basicConfig(level=logging.INFO)
core_logger = logging.getLogger("Citadel")




'''
	CONTAINERS FOR HOLDING DATA AN PASSING VIA THE PIPELINE
'''
collections_mapper= []

table_mapper = []






'''
	Following are the steps to be executed in order'

	Step 1 :: Launch the Core Driver

	Step 2 :: Fetch all Equipment Types

	Step 3 :: Fetch all Equipment Categories

	Step 4 :: Fetch all Subcats

	Step 5 :: For each Subcat , derive information based on zipcode

	Step 6 :: Record ass much details as possible for the product

'''




'''
	SECTION - FUNCTIONS	

	**** 

		Define the functions required to extract equipments related information 

		Functions are to be executed via a pipeline

	*****
'''



'''
	Load the home page and return thy elements
'''

def load_home_page(driver):

	'''
		Load and return elements as lxml object
	'''

	try:

		core_logger.info("Home Page Loading .... ")
		core_logger.info("\n\n")

		driver.get(csettings.baseurl_equipment)


		element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.XPATH,csettings.home_page_load)))

		core_logger.info("Home Page Loaded ")
		core_logger.info("\n\n")
		
		yield html.fromstring(driver.page_source.encode('utf-8'))

	except Exception as I:

		raise Exception("Unable to proceed since home page %s cant be loaded ..."%(csettings.baseurl_equipment))


'''
	Get all the HREF that contains Equipments types related information
'''
def get_list_equipmenttypes_urls_to_process(driver,page_source_lxml):

	'''
		Parameters
		
			driver -> Webdriver
			page_source_lxml -> Home page lxml object

		return
			A Container with Equipments related HREFs

	'''

	try:


		core_logger.info("Fetch all the Equipment types")
		core_logger.info("\n\n")

		url_container = []
		get_page_source_lxml = page_source_lxml



		while True:

			try:	

				get_get_page_source_lxml = get_page_source_lxml.next()

				get_equipment_catalog_home_page = get_get_page_source_lxml.xpath(csettings.equipment_catalog_home_page)			
				
				urls = []

				try:

					for urls in get_equipment_catalog_home_page:

						core_logger.info("Loading Category Page . . .")
						core_logger.info("\n\n")

						driver.get(urlparse.urljoin(csettings.baseurl,urls))

						element = WebDriverWait(driver, 100).until(
						EC.presence_of_element_located((By.XPATH,csettings.home_page_load)))

						''' Get the Page Source '''
						get_page_source_lxml = html.fromstring(driver.page_source.encode("utf-8"))
						get_subCats = get_page_source_lxml.xpath(csettings.equipment_catalog_home_page)

						

						core_logger.info("Loading Subcats Page . . .")
						core_logger.info("\n\n")

						for urls in get_subCats:

							try:

								driver.get(urlparse.urljoin(csettings.baseurl,urls))


								element = WebDriverWait(driver, 100).until(
								EC.presence_of_element_located((By.XPATH,csettings.home_page_load)))

								''' Get the Page Source '''
								get_page_source_lxml = html.fromstring(driver.page_source.encode("utf-8"))
								get_items = get_page_source_lxml.xpath(csettings.equipment_catalog_home_page)

								core_logger.info("Loading Items page ... ")
								core_logger.info("\n\n")

								for urls in get_items:

									try:


										driver.get(urlparse.urljoin(csettings.baseurl,urls))

										element = WebDriverWait(driver, 100).until(
										EC.presence_of_element_located((By.XPATH,csettings.home_page_load)))								

										''' Get the Page Source '''
										get_page_source_lxml = html.fromstring(driver.page_source.encode("utf-8"))

										getmore_items = get_page_source_lxml.xpath(csettings.more_items)


										if bool(getmore_items):

											core_logger.info("Sub-items found for %s "%driver.current_url)

											for urls in getmore_items:

												driver.get(urlparse.urljoin(csettings.baseurl,urls))

												element = WebDriverWait(driver, 100).until(
												EC.presence_of_element_located((By.XPATH,csettings.home_page_load)))

												print driver.current_url,'\n\n'

										else:

											print driver.current_url,'\n\n'

									except Exception as I:
										
										core_logger.critical(I)
										core_logger.info("\n\n")
										core_logger.critical(urls)
										core_logger.info("\n\n")
										core_logger.info("Fetching next ... ")
										core_logger.info("\n\n")
										continue



							except Exception as I:
								
								core_logger.critical(I)
								core_logger.info("\n\n")
								core_logger.critical(urls)
								core_logger.info("\n\n")
								core_logger.info("Fetching next ... ")
								core_logger.info("\n\n")
								continue

				except Exception as I:
					core_logger.critical(I)
					continue



			except StopIteration as I:
				core_logger.info("Completed processing ")
				break



	except Exception as E:
		core_logger.critical(E)
		return []



'''
	Launch and return the core driver object 
'''
def launch_driver(phantomjsloc,service_args=None):

	'''
		Parameters

			-> phantomjsloc - Path to fetch the core driver

		return
	
			-> Core Driver

	'''

	try:

		driver = webdriver.PhantomJS(phantomjsloc)
		driver.maximize_window()

		return driver

	except Exception as E:
		raise Exception(E)
		



'''

	Write the final output to the csv file 

	***** This CSV file is to be then loaded as a bcp file into SQL Server *****

'''

def final_op_csv(driver,records):

	'''
		Parameters
			records -> Row data formatted as string seperated by ',' in previous step
	'''


	core_logger.info("Writing Final Output to the CSV File ")

	for each_rcd in records:

		with open("records.csv",'a') as writer:

			try:

				writer.write(each_rcd)
				writer.write("\n")

			except Exception as E:

				core_logger.critical(E)
				continue



'''
	Process records for each year

	***** Function below triggers the pipeline *****
'''

def run_gdl(driver):



	'''
		Parameters
			driver -> Webdriver
	'''


	''' Delete the O/p file it exists already '''

	if os.path.exists(csettings.file_create_op):os.remove(csettings.file_create_op)

	''' Load the Home page and return its elements '''
	core_logger.info("Load the Home page and return its elements")
	core_logger.info("\n\n")

	get_home_page_objects = load_home_page(driver)

	core_logger.info("Fetch Equipments Types")
	core_logger.info("\n\n")

	get_list_cats_urls_to_process_data = get_list_equipmenttypes_urls_to_process(driver,get_home_page_objects)


if __name__ == "__main__":

	core_logger.info("Launching Core Driver ...  ")
	core_logger.info("\n\n")

	driver = launch_driver('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()

	core_logger.info("Starting to Process - Fetch Equiments details  ... ")
	core_logger.info("\n\n")
	
	run_gdl(driver)

