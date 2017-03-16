
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")



'''
	Analyze the metadata of a function in detail . Explore func code - Code objects

	***** Assigning the Code object of one function to another will
	change the way the function works ******

	for eg : If we have 2 functions, say funcA and funcB , if we assign code object of funcBto funcA
	then funcA will be expected to work similar to funcB
	
'''


'''
	A Simple function with a Closure
'''

def funcA(*args):

	def funcA__inner():

		return args # Returns a Tuple

	return funcA__inner




''' Calculate the product of numbers '''

def calculatePRD(x,y,z,w):


	''' 
		Perform arithmetics on the given inputs

		Parameters :
			x -> int
			y -> int
			z -> int
			return -> int (x * y * z)
	'''

	
	return x * y * z
    


''' Calculate the sum of numbers '''

def calculate(x,y,z=100,*args,**kwargs):


	''' 
		Perform arithmetics on the given inputs

		Parameters :
			x -> int
			y -> int
			z -> int
			return -> int (x+y+z)
	'''
	a = b = c = 10000
	
	return x + y + z
    

if __name__ == "__main__":

	# ************************************************************************ #


	''' Executing the function '''


	'''

	when we do dir(functionobject) this is what we get ;

	['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', 
	'__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
	 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']


	 when we do dir(codeobject) this is what we get ;


	['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
	'__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
	'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 
	'co_nlocals', 'co_stacksize', 'co_varnames']

	'''

	 # A code object is the most important attribute of a function

	core_logger.info("Function Code Object %s "%calculate.__code__)
	core_logger.info("\n\n\n\n\n")


	'''
		Let us get into the attributes of a function code one by one
	'''

	# Return the name of the file

	core_logger.info("File Name %s "%calculate.__code__.co_filename)	
	core_logger.info("\n\n\n\n\n")

	
	# Return the code object byte code
	
	core_logger.info("Code Object co_code %s "%calculate.__code__.co_code)	
	core_logger.info("\n\n\n\n\n")

	# Return the name of the function
	
	core_logger.info("Code Object co_name %s "%calculate.__code__.co_name)	
	core_logger.info("\n\n\n\n\n")


	# Return the names
	
	core_logger.info("Code Object co_names ...")	
	core_logger.info(calculate.__code__.co_names)	
	core_logger.info("\n\n\n\n\n")

	# Return the total n.o. arguments

	core_logger.info("Code Object - Total n.o. arguments ")
	core_logger.info(calculate.__code__.co_nlocals)	
	core_logger.info("\n\n\n\n\n")

	# Return the names of the arguments

	core_logger.info("Code Object - Names of the arguments ")
	core_logger.info(calculate.__code__.co_varnames)
	core_logger.info("\n\n\n\n\n")


	# Return the freevars

	core_logger.info("Code Object - Freevars ")
	core_logger.info(calculate.__code__.co_freevars)
	core_logger.info("\n\n\n\n\n")

	# Return the default argument details

	core_logger.info("Default Arguments ")
	core_logger.info(calculate.__defaults__)
	core_logger.info("\n\n\n\n\n")


	# ************************************************************************ #