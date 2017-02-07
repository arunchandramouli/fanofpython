
from functools import wraps, partial
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a function and access it partially
	
'''

def calculate(x,y,z):

	return x + y * z
    

if __name__ == "__main__":

	# ************************************************************************************** #
	
	#calculate(10,20) # This will result in an error since function calcualte has 3 parameters

	get_func = calculate(10,20)
	print get_func

	# ************************************************************************************** #

