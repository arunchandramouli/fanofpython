

import logging
import datetime

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a plain decorator to execute a function

	
'''


''' 
	A Decorator to make sure a Class contains only one instance at any given point of time
'''

def instance_validator(func):

	validate_instance = {}

	def inner(*args,**kargs):

		if not bool(validate_instance):

			instance = func(*args , **kargs)
			validate_instance.__setitem__(func,instance)

			print validate_instance

			return instance

		print validate_instance

		return validate_instance.__getitem__(func)

	return inner


'''

	Define a Simple Class
'''
@instance_validator
class Alpha(object):
	

	def __init__(instance , *args):

		instance.x = args


	def instancemethod(instance):

		return "I am an instance method"


	@classmethod
	def classmethod(klass):

		return "I am a Class Method"


	@staticmethod
	def staticmethod():

		return "I am a Static Method"


if __name__ == "__main__":

	
   instance_x = Alpha()
   instance_y = Alpha()
   instance_z = Alpha()

   print id(instance_x) , id(instance_y) , id(instance_z),'\n\n'

