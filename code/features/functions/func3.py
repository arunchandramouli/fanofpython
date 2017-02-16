
from functools import wraps, partial
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a function and access it.. In Simple Words, a function can 
	take a set of arguments as an input, and return the calculated result

	It can be used to perform repetitive actions

	Here we will see examples of functions with default arguments 
	
'''


'''
	Let's start with a simple example - A Function to append numbers to a list and return it

	***** 
			
			Here we have defined containery=[] which means that the container is initialized at function
			definition time .

	*****
'''

def funcA(containerx,containery=[]):

	'''
		Add numbers in containerx to containery and return it

		Parameters:

			containerx - A List of numbers
			containery - A List to add numbers from containerx
			return containery
	'''

	for numbers in containerx:
		containery.append(numbers)

	return containery





'''
	Let's define another function - A Function to append numbers to a list and return it

	***** 
			
			Here we have defined containery=[] which means that the container is initialized at function
			definition time .

	*****
'''

def funcB(containerx,containery=[]):

	'''
		Add numbers in containerx to containery and return it

		Parameters:

			containerx - A List of numbers
			containery - A List to add numbers from containerx
			return containery

	'''

	''' 
		Make sure containery is empty before the action .
		When we add this if condition before, the container gets re-initialized each time
		the function is called.
	'''

	if not containery is None : containery = []

	for numbers in containerx:
		containery.append(numbers)

	return containery











'''
	Let's define another function - A Function to append numbers to a list and return it

	***** 
			
			Here we have are passing containery as a parameter.

	*****
'''

def funcC(containerx,containery):

	'''
		Add numbers in containerx to containery and return it

		Parameters:

			containerx - A List of numbers
			containery - A List to add numbers from containerx
			return containery

	'''

	''' 
		Make sure containery is empty before the action .
		When we add this if condition before, the container gets re-initialized each time
		the function is called.
	'''

	if not containery is None : containery = []

	for numbers in containerx:
		containery.append(numbers)

	return containery







if __name__ == "__main__":

	# ************************************************************************************** #
	
	''' Pass a list to the function '''


	get_result = funcA([100,200,300,400,500])
	print "Result is %s "%get_result,"\n"
	# Expected Result : [100, 200, 300, 400, 500]
	# Actual Result : [100, 200, 300, 400, 500]

	''' Pass a list to the function '''

	get_result = funcA([1000,2000,3000,4000,5000])
	print "Result is %s "%get_result,"\n"

	# Expected Result : [1000,2000,3000,4000,5000]
	# Actual Result : [100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000]

	'''
		
		When we call the same function for the second time why Actual != Expected?
		As mentioned above containery = [] is initialized at function definition time,so it wouldn't 
		re-initialize again while calling for the 2nd time. The values hence added on 1st call get appended
		with those on 2nd call. This is an important feature of a mutable argument.

		*** This problem has been solved in funcB

	'''


	''' Pass a list to the function '''


	get_result = funcB([100,200,300,400,500])
	print "Result is %s "%get_result,"\n"
	# Expected Result : [100, 200, 300, 400, 500]
	# Actual Result : [100, 200, 300, 400, 500]

	''' Pass a list to the function '''
	
	get_result = funcB([1000,2000,3000,4000,5000])
	print "Result is %s "%get_result,"\n"

	# Expected Result : [1000,2000,3000,4000,5000]
	# Actual Result : [1000,2000,3000,4000,5000]


	''' Pass a list to the function '''

	''' *** The functions below will work and return results properly since, the containery is initialized each time the 
		function is called .. for eg - funcC([10000,20000,30000,40000,50000],containery=[]) ***'''
	
	# containery is initialized as [] on function call not on function definition

	get_result = funcC([10000,20000,30000,40000,50000],containery=[]) 
	print "Result is %s "%get_result,"\n"

	# Expected Result : [10000,20000,30000,40000,50000]
	# Actual Result : [10000,20000,30000,40000,50000]

	# containery is initialized as [] on function call not on function definition

	get_result = funcC([10000,20000,30000,40000,50000],containery=[])
	print "Result is %s "%get_result,"\n"

	# Expected Result : [10000,20000,30000,40000,50000]
	# Actual Result : [10000,20000,30000,40000,50000]


	# ************************************************************************************** #

