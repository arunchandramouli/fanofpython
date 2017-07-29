# -*- coding: UTF-8 -*-


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



************************************************************************************

		There are various products to fetch such as ;

			-> Software Weekly

			-> Hardware Weekly

			-> Digital Data

			-> Million Sellers

			-> Sotware Data

			-> Software Yearly

			-> Hardware Data

			-> Hardware Yearly

			-> Hardware Tools

		
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
'''




"""
	************************************************************************************


'''
	
	******************************************************************

		STEP 1 :: launch the Core Driver
	******************************************************************

'''


'''
	******************************************************************

		STEP 2 :: Get the list of HREFs that we need to process

		FOR EG - UNDER SOFTWARE WEEKLY, We have game sales data 
		represented for multiple years, say 1995 - Till Date
	******************************************************************

'''


'''

	******************************************************************

		STEP 3 :: Load the Home page - say 1995

	******************************************************************

'''



'''

	******************************************************************


		STEP 4:: Fetch the Main Iframe from the home page

		This has got pointers to other iframe holding product data

	******************************************************************

'''


'''

	******************************************************************

		STEP 5 :: Load the main Iframe that has links to other sources

	******************************************************************

'''


'''
	******************************************************************


		STEP 6 :: Obtain the iframe src of the Awesome table
		and load the same

		Note :: This is the key table holding all games sales data

	******************************************************************
'''


'''

	******************************************************************
	
		STEP 7 :: From the Awesome table, fetch the headers of the table and it's rows

		***** Do so for all the pages - It has got pagination links *****

	******************************************************************
'''


'''
	
	******************************************************************

		STEP 8 :: Process the Table Records - Say store them in a dictionary and create a table

		Refer - FINAL TABLE FORMAT defined above

	******************************************************************

'''


'''
	
	******************************************************************
		
		STEP 9 :: Format the table and convert each as a string ,
		say comma seperated values .

		We need it in a string format seperated by "," since
		we need to write the output to a *.csv file

	******************************************************************

'''


'''

	******************************************************************
		
		STEP 10 :: Write the string formatted in STEP 9 to a csv file
		Refer - FINAL TABLE FORMAT defined above

		Each and every game, will be shown it's weekly sales
		So in the table, the columns such as 

		System, Title, Publisher , Release Date

		Will find repetition to show sales for each week across the
		span of an year

	******************************************************************

'''


'''
	********** Repeat STEP 3 through STEP 10 for all years say 1995 - till date ********** 
'''


'''
	******************************************************************
	
		STEP 11 :: Load the CSV File into the Database - SQL Server

	******************************************************************
'''


'''
	
	## TODO :: Future Scope -- Perform this task in parallel, say for each HREF ; for eg - 1995, 1996 etc...
	perform tasks STEP 3 through STEP 10 and write to individual csv files, for eg - PRD_SALES_1995.csv

	
'''



"""


'''
	SECTION - FUNCTIONS	

	**** 

		Define the functions required to extract game related information 

		Functions are to be executed via a pipeline

	*****
'''


'''
	Get all the HREF that contains Games related information
'''
def get_list_urls_to_process(driver,page_source_lxml):

	'''
		Parameters
		
			driver -> Webdriver
			page_source_lxml -> Home page lxml object

		return
			A Container with Games related HREFs

	'''

	try:

		url_container = []

		for each_href in driver.find_elements_by_xpath(csettings.page_load_games_full_content):			
			url_container.append(each_href.get_attribute("href"))
		return url_container

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
	Given an URL, determine the year for which we need to determine weekly sales costs

'''
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

	Given a Header , find the first and last occurrence of Week(*) as a Column
	It could be WEEK1 ... WEEKN

'''

def find_first_last_occurence_weeks(all_headers,string_to_search="WEEK"):


	'''
		Parameters

			allheaders -> Array of headers from the Table

		return

			First and Last Occurrence Of Column that contains WEEK(*)

		    In case of exception, return "NA"
	'''

	try:

		start_pos_end_pos = [position for position,value in enumerate(all_headers) if str(string_to_search).lower() in str(value).lower()]

		return min(start_pos_end_pos),max(start_pos_end_pos)

	except Exception as E:

		core_logger.critical(E) 
		return "NA","NA"






''' 

	For a given year , return an array of week start dates - It should return an array of all weeks in an year,
	as a datetime object in isoformat

