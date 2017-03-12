# -*- coding: UTF-8 -*-

'''
	SECTION - IMPORTS
'''
import multiprocessing
import datetime


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

def multirun(args_params):

	'''
		Parameters

			args_params -> Zip of iterables
	'''

	'''
		unwind the Container and get individual containers

		These are ranges that we had initially passed

			params1 - range(1000),
			params2 - range(1000,2000),
			params3 - range(2000,3000)

	'''


	params1 , params2 , params3 = args_params

	itemsContainer = []


	for ranges in range(10000):

		itemsContainer.append((params1 * ranges)  +  (params2 * ranges) +  (params3 * ranges))


	return itemsContainer


if __name__ == "__main__" :


	list_of_iterables = zip(range(1000),range(1000,2000),range(2000,3000))

	start_time = datetime.datetime.now()


	''' Create a Multiprocessing Pool Object '''
	multipool = multiprocessing.Pool()	

	'''  Execute it as parallel , shown below , using map function from Pool Class '''
	multipool.map(multirun,list_of_iterables)

	end_time = datetime.datetime.now()

	print "Using Parallel - %s "%(end_time - start_time)


	''' Execute it as a Serial using ordinary map function '''

	start_time = datetime.datetime.now()

	map(multirun,list_of_iterables)

	end_time = datetime.datetime.now()

	print "Using Serial - %s "%(end_time - start_time)

