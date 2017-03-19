
from functools import wraps, partial
import logging
import dis


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

	Also we will use dis module to inspect
	
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



''' A Very simple and loving function :-) '''

def iLoveyou():

	return "I Love You"





if __name__ == "__main__":

	# ************************************************************************************** #
	
	''' Pass a list to the function '''


	get_result = funcA([100,200,300,400,500])
	print "Result is %s "%get_result,"\n"
	# Expected Result : [100, 200, 300, 400, 500]
	# Actual Result : [100, 200, 300, 400, 500]

	''' Using dis  '''

	print "Disassamble .... ",'\n\n'
	print dis.dis(iLoveyou)

	# ************************************************************************************** #

