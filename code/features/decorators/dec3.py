
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

	Use @wraps to protect the signature information
'''



'''
	Define a decorator that doesn't take arguments
	Take a function as an input, pass it a few arguments and validate

	***** Here we will analyze the parameters passed in detail ****

	@wraps given below means to protect the original information of the functions that is being executed

	For eg @wraps(func) means the original information of the function func is protected and not altered

	This is because at run time since decorator get_func is actually executing the function calculate,
	the signature information such as function name, doc information of calculate will get changed to that of 
	get_func

	To prevent this behaviour we are using @wraps(func) which actaully means @wraps(calculate) at runtime.

	Given this , the information of function calculate is protected. 


	****** 
			Please be informed that it's not mandatory to provide @wraps , it is absolutely the
			choice of the developer . But I would recommend to do so..

	******
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
			return -> int (x+y*z)
	'''

	return x + y * z
    

if __name__ == "__main__":

	# ************************************************************************ #

	''' Executing the function '''
	store_result = calculate(10,20,30) # Returns 1220 since we are adding each parameter by 10


	core_logger.info("Result :: %s "%store_result)

	# ************************************************************************ #



	# ************************************************************************ #

	''' 
		Analyse the signature information of the function ... When we use @wraps
		for an inside function , the signature information of the original
		function is protected ..
	'''

	core_logger.info("Function name  - %s "%calculate.__name__) # print the function name
	core_logger.info("Function doc information - %s "%calculate.__doc__) # print the doc information (given in triple quotes inside the function )

	# ************************************************************************ #
