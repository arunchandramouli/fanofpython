
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")



'''
	Analyze the metadata of a function in detail
'''


'''
	A Simple function with a Closure
'''

def funcA(*args):

	def funcA__inner():

		return args # Returns a Tuple

	return funcA__inner




''' Calculate the sum of numbers '''


def calculate(x,y,z=100):


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

	'''


	core_logger.info("Function Class - %s "%calculate.__class__)
	core_logger.info("\n\n\n\n")


	core_logger.info("Function Name - %s "%calculate.__name__) # same as calculate.func_name
	core_logger.info("\n\n\n\n")


	core_logger.info("Function Doc Info - %s "%calculate.__doc__)# same as calculate.func_doc
	core_logger.info("\n\n\n\n")

	core_logger.info("Function Defaults - %s "%calculate.__defaults__)# same as calculate.func_defaults
	core_logger.info("\n\n\n\n")

	core_logger.info("Function Globals - %s "%calculate.__globals__)# same as calculate.func_globals
	core_logger.info("\n\n\n\n")



	''' Function dict remains empty unless we assign it something '''

	core_logger.info("Function Dict - %s "%calculate.__dict__)# same as calculate.func_dict
	core_logger.info("\n\n\n\n")


	''' Lets assign it something '''

	calculate.me = 10000000


	''' Function dict remains empty unless we assign it something '''
	
	core_logger.info("Function Dict - %s "%calculate.__dict__)# same as calculate.func_dict
	core_logger.info("\n\n\n\n")


	core_logger.info("Function Closure - %s "%funcA(1,2,3,4,5).__closure__[0])
	core_logger.info("\n\n\n\n")


	core_logger.info("Function Closure Cell Contents ")
	core_logger.info(funcA(1,2,3,4,5).__closure__[0].cell_contents)
	core_logger.info("\n\n\n\n")


	# ************************************************************************ #

