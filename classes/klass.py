'''
	Use Case:  Exploring the User defined Class
'''



# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


	# Declaring Class level Attrs - visible for class and it's instance

	Arun,Allison,Mark = 'Python','Python','C++'

	def __init__(me):

		me._foo = me.__class__.__name__

	def instanceMethod(this):

		return ' Hello - I am an Instance Method'


	@classmethod
	def klassMethod(that): # that has no clue whatsoever about instance specific _foo

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


'''
/*** Accessing an Instance Method of a Class ***/
'''

# How to access the instance method of a class - Answer is via Instance of a class

print anInstance.instanceMethod.__call__() # same as -- anInstance.instanceMethod()

# Access an instance method of a class

print UserDefined.instanceMethod.__get__(UserDefined,UserDefined).__call__() # Use a descriptor


print UserDefined.instanceMethod.__func__.__call__(UserDefined) # Convert to function and call


'''
/*** Accessing a Class Method of a Class ***/
'''

# A Class method can be accessed via both instance and the class directly.
# Instance specific attributes are not visible for class methods

# Call via class directly

print UserDefined.klassMethod.__call__() 

# Call via instance

print anInstance.klassMethod.__call__()

print UserDefined.klassMethod.__get__(UserDefined,UserDefined).__call__() # Use a descriptor


print UserDefined.klassMethod.__func__.__call__(UserDefined) # Convert to function and call



'''
/*** Accessing a Static Method of a Class ***/
'''

print UserDefined.staticMethod(False) # same as UserDefined.staticMethod.__call__(False)

print anInstance.staticMethod(False) # same as UserDefined.staticMethod.__call__(False)

# Use a descriptor and the static method becomes a bound method, hence you don't need to pass parameter explicitly
print UserDefined.staticMethod.__get__(UserDefined,UserDefined).__call__() 



'''
	At run time how do you determine the type of method as instance/class/static
'''

# Explore Instance Methods
print UserDefined.instanceMethod.im_self # returns None
print UserDefined.instanceMethod.im_class # returns class object
print UserDefined.instanceMethod.im_func #  returns function object


# Explore Class Methods
print UserDefined.klassMethod.im_self # returns class object
print UserDefined.klassMethod.im_class # returns type
print UserDefined.klassMethod.im_func #  returns function object



# Explore Static Methods
# A static method doesn't have im_self / im_class / im_func, but has many more ... that instance and class mets doesn't

'''
func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name'
'''