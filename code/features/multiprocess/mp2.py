# -*- coding: UTF-8 -*-

'''

	SECTION - IMPORTS

'''

import multiprocessing
import datetime
import requests



'''
	
	Aim :: To multiprocess task of performing an operation on containers

	Here we take many containers as input and perform operation on each of its elements

	We peform this operation in parallel, say each process will hold a container

	***** Also we will analyze the time differences between serial and parallel *****


	There are 2 ways to acheive concurrency - Process Class and Pool Class

	Note :: In Python, map is a built-in function that takes 2 arguments;

		-> Function to operate upon
		-> Iterable , the Container
	for eg : map(function1 , range(100000))

	Means that function1 will get an input of range(100000), function will be applied to each item in that list ,
	and finally it returns a list

	Defining function1;

		def function1(num):

			return num ** 5


	*** In this example, we will hit several URLs and get their contents - imagine if we have
	to process several millions on a daily basis ***

'''



'''
	A Simple example of multiprocessing with Pool Class

	Say , We want to take multiple iterables and perform operations
'''



'''
	SECTION - FUNCTION DEFINITION
'''


'''
	A function that operates on the iterables in parallel
'''

def multirun(fetch_url):

	'''
		Parameters

			fetch_url -> The URL To Fetch
	'''


	'''  Add page contents to a container -  A Simple scenario '''

	itemsContainer = []

	get_data = requests.get(fetch_url)
	itemsContainer.append(get_data.content.strip())

	return itemsContainer


if __name__ == "__main__" :


	list_of_iterables = [

						  'http://www.python.org', 
						  'http://www.python.org/about/',
						  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
						  'http://www.python.org/doc/',
						  'http://www.python.org/download/',
						  'http://www.python.org/getit/',
						  'http://www.python.org/community/',
						  'https://wiki.python.org/moin/',
						  'http://planet.python.org/',
						  'https://wiki.python.org/moin/LocalUserGroups',
						  'http://www.python.org/psf/',
						  'http://docs.python.org/devguide/',
						  'http://www.python.org/community/awards/',
						  'https://www.sites.google.com'
						  
						 ]


	''' Create a Multiprocessing Pool Object '''

	multipool = multiprocessing.Pool()	


	''' Execute it as a Serial using ordinary map function '''

	print "Execute it as serial .... ",'\n\n\n\n'

	start_time = datetime.datetime.now()

	map(multirun,list_of_iterables)

	end_time = datetime.datetime.now()

	print "Using Serial - %s "%(end_time - start_time),'\n\n\n\n'



	'''  Execute it as parallel , shown below , using map function from Pool Class '''

	print "Execute it as parallel .... ",'\n\n\n\n'

	start_time = datetime.datetime.now()

	multipool.map(multirun,list_of_iterables)

	end_time = datetime.datetime.now()

	print "Using Parallel - %s "%(end_time - start_time),'\n\n\n\n'

