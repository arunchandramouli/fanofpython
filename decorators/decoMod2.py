'''
	Use Case:  Using a decorator to execute a function object and also get information about other function objects
	in the module and execute it too.
'''

import decoMod1

@decoMod1.execute
def product(param1,param2):

	'''
		Sample Func: Compute the Product
	'''

	return param1 * param2 


def sum(z = None,s = None):

	'''
		Sample Func: Compute the Sum
	'''

	return z  +  s 



def negate(param1,param2):


	'''
		Sample Func: Compute the Negation
	'''
		return param1  -  param2 

product.__call__(100,10)