'''

	 Function are first class objects in python, they can passed as a parameters, be assigned to a variable, manipulated @ runtime etc...
	 We will see the function and inner function basics
	 In Python there are 2 keywords that can create a function object, namely - def & lambda

	 A Closure can be represented as an inner function ... 

	 Pass an argument to an inner function , execute and return the result

'''

'''
	Define a global variable
'''

set_sum = 0

'''

	Define a simple closure that takes a tuple as an argument

	 *** and returns the result of the inner function ***

'''

def function(*args):

	''' 
	
		Take a tuple as an argument , return it in the inner function ...

	'''

	def innerfunction(**kargs):

	
		'''
			
			Let's do some interesting stuff - take all args from inner and outer functions
			Calculate the sum of them and return

			In the following example ;

			(a , b) -> kargs.items() - A Dictionary
			i -> args - A Tuple

		'''
		# To access a global variable use global keyword
		global set_sum

		for (a , b) , i in zip(kargs.items(),args):

			set_sum += b + i

		return set_sum


	'''
		return innerfunction - Returns the function object
		return innerfunction() - Executes the innerfunction and returns the result
	'''

	return innerfunction




''' Execute '''
if __name__ == "__main__":


	'''
		Step 1 :: Get the innerfunction object
	'''	

	get_func = function(10000,20000,30000,40000,50000)

	'''
		Step 2 :: Execute the innerfunction by passing arguments
	'''
	result = get_func(a=100,b=200,c=300,d=400,e=500)
	print "Result is %s "%result