
# -*- coding: UTF-8 -*-

'''

	SECTION - IMPORTS

'''

import multiprocessing
import datetime
import requests
from threading import Thread
import os
import time
from random import random
import sys

sys.setrecursionlimit(10000)



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

def multirun(ranges):

	'''
		Parameters

			ranges -> a biggy list . . . .
	'''

	container = []

	for items in ranges:
		
		if int(items) and int(items) > 10000:

			items += 1000
			items *= 2000
			items %= 1000

			container.append(items * 10)

		else:


			items += 1000
			items *= 2000
			container.append(items * 100)


	for elements in container:

		if elements % 5 != 0 or elements % 7 != 0 :

			container.remove(elements)

	return container




'''
	Execute it without Threads
'''

@execute
def withoutthreads():

	multirun(range(9999999))
	print 0
	multirun(range(9999999))
	print 1
	multirun(range(9999999))
	print 2
	multirun(range(9999999))
	print 3
		



''' Execute it using Threads '''
@execute
def withthreads():


	t = Thread(target = multirun,args = (range(9999999),))
	t1 = Thread(target = multirun,args = (range(9999999),))
	t2 = Thread(target = multirun,args = (range(9999999),))
	t3 = Thread(target = multirun,args = (range(9999999),))

	t.start()	
	t1.start()
	t2.start()
	t3.start()
	
	t.join()
	t1.join()	
	t2.join()
	t3.join()
		


if __name__ == "__main__" :


	#withoutthreads()

	withthreads()