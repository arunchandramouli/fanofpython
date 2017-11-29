"""
	Use Case:  Exploring the User defined Class 
	Accesing all the callable attrs
"""


from klass3 import Masters
import types


"""
	Write a function to fetch the attrs of a class, sets it to other class
"""

def func_fetch_attrs(klassname,borrowerclass):

	"""
		Fetching class attrs
		:param klassname - Class Object
		:param borrowerclass - Class to which the attributes are to be patched
	"""

	try:
		

		for key , val in vars(klassname).items():

			if not (type(val) == types.IntType or type(val) == types.StringType):
				
				if not str(key) in ("__init__","__doc__","__dict__","__weakref__"):

					setattr(borrowerclass,key,val)

	except Exception as e:
		raise
	


if __name__ =="__main__":

	for i in func_fetch_attrs(Masters): print i