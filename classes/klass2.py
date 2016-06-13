'''
	Use Case:  Exploring the User defined Class
'''



# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


	#__slots__ = ['_foo'] # limit the Attrs

	# Declaring Class level Attrs - visible for class and it's instance

	Arun,Allison,Mark,__private= 'Python','Python','C++','You cant access me !'

	def __init__(me):

		me._foo = me.__class__.__name__

	def instanceMethod(this):

		print this.Arun,this.Allison,this.Mark
		return ' Hello - I am an Instance Method'


	@classmethod
	def klassMethod(that): # that has no clue whatsoever about instance specific _foo

		print that.Arun,that.Allison,that.Mark		
		return ' Hello - I am a Class Method'


	@staticmethod
	def staticMethod(nothingHere): # There is no positional param for static method, if specified must be given value by the uer

		return ' Hello - I am a Static Method'


	@property
	def foo(they):
		return they._foo
	
	@foo.setter
	def foo(them,someThingFooish):
		them._foo = someThingFooish


# Now Examine the Class

print UserDefined # prints class object

# Create an Instance

anInstance = UserDefined()
print anInstance # prints instance of a class

# Access the Property - they are not callable
print UserDefined.foo # returns property object not the value, since we are calling via the class

# Access the Property - they are not callable
print anInstance.foo # returns value, since we are calling via the instance of the class


# set a value for a property and call them again


anInstance.foo = 'Geekish is better than Nerdish! ? '
UserDefined.foo = 'Geekish is better than Nerdish!'

print anInstance.foo # returns value, since we are calling via the instance of the class
print UserDefined.foo # returns value, rebinding outside the class!


# Call the class level variables # They are not callable - they are accessible inside instance and class methods

print UserDefined.Allison, UserDefined.Arun, UserDefined.Mark

print anInstance.Allison, anInstance.Arun, anInstance.Mark


# Call the private attributes of the Class

#print UserDefined.__private # we cant access it directly, but there is a way!

print UserDefined._UserDefined__private # returns value


print UserDefined.__dict__