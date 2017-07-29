

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



''' A Decorator to execute the methods of the class '''

def execute(func):

	def inner(*args,**kargs):

			core_logger.info("Executing function - %s "%func.__name__)
			start = datetime.datetime.now()
			result = func(*args , **kargs)
			end = datetime.datetime.now()
			core_logger.info("Result == %s "%result)

			core_logger.info("Total time taken %s "%(start-end))

			return result

	return inner



'''
	A Decorator to apply above decorator - execute to all methods of the class
'''


def apply_class_decorator(klass):

	def inner(*args , **kwargs):

		for key , value in vars(klass).items():

			try:

				setattr(value,key,execute)

			except AttributeError as I:
				
				continue

		return klass

	return inner


'''

	Define a Simple Class
'''

@apply_class_decorator
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

   print instance_x ,'\n' ,instance_x.classmethod() #,'\n',instance_x.staticmethod(),'\n'
