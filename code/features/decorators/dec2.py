
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

''' 
	Define a decorator get_func that takes a function as an input, executes it and returns the result
	of the function
'''

def get_func(func):

	''' 
		
		Define an inner function wrapper that actually does the job of executing the function.
		In the Outer function we get the function object, in this case calculate
		In the inner function we get the arguments of the calculate function , say x,y,z in this case

		What inner function does?

		The inner function wrapper is actually taking the arguments x,y,z as *args

			-- As we saw earlier * args means any numbers of arguments and **kargs means any n.o keyword arguments

		Then the inner function does the execution,
			store_result = func(*args,**kargs)
			This means that store_result is a variable that holds the result of the execution that is actually returned.
			func(*args,**kargs) - means to call a function
			If we were to call calculate  function with arguments 100,200,300 .. say for eg ;

			we would do as calculate(100,200,300), that's what the inner function does as func(*args,**kargs)

			At run time func becomes calcualte and *args becomes 100,200,300

			That's all there to it. As simple as that.

	'''


	@wraps(func)
	def wrapper(*args,**kargs):

			'''
				Calculate the Result
			'''
			core_logger.info("Execute and Store the Result")
			store_result = func(*args,**kargs)

			core_logger.info("Result :: %s "%store_result)

			return store_result

	return wrapper



@get_func
def calculate(x,y,z):

	
	''' 
		Perform arithmetics on the given inputs

		Parameters :
			x -> int
			y -> int
			z -> int
			return -> int (x+y*z)
	'''

	return x + y * z
    

if __name__ == "__main__":

	# ************************************************************************ #
	
		calculate(10,20,30) # Returns 610

	# ************************************************************************ #

