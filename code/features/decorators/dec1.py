
from functools import wraps, partial
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a Decorator that takes arguments

	Take a function as an input, pass it a few arguments and validate
'''


'''
	Define a decorator that takes arguments
	Take a function as an input, pass it a few arguments and validate
'''
def debug(func = None , prefix = ''):

        if func is None:
            return partial(debug,prefix = prefix)

        core_logger.info("Executing function %s "%func.__name__)

        @wraps(func)
        def wrapper(*args,**kargs):

			'''
				Calculate the Result
			'''
			core_logger.info("Execute and Store the Result")
			store_result = func(*args,**kargs)

			'''
				Manipulate the result by the parameter
			'''
			core_logger.info("Calculate and return the new result")
			new_result = store_result + prefix

			core_logger.info("Result :: %s "%new_result)
			return new_result

        return wrapper


@debug(prefix= 1000)
def calculate(x,y,z):

	return x + y * z
    

if __name__ == "__main__":

	# ************************************************************************ #
	
	calculate(10,20,30) # Returns 1610

	# ************************************************************************ #

