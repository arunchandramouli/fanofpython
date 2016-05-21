

'''
	Use Case: Demostrate the different scenarios with functions

	Show how to create and manipulate functions on the fly	
'''

'''
	I have a function and I want to create a copy of that function and 
	change the default parameters values
	Note :- If you use copy module it creates a copy of that and it refers 
	to the similar memory location

'''

# A Simple function!

def funcA(x=100,y=200):
	return x+y

'''
 	A metafunction that creates a copy of a function at a new memory location.

 	The need is to apply patching for a function @ run-time and change it's attributes.

'''
def copyDfunction(func,defaults):

	difffuncs = type(func)
	
	func_new = difffuncs(func.func_code,
		func.func_globals,
		func.__name__,
		defaults,
		func.__closure__)

	func_new.__doc__ = func.__doc__
	return func_new


defaultVals = ('x','y')

print copyDfunction(funcA,defaultVals).func_defaults


# Is function callable, let's Try

def funcB():pass
print funcB.__call__() # same as funcB()

# Is function hashable?? Can it be used as a Dict key??

print hash(funcB) # Yes
dictA = dict(funcB=True,funcOuter = False) # Yes


# Exploring Function object

def funcOuter(x,y):

	print ' funcOuter -- '
	def funcInner():
		print ' funcInner-- '
		dictA.__setitem__('funcInner',True)
		return True
	return funcInner

#print funcOuter
#print funcOuter()
#print (funcOuter.func_code,"\n\n",funcOuter.func_globals,"\n\n",
#funcOuter.__name__,"\n\n",funcOuter.func_defaults,"\n\n",funcOuter.__closure__) # try similarly for funcOuter() i.e. funcInner

# Exploring func_code i.e. the Code Object

#print funcOuter.func_code # returns the Code object! which is produced by the Compiler and the bytecode which the interpreter actually executes is an attribute of it.

# Execute the Code object and the function gets executed . *** Code object is not a callable ***

exec funcOuter(1000,2000).func_code # It will print ' funcOuter -- ' 
exec funcOuter(100,200).func_code # It will print ' funcOuter -- ' ' funcInner -- ' 
print dictA # Dictionary is updated :-) that means inner function is executed



# Explore Code object and see what's actually inside

print dir(funcOuter.func_code)

'''
	Output is as follows;

	['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', 
	'__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', 
	'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
	'__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 
	'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
'''


'''
	Let's examine the following
	'co_argcount', 'co_cellvars', 'co_code', 'co_consts',
	'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 
	'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames'
'''

# Get the bytecode

print funcOuter.func_code.co_code, funcOuter.func_code.co_code.__class__