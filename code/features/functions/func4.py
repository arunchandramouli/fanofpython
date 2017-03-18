
from functools import wraps, partial
import logging


'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a function and access it.. In Simple Words, a function can 
	take a set of arguments as an input, and return the calculated result

	It can be used to perform repetitive actions

	Here we will analyze the globls and locals which are both builtin

	If a variable is being used inside a block without being defined there
	that variable is known as Free Variable
	
'''


'''
	Let's start with a simple closure

'''


'''

	globals - Specific to an entire module
	locals -  Specific to a block of code alone

'''

'''
	Lets define a global variable 
'''

winter = True 
ages = [21,23,24,26,27]
kids_name = ("Anne","Mary","Priya","Joey","Samuel","Abraham")


'''

	Define funcA that takes a tuple and does something in the inner function - closure

'''

def funcA(*args):
	
	print '\n\n\n\n\n'
	print "Inside funcA ...",'\n\n\n\n\n'

	''' Define a local variable here and it shall be added to locals dict '''
	funcALocal = "My Lord ... "

	print winter , ages , kids_name,'\n\n\n'


	print globals(),'\n\n\n\n',locals(),'\n\n\n'


	def funcB():

		''' Print locals and globals '''

		print '\n\n\n\n\n'
		print "Inside funcB ...",'\n\n\n\n\n'


		''' Define a local variable here and it shall be added to locals dict '''

		''' A variable declared in the outer scope is accessible in the inner scope '''

		funcBLocal = "My Way ... "

		print winter , ages , kids_name,'\n\n',funcBLocal,funcALocal,'\n\n\n'


		''' 
			
			Here we are taking a tuple as an argument in the outer function 
			and we are accessing it in the inner

			A Global dictionary will contain anything and everything global,
			say module level imports and other attributes such as classes, functions,
			variables that are accessible globally... it will not contain
			anything specific to an attribute such as function or class etc...

			For eg : We are having a parameter *args , funcA(*args)
			This args will not be shown in the globals dictionary but in the locals

		'''


		'''
			 ******************************************************************************************** 
				 
				 	Note :: 

				 	 The most important point to note here is that I am able to access
				 	 args that was passed as an argument to an outer function
				 	 only because it is part of the locals() dict.

				 	 So if it's gonna be part of globals() and locals() we can access them all.
		

			 ******************************************************************************************** 
		'''

		
		result = [f+1000 for f in args]

		print globals(),'\n\n\n\n',locals(),'\n\n\n'

		return result

	return funcB



if __name__ == "__main__":

	
	# ************************************************************************************** #
	

	print funcA(100,200,300,4005,5000)()


	# ************************************************************************************** #
