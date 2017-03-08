'''
	Use Case:  Exploring the User defined Class  -- using Private Methods

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

	
	Why we need Instance Method?

		-> 	Facilitate instance creation and ability to access certain methods via instances alone
		->  Make instance specific attributes accessible inside the instance methods
		->  Can access all the attributes of the class, methods, class variables, instance specific variables...
		->	* Takes first argument as a Class Instance ,which is a mandate
	
	Why we need Class Method?

		-> * Takes first argument as a Class object which is a mandate
		-> Doesn't depend on the instances of the class
		-> Favors advantages while inheriting the parent class 
		-> Defines Alternate Constructors
		-> Perform some activity before an instance of the class gets created

	
	Why we need Static Method?

		-> * Doesn't take any first argument as a mandate positional parameter
		-> Makes you feel a function inside the class
		-> Can be used in many ways to pass data
		-> Perform some tasks that is not dependent on the instance or the class
		-> Can be accessed by both the instance of the class and the class

'''




''' Define an User defined class - Masters'''

class Masters(object): # A new-style class inherits from object


	# Declaring Class level Attrs - visible for class and it's instance

	a1,b2,c3 = 100,200,300

	''' 
		__init__ is the constructor block.

		It takes 3 arguments namely x,y,z which means during instance creation they have passed,
		else an error will be raised

		For eg: 
			anInstance = Masters() # INCORRECT
			anInstance = Masters("Tim","John","David") #CORRECT


		***** 
				Please note carefully that __init__ has 4 parameters
					-> instance
					-> x
					-> y
					-> z

				Here we are passing only 3 Parameters, right ? - anInstance = Masters("Tim","John","David") #CORRECT

				When we pass anInstance = Masters("Tim","John","David") it goes to the __init__ block

				The call transforms as Masters(anInstance,"Tim","John","David")

				So whatever instance we created gets converted automatically and it refers
				to the first positional argument inside __init__ block i.e. instance

		*****

	'''
	def __init__(instance,x,y,z):

		''' 

			*** During instance creation while passing arguments to the class name this block will get executed ***
			
			The variables declared inside the __init__ block 
			are known as instance specific variables
			*** "instance" that we find as a parameter is the instance, at run time that argument gets
			converted as an instance ***

		'''
		
		instance.topic = "SCIENCE & PROGRAMMING"

		# Lets access values of x,y,z

		print x,y,z


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

		''' Can Access Class level attributes here '''
		print "Accessing Class level attributes inside the instancemethod","\n"
		print this.a1, this.b2, this.c3

		''' Accessing the Private Method '''

		print this.__iamprivate()

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


		''' Can Access Class level attributes here '''
		print "Accessing Class level attributes inside the classmethod","\n"
		print that.a1, that.b2, that.c3,"\n\n"

		return ' Hello - I am a Class Method'

	''' 
		A Static method is as good as a function , no positional arguments are needed


		It can be accessed via an instance , as well as a class.

		It gets converted as a function @ run time  .... *** A Static method is neither bound nor un-bound, it is only a function ***

		It is defined as @staticmethod

	'''
	@staticmethod
	def static_Method(): # No positional arguments

		''' We cannot access class level variables here, but can take arguments and perform any operations '''
		return ' Hello - I am a Static Method'



	'''
		Define a Private Method and access it inside the class

		This is an instance method
	'''

	def __iamprivate(self):

		''' Private Methods are stored in a different format in the class dict '''
		return "Hello World! __iamprivate "



if __name__ == '__main__':

	# Now Examine the Class

	# Create an Instance of class Masters

	anInstance = Masters("Tim Peters","David Beazley","Raymond Hettinger")

	print "*"*50

	''' Execute an instance method from an instance '''

	print anInstance.instance_Method()


	''' Execute an instance method using a Class '''

	#print Masters.instance_Method() # Will raise an error since an instance method is not bound to a class


	''' Execute a classmethod from an instance '''

	print anInstance.klass_Method()


	''' Execute a classmethod from a class '''

	print Masters.klass_Method()