'''
def determine_week_start_dates(total_weeks ,year_of_product,array_of_weeks = []):

	
	'''
		Parameters

			total_weeks -> Total no. weeks given in the Table
			year_of_product -> Product Release year

		return

			-> an array of week start dates - It should return an array of all weeks in an year in a datetime object format

			In case of an exception return as an array of strings
	'''

	''' Make sure to make it void each time the function is called '''

	if not array_of_weeks == [] : array_of_weeks = []

	try:

		core_logger.info("Determine the week start dates , given an year !")
		core_logger.info("Processing for Year %s "%year_of_product)

		set_start_year = datetime.date(int(year_of_product),1,1)

		for each_week_number in range(1,total_weeks+1):

			''' Determine the week start dates '''

			array_of_weeks.append(set_start_year + datetime.timedelta(weeks=int(each_week_number)))

		return array_of_weeks

	except Exception as E:

		core_logger.critical(E)

		return ["WEEK"+str(week_number) for week_number in range(1,total_weeks+1)]




'''

	From the initial product home page - Fetch the base iframe

	**** This iframe has got links to other sections of the product ****

'''

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


			core_logger.info("*"*50)
			core_logger.info("\n\n\n\n")

			core_logger.info("Fetching product page based on year .... %s "%get_prd_year_val)

			core_logger.info("\n\n\n\n")			


			core_logger.info("*"*50)
			core_logger.info("\n\n\n\n")

			driver.get(each_href)

			element = WebDriverWait(driver, 100).until(
			EC.presence_of_element_located((By.XPATH,csettings.page_load)))

			iframe_contents = driver.find_element_by_xpath(csettings.iframe_game_data).get_attribute("src")

			yield iframe_contents


		except Exception as E:

			core_logger.critical("Exception on processing URL %s "%each_href)
			core_logger.critical (E)
			core_logger.critical("Processing Next ... ")
			continue


'''

	Load the main Iframe that was determined in the previous step

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
			EC.presence_of_element_located((By.XPATH,csettings.iframe_body)))

			inner_iframe_awesome_table_src = driver.find_element_by_xpath(csettings.inner_iframe_awesome_table).get_attribute("src")

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
			EC.presence_of_all_elements_located((By.XPATH,csettings.inner_iframe_awesome_table_middle_container)))

			get_no_pages_total = driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_rows_count_3)[0]

			count_get_no_pages_total = get_no_pages_total.text
	
			core_logger.info("Total n.o. pages to process .... %s "%count_get_no_pages_total)
			core_logger.info("\n\n\n\n\n")

			counter_pages = 1

			''' Fetch records for all the pages '''

			while True:

				''' Fetch the Table and send it for further processing downstream '''			


				core_logger.info("Fetching page count index ..... ")
				core_logger.info("\n\n\n\n")

				get_no_pages_curr = driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_rows_count_2)[0]

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

						core_logger.info("*"*50)
						core_logger.info("\n\n\n\n")
						core_logger.info("Clicking '>' arrow to access the next page .... please wait ")
						time.sleep(1)
						core_logger.info("\n\n\n\n")
						core_logger.info("*"*50)
						core_logger.info("\n\n\n\n")

						driver.find_element_by_xpath(csettings.inner_iframe_awesome_table_rows_pag_next).click()

						element = WebDriverWait(driver, 100).until(
									EC.presence_of_all_elements_located((By.XPATH,csettings.inner_iframe_awesome_table_middle_container)))


					counter_pages += 1

					yield driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_headers),driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_rows)


				else :

					core_logger.info("Processing Final records ... page ...  !")
					yield driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_headers),driver.find_elements_by_xpath(csettings.inner_iframe_awesome_table_rows)
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
					
					Find the first and last occurrence of column titled as WEEK(*)
					We need to slice the Table row containing Game related data
					and map each sale period to its corresponding week

				'''

				get_occurrences_weeks_in_headers = find_first_last_occurence_weeks(headers_text)

				''' Set it as an attribute to a module '''

				setattr(sys.modules[__name__],"get_occurrences_weeks_in_headers",get_occurrences_weeks_in_headers)


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

					fetch_td_curr_xpath = csettings.inner_iframe_awesome_table_rows_curr_td%counter

					get_row_value = driver.find_elements_by_xpath(fetch_td_curr_xpath)

					get_data = [element.text for element in get_row_value]
					
					yield get_data , get_week_startdates
					


			except Exception as E:

				core_logger.critical (E)
				core_logger.critical("Processing Next ... ")
				continue


'''
	Process the records obtained in the previous step and form a table
	
	The Table Columns are as follows;

	Sys Title Sales Week Publisher ReleaseDate

