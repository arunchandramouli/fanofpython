
from functools import wraps, partial
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a plain decorator to execute a function

	Take a function as an input, pass it a few arguments and validate
'''



'''
	Define a decorator that doesn't take arguments
	Take a function as an input, pass it a few arguments and validate

	***** Here we will analyze the parameters passed in detail ****
'''

def get_func(func):

	@wraps(func)
	def wrapper(*args,**kargs):

			'''
				Calculate the Result
			'''
			get_args = args
			get_kargs = kargs

			

			'''
				For each of the argument passed , add'em a value of 10

				which shall become (20,30,40)
			'''

			args = (i+10 for i in args)


			core_logger.info("Execute and Store the Result")
			store_result = func(*args,**kargs)

			core_logger.info("Result :: %s "%store_result)

			return store_result

	return wrapper


''' Calculate the sum of numbers '''
@get_func
def calculate(x,y,z):

	''' 
		Calculate the sum of numbers by adding all the arguments

		Parameters :
			x -> int
			y -> int
			z -> int
			return -> int (x+y+z)
	'''

	return x + y * z
    

if __name__ == "__main__":

	# ************************************************************************ #
		
		''' Executing the function '''
		calculate(10,20,30) # Returns 1220 since we are adding each parameter by 10

	# ************************************************************************ #



	# ************************************************************************ #

	''' 
		Analyse the signature information of the function ... When we use @wraps
		for an inside function , the signature information of the original
		function is protected ..
	'''

	print calculate.__name__ # print the function name
	print calculate.__doc__ # print the doc information (given in triple quotes inside the function )

	# ************************************************************************ #
