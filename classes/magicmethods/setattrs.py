'''
	Use Case: To prevent the User from creating any additional attributes for the class. Only the attributes
	that are initialized during the instance creation are to be used and accessed.

	Why we need this: This is a replacement for __slots__. No additioanl attributes allowed.

	How do we do it? Inside the body of the class we override the __setattr__ magic method

'''


# Class LimitedAttrs

class LimitedAttrs(object):

	# Initialize the attributes

	def __init__(instance,age,location):
		instance.myAge = age
		instance.myLoc = location

	# Overide __setattr__

	def __setattr__(instance,name,value):

		if name in ['myAge','myLoc']:

			object.__setattr__(instance,name,value)
		else:
			raise AttributeError("Attribute '%s 'is not recognized! "%name)

# Instance

getLimited = LimitedAttrs(30,'MUM')
getLimited.myLoc = 'Chennai' # valid
#getLimited.age = True # AttributeError: Attribute 'age 'is not recognized!



'''
	Use Case: Explore __setattr__ and populate instance dictionary
'''

class Setattr(object): # New Style Class

	def __setattr__(instance,name,value):
		

		'''
			Aim: To set a value for an attribute
			The __setattr__ gets invoked only for instances of class Setattr
			*** Attributes that are set as class attrs will not pass through this magic call ***
			By default this method will get called even if not defined inside the class body!
		'''

		print ' instance = %s , name = %s , value = %s , class = %s '%(instance,name,value,instance.__class__)

		return super(Setattr,instance).__setattr__(name,value ) # We are actually setting the value for an attribute and it gets stored in the instance dictionary.


if __name__ == '__main__':
		
	'''
		Create an Instance
	'''

	objectSetattr = Setattr()

	Setattr.names = 'Tim' # won't pass through __setattr__

	objectSetattr.name = 'Tim Peters!' # will pass through __setattr__

	print objectSetattr.__dict__, '\n\n', Setattr.__dict__, '\n\n'