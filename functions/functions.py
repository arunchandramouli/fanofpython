'''
	Use Case: Demostrate the different scenarios with functions

	Show how to create and manipulate functions on the fly

	Explore function objects in detail!

	Note : Please uncomment all the print statement to view output

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

# Set the default values for the function
defaultVals = ('x','y')

makeCopy = copyDfunction(funcA,defaultVals) # Create a copy and store it in a variable!
##print "Copied function ---> makeCopy  ",makeCopy, '\n\n'

'''
	Output:
		makeCopy   <function funcA at 0x00000000011FAC18>
'''

# Now let's  check the memory address of makeCopy and funcA, they will be different...
# If you are using copy module it will generate a new function @ same location only!

##print 'Address of funcA --> {0} and address of makeCopy --> {1}'.format(id(funcA),id(makeCopy)),"\n\n"

'''
	Output:
		Address of funcA --> 21146424 and address of makeCopy --> 21146648
'''
# Is function callable, yes it is!
##print funcA.__call__

'''
	Output:
		<method-wrapper '__call__' of function object at 0x000000000133AB38>
'''

# Is function hashable?? Can it be used as a Dict key??
##print 'funcA hash key! ' .format(hash(funcA)) ,'\n\n' # Yes

'''
	Output: 20163384
'''
dictA = dict(funcA=True,funcOuter = False) # Yes


# Exploring Function object

def funcOuter(x,y):
	z = 1000 # Local to the function
	##print ' funcOuter -- '
	def funcInner():
		##print ' funcInner-- '
		dictA.__setitem__('funcInner',True)
		return
	return funcInner

###print funcOuter
###print funcOuter()
###print (funcOuter.func_code,"\n\n",funcOuter.func_globals,"\n\n",
#funcOuter.__name__,"\n\n",funcOuter.func_defaults,"\n\n",funcOuter.__closure__) # try similarly for funcOuter() i.e. funcInner

# Exploring func_code i.e. the Code Object

###print funcOuter.func_code # returns the Code object! which is produced by the Compiler and the bytecode which the interpreter actually executes is an attribute of it.

# Execute the Code object and the function gets executed . *** Code object is not a callable ***

exec funcOuter(100,200).func_code # It will ##print ' funcOuter -- ' ' funcInner -- '
###print dictA # Dictionary is updated :-) that means inner function is executed



# Explore Code object and see what's actually inside

###print dir(funcOuter.func_code)

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
###print funcOuter.func_code.co_code, funcOuter.func_code.co_code.__class__

# Get the argcount - How many args were passed?
###print funcOuter.func_code.co_argcount # There are 2 args hence it will show as 2

# Get the co_cellvars
'''
	 returns local variables used in the function if you return it.. but since we use
	 exec here it is not quite possible, since it doesn't allow any free variables
	 our function funcOuter has a local variable 'a', but i didnt make use of it and return it hence it
	 is not shown in the tuple co_cellvars
'''
###print funcOuter.func_code.co_cellvars

# Get the co_consts
###print funcOuter.func_code.co_consts # returns the literals being used by the bytecode; for eg: 2+2 , (2,2) are literals


# Get the co_filename
#print funcOuter.func_code.co_filename # returns the filename i.e. functions.py

# Get the co_firstlineno
# returns the line n.o. at which the function starts @ this source file!. 
# In this case funcOuter starts @ line n.o. 77
#print funcOuter.func_code.co_firstlineno 

# Get the Flags
#print funcOuter.func_code.co_flags # Returns an integer encoding a number of flags for the interpreter. 67

# Get the co_freevars
#print funcOuter.func_code.co_freevars # Returns the names of the free variables

# Get the function name
#print funcOuter.func_code.co_name # returns funcOuter

# Get the names used by the bytecode
#print funcOuter.func_code.co_names

# Get the total no.o arguments used by the function

#print funcOuter.func_code.co_nlocals # returns 


# Get the names of the local variables used in the function, including arguments
#print funcOuter.func_code.co_varnames # returns ('x', 'y', 'z', 'funcInner')

# Get the Stack Size
#print funcOuter.func_code.co_stacksize # Returns the required stack size