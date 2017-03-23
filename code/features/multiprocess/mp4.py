# -*- coding: UTF-8 -*-

'''

	SECTION - IMPORTS

'''

import multiprocessing
import datetime
import urllib
from threading import Thread
import os
import time
from random import random

'''
	
	Aim :: To multithread task of performing an operation on containers

	Here we take many containers as input and perform operation on each of its elements

	We peform this operation in parallel, say each process will hold a container


	*** In this example, we will hit several URLs and get their contents - imagine if we have
	to process several millions on a daily basis ***

'''



'''
	A Simple example of multithreading, this example will not be affected by GIL

	Say , We want to take multiple iterables and perform operations
'''



'''

	Declare the list of URLs to process

'''


list_of_urls_to_process = [

					  'http://www.python.org', 					
					  	"http://yahoo.com", "http://google.com", 
					  	"http://amazon.com",
						"http://ibm.com", "http://apple.com",
					  'http://stackoverflow.com'
					  
					 ]




'''
	SECTION - FUNCTION DEFINITION
'''


'''	
	Execute
'''

def execute(func):

	def mapper(*args,**kargs):

		print func.__name__

		start = time.time()

		result = func(*args,**kargs)

		end = time.time()

		print "Time Taken %s "%(end-start)

		return result

	return mapper


'''
	A function that operates on the iterables in parallel
'''

def multirun(fetch_url):

	'''
		Parameters

			fetch_url -> The URL To Fetch
	'''


	'''  Add page contents to a container -  A Simple scenario '''


	#with open("op_mp4"+str(random()*1000)+'.txt','w') as writer:

	get_data = urllib.urlopen(fetch_url)


	#writer.write(get_data.read().strip())



'''
	Execute it without Threads
'''

@execute
def withoutthreads():




	for x in list_of_urls_to_process:

		multirun(x) 

		



''' Execute it using Threads '''
@execute
def withthreads():


	''' Each and every URL will be a separate Thread ... '''

	for x in list_of_urls_to_process:

		t = Thread(target = multirun,args = (x,))
		t.daemon = True
		t.start()
		t.join()
		


if __name__ == "__main__" :


	withoutthreads()


	withthreads()