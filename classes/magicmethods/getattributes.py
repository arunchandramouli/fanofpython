'''
	Use Case:  The magic call to __getattribute__ gets invoked as a default gateway for attribute access
'''

class Getattribute(object): # New Style Class


	# Class level Attributes

	globalset, localSet = False, False

	# Initialize the attributes

	def __init__(instance,fname,age,location):
		instance.fname = fname
		instance.myAge = age
		instance.myLoc = location

	# A call to this method will not flow into __getattr__ eventhough self.age is not a valid attribute
	#@classmethod
	def returnsomething(self):

		return self.fname,self.myAge, self.myLoc

	def __getattribute__(instance,name):
		

		'''
			Aim: To check the default attribute access
			The __getattribute__ gets invoked only for accessing instance attributes
			It is available only for new style classes
			Class level attributes such as defined above will also pass via this gateway.
			*** By default this method will get called even if not defined inside the class body. ***
		'''

		# The below print statement will result in infinite recursion 
		# instance.__class__ internally calls __getattribute__ , a function executing itself inside it's body!
		#print ' instance = %s , name = %s , class = %s '%(instance,name,instance.__class__)

		print ' instance = %s , name = %s '%(instance,name)

		try:
			# Trying to get the attribute value, __getattribute__ is the default gateway
			# If you override this and add some condition for access, it will affect the attributes of the class
			return super(Getattribute,instance).__getattribute__(name) 

		except AttributeError:

			raise AttributeError(' Attribute  "%s" is invalid ! '%name)


if __name__ == '__main__':

		
	'''
		Create an Instance
	'''

	objectGetattr = Getattribute('Annabelle',28,'England')

	print objectGetattr.fname
	print objectGetattr.myAge
	print objectGetattr.myLoc
	print objectGetattr.returnsomething()
	print objectGetattr.globalset
	print objectGetattr.localSet
	#print objectGetattr.fnameLname # will raise attribute error