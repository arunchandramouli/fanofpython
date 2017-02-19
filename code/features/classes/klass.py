'''
	Use Case:  Exploring the User defined Class

	A User can define any n.o. classes

	A Class is a repository of attributes, which are Callable and Non-Callabe

	Callable means able to access () - for eg - UserDefined.instanceMethod()

	Non - callable attributes are those which are called without () - for eg UserDefined.a,UserDefined.b

	A class also holds the built-in special methods such as __init__ and many more....


	All the methods of a class are callable,

		There are 3 kinds of methods;

			-> Instance Methods -> First argument is the positional, gets converted as an instance @ run-time
			-> Static methods  -> No positional arguments
			-> Class Methods -> First argument is the positional, gets converted as a class object @ run-time

	
	Why we need Instance Methods?

		-> 	Facilitate instance creation and ability to access certain methods via instances alone
		->  Make instance specific attributes accessible inside the instance methods
		->  Can access all the attributes of the class, methods, class variables, instance specific variables...		
		->	* Takes first argument as a Class Instance ,which is a mandate
	
	Why we need Class Methods?

		-> * Takes first argument as a Class object which is a mandate
		-> Doesn't depend on the instances of the class
		-> Favors advantages while inheriting the parent class 

	
	Why we need Static Methods?

		-> * Doesn't take any first argument as a mandate positional parameter
		-> Makes you feel a function inside the class
		-> Can be used in many ways to pass data
		-> Perform some tasks that is not dependent on the instance or the class
		-> Can be accessed by both the instance of the class and the class

'''



''' Define an User defined class - Masters '''

class Masters(object): # A new-style class inherits from object


	''' 
		
		instance_Method is an instance method , meaning it is callable via an instance
		for eg; instance.instance_Method()

		Internally this call instance.instance_Method() gets converted as Masters.instance_Method(instance)

		*** 
			Naturally instance methods are called via instance, if called via class it will raise an error

			For eg; calling Masters.instance_Method() will raise an error, since instance methods are
			meant to be called only by an instance.

			This is the concept of being bound and unbound

			An instance method is always tied and bound to an instance

		***

	'''
	def instance_Method(this):

		''' 
			Parameter "this" gets converted as an instance @ run time
			hence instance_Method will become accessible
		'''

		return ' Hello - I am an Instance Method'



	''' 
		
		klass_Method is a class method , meaning it is callable via a class and also an instance
		for eg; Masters.klass_Method() and instance.klass_Method()

		Internally this call Masters.klass_Method() gets converted as Masters.klass_Method(Masters)

		*** 
			Naturally instance methods are called via instance, if called via class it will raise an error

			For eg; calling Masters.instance_Method() will raise an error, since instance methods are
			meant to be called only by an instance.

			But class methods are accessible via both class directly, as well as an instance

			This is the concept of being bound and unbound

			An instance method is always tied and bound to an instance

			A Class method is bound to a class, but accessible via an instance too
			
			It is defined as @classmethod

			Note - Having all class methods in a class prevents the need for any instance

			Instance specific attributes that are defined inside __init__ block wont be accessible to classmethods
			unless and until specified for the class

		***
	'''
	
	@classmethod
	def klass_Method(that): 

		'''
			Parameter "that" gets converted as a class object @ run time
			hence it is accessible directly via a class
			For eg: Masters.klass_Method()
		'''

		return ' Hello - I am a Class Method'

	''' 
		A Static method is as good as a function , no positional arguments are needed

		It can be accessed via an instance , as well as a class.

		It gets converted as a function @ run time  .... *** A Static method is neither bound nor un-bound, it is only a function ***

		It is defined as @staticmethod

	'''
	@staticmethod
	def static_Method(): # No positional arguments

		return ' Hello - I am a Static Method'


if __name__ == '__main__':

	# Now Examine the Class

	# Create an Instance of class Masters

	anInstance = Masters()

	print "*"*50

	''' Access instance method via an instance '''

	print anInstance.instance_Method

	''' 
		Output - As we can see below an instance method is bound to an instance
	'''

	''' <bound method Masters.instance_Method of <__main__.Masters object at 0x0000000000681AC8>> '''



	''' Access class method via an instance '''

	print anInstance.klass_Method

	''' 
		Output - As we can see below a class method is bound to an instance too
	'''

	''' <bound method type.klass_Method of <class '__main__.Masters'>> '''




	''' Access static method via an instance '''

	print anInstance.static_Method
	
	''' 
		Output - As we can see below a static method can be accessed via instance too

		*** A Static method is neither bound nor un-bound, it is only a function ***
	'''

	''' <function static_Method at 0x0000000001431198> '''


	print "*"*50



	''' Access instance method via a Class '''

	print Masters.instance_Method

	''' 
		Output - As we can see below an instance method is not bound to the Class

		*** When it says unbound it can't be called.. i.e.. Masters.instance_Method() will raise an error ***
	'''

	''' <unbound method Masters.instance_Method> '''



	''' Access class method via a Class '''

	print Masters.klass_Method

	''' 
		Output - As we can see below a class method is bound to the Class
	'''

	''' <bound method type.klass_Method of <class '__main__.Masters'>> '''



	''' Access static method via a Class '''

	print anInstance.static_Method
	
	''' 
		Output - As we can see below a static method can be accessed via Class too

		*** A Static method is neither bound nor un-bound, it is only a function ***
	'''

	''' <function static_Method at 0x0000000001431198> '''

