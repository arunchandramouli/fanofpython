
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
	

	An example of global and non-local
'''

global_me = "Arun Chandramouli"
INT_POWER = 1000
FLOAT_POWER = 1000.124
BOOL_VAL = True



'''
	A Simple and cool closure ..
'''

def whatdhecksglobal():

	print "global_me Outer {0} ".format(global_me),'\n\n'

	outer_someValue = "Beauty and the Beast"

	print "From Outer " , outer_someValue , id(outer_someValue),'\n\n'

	''' Not permitted 

	FLOAT_POWER += 2000.459

	'''

	'''
		Solution Use Global
	'''

	global FLOAT_POWER
	print "FLOAT_POWER before modification %s and %s "%(FLOAT_POWER,id(FLOAT_POWER)),'\n\n'

	FLOAT_POWER += 2000.459
	print "FLOAT_POWER before modification %s and %s "%(FLOAT_POWER,id(FLOAT_POWER)),'\n\n'
	
	def idoseethings():

		print "global_me {0} ".format(global_me),'\n\n'


		'''
			print "From inner " , outer_someValue , id(outer_someValue),'\n\n'
			This print will raise an exception ,it will think that outer_someValue
			is the name binding in the line below and thus will not take
			the outer one

		'''


		''' Change the value of outer scope '''

		outer_someValue = "Hitler and the Jews "


		''' 
			Not permitted 

			outer_someValue += "Hitler and the Jews "

			We didnt define outer_someValue inside the block of idoseethings hence cant be altered

		'''

		'''
			Change the global value

			INT_POWER += 200 will raise an error for the same reason said above
		'''


		'''
			Solution
		'''
		global INT_POWER

		print "INT_POWER before modification %s and %s "%(INT_POWER,id(INT_POWER)),'\n\n'
		INT_POWER += 200
		print "INT_POWER after modification %s and %s "%(INT_POWER,id(INT_POWER)),'\n\n'


		print "From inner " , outer_someValue , id(outer_someValue),'\n\n'


		return True

	return idoseethings





if __name__ == "__main__":

	# ************************************************************************************** #
	
	whatdhecksglobal()()