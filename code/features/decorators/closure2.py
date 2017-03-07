'''

	 Function are first class objects in python, they can passed as a parameters, be assigned to a variable, manipulated @ runtime etc...
	 We will see the function and inner function basics
	 In Python there are 2 keywords that can create a function object, namely - def & lambda

	 A Closure can be represented as an inner function ... 

'''


'''

	Define a simple closure that takes a tuple as an argument

	 *** and returns the inner function ***

'''

def function(*args):

	''' 
	
		Take a tuple as an argument , return it in the inner function ...

	'''

	def innerfunction():

		# Return the result

		return [i * 100 for i in args]

	'''
		return innerfunction - Returns the function object
		return innerfunction() - Executes the innerfunction and returns the result
	'''

	return innerfunction





'''

	Define a simple closure that takes a tuple as an argument

	 *** and returns the result of inner function ***

'''




def functionB(*args):

	''' 
	
		Take a tuple as an argument , return it in the inner function ...

	'''

	def innerfunctionB():

		# Return the result

		return [i * 100 for i in args]

	'''
		return innerfunction - Returns the function object
		return innerfunction() - Executes the innerfunction and returns the result
	'''

	return innerfunctionB()




''' Execute '''
if __name__ == "__main__":

	
	''' Get the function object '''

	get_func = function(100,200,300,400,500)
	
	# Returns <function innerfunction at 0x000000000129A0B8>

	''' Execute the function object '''

	result = get_func()
	print "Result is %s "%result
	# Returns Result is [10000, 20000, 30000, 40000, 50000]



	''' Execute functionB '''
	result = functionB(1000,2000,3000,4000,5000,6000,7000,8000,9000,10000)
	print "Result is %s "%result
	# Returns Result is [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]