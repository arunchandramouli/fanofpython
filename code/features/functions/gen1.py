

import logging

'''
	Git Repo ::


'''

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a generator function and access it.. In Simple Words, create a 
	pipeline for execution
	
'''


'''
	A Function to take multiple args and kargs
'''

def funcA(*me,**myself):

	'''
		Append to list and yield

	'''


	core_logger.info("Append to list and yield .. ")
	core_logger.info("\n\n\n\n")

	sendmedown = []

	for itemsme , itemsmyself in zip(me,myself.values()):

		sendmedown.extend((itemsme,itemsmyself))

	
	yield sendmedown


'''
	A Function to do some filter operations
'''

def funcB(args):

	'''
		
		Do some filter

	'''


	core_logger.info("Filter and extract remaining values .. ")
	core_logger.info("\n\n\n\n")

	for values in args:

		get_filter_set = filter(lambda x : x %10 == 0 and x %5 == 0 , values)

		yield get_filter_set


'''
	A Function to sort the values
'''

def sortme(args):

	'''
		Get the container and sort
	'''

	for values in args:
		
		yield sorted(values)


'''
	A Function to add 10 to each number

	
'''

def funcC(args):

	'''
		Get the values and add and yield

	'''


	core_logger.info("Get the values and add and yield .. ")
	core_logger.info("\n\n\n\n")
	

	for values in args:

		yield [i+10 for i in values]




'''
	A Function to calculate the sum of numbers

'''

def funcD(args):

	'''
		Calculate sum and yield
	'''


	core_logger.info("Calculate sum and yield .. ")
	core_logger.info("\n\n\n\n")

	set_initial_sum = 0

	''' Iterate the args and add the values '''
	
	for value in args:

		for items in value:

			set_initial_sum += items

	yield set_initial_sum




'''
	Print the final sum
'''

def funcE(kargs):

	'''
		print the final sum
	'''

	core_logger.info("Print the final sum .. ")
	core_logger.info("\n\n\n\n")

	for values in kargs:

		print "Sum is %s "%values


def execfuncA():

	get_val = funcA(100,200,300,400,500,a=10,b=20,c=30,d=40,e=50)

	while True:

		try:

			print get_val.next()

		except StopIteration as I:
			core_logger.info("Process Completed !")
			break
	


'''
	Now let's form the flow for executing our generator code
'''

def run():

	'''
		
		When this bock is run , funcE will be first function to get called,
		it triggers the pipeline and executes in reverse order

		You can see this via logging ..... 

	'''

	get_val = funcA(100,200,300,400,500,a=10,b=20,c=30,d=40,e=50)
	ip_sortme = sortme(get_val)
	ip_funcB = funcB(ip_sortme)
	ip_funcC = funcC(ip_funcB)
	ip_funcD = funcD(ip_funcC)
	ip_funcE = funcE(ip_funcD)

if __name__ == "__main__":

	run()
