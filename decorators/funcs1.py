
'''

	 Function are first class objects in python, they can passed as a parameters, be assigned to a variable, manipulated @ runtime etc...
	 We will see the function and inner function basics
	 In Python there are 2 keywords that can create a function object, namely - def & lambda

'''


'''
	Function Basics: The Outer and Inner function calls
'''

# Access the value of the internal function - A Closure, I want to know what function bar() returns

def foo():
	def bar():
		return ' The Foobar'
	return bar

# print foo() will actually return the function bar not the result of bar

print foo() # this is same as foo.__call__()

'''
	Extract from Output Window:

	<function bar at 0x000000000233DBA8>	
'''
# If I want to know the resulf of bar, I actually have to call bar function

print foo()() # this is same as foo.__call__().__call__()


'''
	Extract from Output Window:

	The Foobar

'''

# Now let's have 1 outer and 2 inner functions


def foo():
	def bar():
		def bravo():
			return ' Practice makes your core perfect!'
		return bravo
	return bar

# So now we have 3 levels of call functions that could give us the expected value
print foo()()() # this is same as foo.__call__().__call__().__call__()


'''
	Extract from Output Window:

	Practice makes your core perfect!
'''


# Now let's examine the dictionary

print foo.__dict__ # prints empty


# Let's us add parameters to our functions - Parameters of the outer scope are accessible on the inner scope also

def foo(getMeaFoo):
	def bar(theBar):
		assert getMeaFoo.__class__ == str # type checking - p.s. getMeaFoo.__class__ is same as type(getMeaFoo)
		assert theBar.__class__ <> float # type checking - p.s.  theBar.__class__ is same as type(theBar)
		return getMeaFoo + ' '+theBar
	return bar

print foo("Arun loves")("Foobar !")

'''
	Extract from Output Window:

	Arun loves Foobar !	
'''


# Let us say you want pass the parameter to the inner function directly!
hru = 'How are you !'
def foo(getMeaFoo):
	def bar(theBar):
		assert getMeaFoo.__class__ == str # type checking - p.s. getMeaFoo.__class__ is same as type(getMeaFoo)
		assert theBar.__class__ <> float # type checking - p.s.  theBar.__class__ is same as type(theBar)
		return getMeaFoo + ' '+theBar
	return bar(hru)

'''
	-> When foo("Hello Arun! ") is called it calls the function foo with "Hello Arun! " as a parameter.
	-> Function foo return function bar, hence it internally calls bar(hru = 'How are you !')
	-> bar function gets called and bar(theBar) becomes bar('How are you !')
	-> bar function does assertion and returns getMeaFoo + ' '+theBar -> 'Hello Arun! How are you !'
'''

print foo("Hello Arun! ")



'''
	Asssignment of function object to a variable
'''

varx = foo # Function object foo is stored in varx
print varx
print varx('Hello Arun ! ')


vary = foo # Function object foo is stored in vary
print vary
print vary('Hello Arun Ji! ')

print id(varx) , id(vary), id(foo)

del foo # Even if foo is deleted, it's variables will still work and execute the function

print varx
print varx('Hello Arun ! ')
print vary
print vary('Hello Arun Ji ! ')