'''

def process_table_records(driver,table_records):

	
	'''
		Parameters

			table_records -> Table Row data and the no weeks they need to be mapped against		

			Form a Table such as ;

			Sys Title Sales Week Publisher ReleaseDate

			The n.o. weeks are fetched from the Headers, map sales data for each week
			against the records
	'''


	for row_value,week_start_dates in table_records:

		''' 

			Unpack it to obtain the rows data and week array 

		'''


		''' 

			Get value of attribute - get_occurrences_weeks_in_headers 
			getattr(sys.modules[__name__],"get_occurrences_weeks_in_headers") and map sales
			for each week against the Week

		'''


		get_start , get_end = getattr(sys.modules[__name__],"get_occurrences_weeks_in_headers")

		'''
			Now Slice the table row accordingly
		'''

		get_rows_sales_data = row_value.__getslice__(get_start,get_end+1)

		get_sys_title = row_value[0:get_start]

		get_publisher_release_date = row_value[get_end+1:]



		''' 

			Create an OrderedDict of Weekly Sales and Week Start Dates , insertion order is very important
			while we publish the sales table

			Sys Title Sales Week Publisher ReleaseDate

		'''

		get_weekly_sales_data = OrderedDict()

		core_logger.info("Creating a Table of records .... ")
		core_logger.info("\n\n\n\n")

		for sales_data,week_start_date in zip(get_rows_sales_data,week_start_dates):


			try:

				get_weekly_sales_data.__setitem__("System",u''.join(get_sys_title.__getitem__(0)).encode('utf-8').strip())
				get_weekly_sales_data.__setitem__("Title",u''.join(get_sys_title.__getitem__(1)).encode('utf-8').strip())
				
				get_weekly_sales_data.__setitem__("Sales",float(sales_data))
				get_weekly_sales_data.__setitem__("Week",week_start_date.isoformat())
				
				get_weekly_sales_data.__setitem__("Publisher",u''.join(get_publisher_release_date.__getitem__(0)).encode('utf-8').strip())
				get_weekly_sales_data.__setitem__("ReleaseDate",u''.join(get_publisher_release_date.__getitem__(1)).encode('utf-8').strip())

				yield get_weekly_sales_data

			except Exception as E:
				core_logger.critical(E)
		
				continue


	

''' 
	
	Obtain the records from the Table and process it further	
	and convert it in a format to fit a csv file, say as "," seperated values

'''

def process_table_records_format(driver,get_weekly_sales_data):

	'''
		
		Parameters

			get_weekly_sales_data -> A Table reprensenting Weekly Sales

	'''


	core_logger.info("Analyzing the Table of records and converting to a different format ... ")
	core_logger.info("\n\n\n\n")


	for sales_data in get_weekly_sales_data:

		data = ''

		for each_week_data_keys,each_week_data_vals in sales_data.items():

			try:

				data += str(each_week_data_vals)+","

			except Exception as E:

				core_logger.critical(E)
				continue

		data += '\r'

		yield data




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

	'''
		Load the Home Page
	'''

	driver.get(csettings.baseurl)

	element = WebDriverWait(driver, 1000).until(
	EC.presence_of_element_located((By.XPATH,csettings.page_load)))


	'''
	Get all links to yearly games data
	'''

	core_logger.info("Get all links to yearly games data")
	core_logger.info("\n\n\n\n")

	all_years_games_urls = get_list_urls_to_process(driver,driver.page_source.encode("utf-8").strip())

	'''
		Fetch each href and obtain game related info

		Execute the pipeline and write games related info into a CSV File

	'''
	core_logger.info("Execute the pipeline and write games related info into a CSV File")
	core_logger.info("\n\n\n\n")
		


	''' Execute the pipeline and write games related info into a CSV File '''

	final_op_csv(driver,process_table_records_format(driver,process_table_records(driver,
		fetch_headers_rows_table_content(driver,load_awesome_table(driver,
			load_iframe_game(driver,fetch_game_iframe_src(driver,all_years_games_urls)))))))





if __name__ == "__main__":

	core_logger.info("Launching Core Driver ...  ")
	core_logger.info("\n\n\n\n")

	driver = launch_driver('C:/PhantomJs/bin/phantomjs')
	driver.maximize_window()

	core_logger.info("Starting to Process - Fetch Game related sales data for all years until today ... ")
	core_logger.info("\n\n\n\n")
	
	run_gdl(driver)

