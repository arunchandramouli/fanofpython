'''
	Use Case: Catch undefined attributes inside __getattr__
	The magic call to __getattr__ gets invoked only for attributes not available in the instance dictionary
'''

class GetattrDemo(object): # New Style Class


	# Initialize the attributes

	def __init__(instance,fname,age,location):
		instance.fname = fname
		instance.myAge = age
		instance.myLoc = location

	# A call to this method will get into __getattr__ but if it were a classmethod it wouldn't
	def returns(self):

		return self.age

	# A call to this method will not flow into __getattr__ eventhough self.age is not a valid attribute
	@classmethod
	def returnsomething(self):

		return self.age

	def __getattr__(instance,name):
		

		'''
			Aim: To set a value for an attribute
			The __setattr__ gets invoked only for instances of class Setattr
			*** Attributes that are set as class attrs will not pass through this magic call ***
			By default this method will get called even if not defined inside the class body!
		'''

		print ' instance = %s , name = %s , class = %s '%(instance,name,instance.__class__)

		try:
			# Trying to get the attribute value, __getattribute__ is thedefault gateway
			return super(GetattrDemo,instance).__getattribute__(name) 

		except AttributeError:

			raise AttributeError(' Attribute  "%s" is invalid ! '%name)


if __name__ == '__main__':

		
	'''
		Create an Instance
	'''

	objectGetattr = GetattrDemo('Alice',30,'Wonderland')

	print objectGetattr.fname # will not pass through __getattr__
	print objectGetattr.myAge # will not pass through __getattr__
	print objectGetattr.myLoc # will not pass through __getattr__	
	#objectGetattr.returns()	#  ***** will pass through __getattr__
	#print objectGetattr.name # ***** will pass through __getattr__
	print objectGetattr.returnsomething()