'''
	Use Case : Exploring User defined Class

	Define a Base class with @classmethod and access it in the sub-class

	- Here we are using classmethod as an alternate constructor
'''



''' Defining a Base class with 3 different types of methods '''

class MyBase(object) : # New Style Class


	'''
		Define a constructor that takes a string as an argument
	'''

	def __init__(instance,astring):

		'''
			Parameter 
				instance -> Instance of the class MyBase
				container -> An Iterable passed to the constructor
		'''

		instance.astring = astring


	''' Define a  classmethod to join the string and return '''	

	@classmethod
	def join_string(klass,container):

		''' Create an instance and instantiate '''
		
		gets = klass("") # Instantiate
		gets.astring = '-'.join(s for s in container)
		return gets


	''' Use __str__ to print the value instance.astring '''

	def __str__(instance):

		return "String value is %s "%instance.astring


''' Create a sun-class of class MyBase '''
class Sub_of_MyBase(MyBase):


	''' Use __str__ to print the value instance.astring '''

	def __str__(instance):

		return "From Class Sub_of_MyBase - String value is %s "%instance.astring




#Create an instance of class MyBase

instance_new_MyBase = MyBase('xyz')

print instance_new_MyBase

value = instance_new_MyBase.join_string("Hello World")

print value

# Access join_string of base class directly
get_val = Sub_of_MyBase.join_string("Python Programming")
print get_val
