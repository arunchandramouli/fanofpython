import datetime

'''
	 Function are first class objects in python, they can passed as a parameters, be assigned to a variable, manipulated @ runtime etc...
	 We will see the function and inner function basics
	 In Python there are 2 keywords that can create a function object, namely - def & lambda

	 Decorators are a concept actually, they take a function as an input, manipulate it and return it's output.
	 For Example - @classmethod is a decorator, that takes a function and converts it as a classmethod
	 You must @ first understand whats the need for it?? 
	 Its simple, manipulates/asserts/validates/add/delete attributes etc.. in your function
	 and we can think of many more situations.

'''

'''
	Now Let's say I have a decorator that returns the time taken for a function to perform
	I am also using the print keyword to highlight
'''

def theRunner(func):
	def argsPassed(*args,**kargs):

		# Function name
		print "Function name - %s "%func
		print "Arguments %s %s "%(args,kargs) # Arguments passed to the function will be listed here
		# Store the result in the variable
		result = func(*args,**kargs) # Executing the Function
		# Print the result
		print 'Result is %s '%result
		print 'Manipulated Result is  - %i' %(result + 1000) # The Decorator can manipulate/modify the result of a function!
		return result # Return the result of the function
	return argsPassed # Return the Function - Do not return as argsPassed() - it will result in recursion since a function calls itself

'''
	Apply the Decorator theRunner to the function below!
'''
@theRunner
def theFunc(inta,intb):
	
	'''
		Add inta and intb and return the result
	'''
	return inta + intb # This is the value to be returned by the decorator - theRunner


# Now Lets us execute the function
theFunc(100,2000) # same as theFunc.__call__(100,2000) a function is callable :-)


'''
	Extract from Output Window:

	Function name - <function theFunc at 0x0000000002691C88>
	Arguments (100, 2000) {}
	Result is 2100
	Manipulated Result is  - 3100	
'''

# Now lets the signature
# It will print argsPassed since the func - "theFunc" is decorateed by the func - "theRunner", this will be dealt in next examples - refer deco2.py
print theFunc.__name__ 
