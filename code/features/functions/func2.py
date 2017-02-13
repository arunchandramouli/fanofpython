
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

	Here we will see examples of recursive functions -  A function that calls itself is known as recursive
	
'''


'''
	Let's start with a simple example - A Function to print the sum of numbers
'''

def funcA(x):

	'''
		Add numbers until range of x and return the result

	'''

	if x == 0:
		''' If the input is 0 we return 0 '''
		return x
	else:
		''' 
			Each time increment result until range is reached.
			For instance - if we input 10, it will start with 0 and sum-up the values until 10
			0 + 1
			0 + 1 + 2 ...

		'''
		return x + funcA(x-1)




if __name__ == "__main__":

	# ************************************************************************************** #
	
	''' Calculate sum of numbers and return the result .. '''

	''' ***** Following Program will add all numbers from 0 to 100 and return the result ***** '''

	print funcA(100)


	''' ***** Following Program will add all numbers from 0 to 10 and return the result ***** '''

	print funcA(10)

	# ************************************************************************************** #

