
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

	Here we will define multiple decorators to a function and check the order of execution

	*** 
		Please remember that each decorator will have its own copy of the function object , 
		check the same using id(func) ...
	***

'''


''' A Dummy decorator that does nothing '''
def deco_func1(func):

	def inner_deco_func1(*args,**kargs):

		print "deco_func1" , id(func)

		result_func1 = func(*args,**kargs)

		return result_func1 + 10

	return inner_deco_func1


''' A Dummy decorator that does nothing '''
def deco_func2(func):

	def inner_deco_func2(*args,**kargs):

		print "deco_func2", id(func)

		result_func2 = func(*args,**kargs)

		return result_func2 + 20

	return inner_deco_func2



''' A Dummy decorator that does nothing '''
def deco_func3(func):

	def inner_deco_func3(*args,**kargs):

		print "deco_func3", id(func)

		result_func3 = func(*args,**kargs)
		
		return result_func3 + 30

	return inner_deco_func3


''' Calculate the sum of numbers '''


''' 
	
	What happens internally ??? Did you think why we need 3 decorators? What's the heck of order?
	

	Well, when we structure a block like this,
	
	@deco_func1
	@deco_func2
	@deco_func3

	deco_func1 -> Get's called first and the result is calculated , say X

	deco_func2 -> Take the result of deco_func1 (X) and do more ... , it returns new result
	
	deco_func2 -> Take the result of deco_fun3 and do more ..., it returns new result

	As we can see the function is manipulated by 3 decorators and results are accumulted

	Here we are adding 3 n.os x,y,z as x+y+z

	deco_func1 -> Executes calculate and states result_func1 + 10 (Add 10 to the result )
	deco_func2 -> First obtain the resulf of deco_func1 and it further states result_func2 + 20 (Add 20 to the result )
	deco_func3 -> First obtain the resulf of deco_func2 and it further states result_func3 + 30 (Add 30 to the result )


	If you see the code below, we are actually executing as ; calculate(10,20,30)
	which by all means returns 120, since the results are executed and incremented at each level by the decorators


'''

'''  Function calculate has 3 levels of decorators to be executed '''
@deco_func1
@deco_func2
@deco_func3
def calculate(x,y,z):


	''' 
		Perform arithmetics on the given inputs

		Parameters :
			x -> int
			y -> int
			z -> int
			return -> int (x+y+z)
	'''

	
	return x + y + z
    

if __name__ == "__main__":

	# ************************************************************************ #

	''' Executing the function '''
	store_result = calculate(10,20,30) # Returns 60


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
