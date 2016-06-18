'''
	Use Case:  Using a decorator to execute a function object and also get information about other function objects
	in the module and execute it too.
'''


'''
	execute is a function decorator, it actually takes functions as input and performs operations and executes it on return
	While it does to, we can access the information of the module where the input function resides...

	Let's say i have 5 different functions in another module, and we are using @execute decorator to execute 1 of the function
	While 1 function is taken as an input, we can actually execute all of th functions in that module by accessing the func_globals
	attribute of the function object
'''


def execute(func):

	'''
		Execute the function and return the result
	'''

	def reporter(*args,**kargs):

		print "Sum - " , func.func_globals.__getitem__('sum')(*args,**kargs) # Execute sum
		print "negate - "  , func.func_globals.__getitem__('negate')(*args,**kargs) # Execute negation
		prd = func(*args,**kargs) # Execute Product
		print "prd - ", prd
		return prd

	return reporter


