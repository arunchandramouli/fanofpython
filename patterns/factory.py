
__author__ = 'Arun Chandramouli'

'''
	A Class factory - Pass in parameters to a function and return a class.
	The Functions below act as a factory and they produce classes on demand,
	in this way we needn't hardcode the classes, they are created as per the need.
'''

# Factory to create the Classes!
def a_class_factory(onion,pepper,cardamom,tomato,cheese,chillyflakes):

	class MySpecialPizza(object): # A Class inside a function!

		@classmethod #This can be  classmethod or anything...
		def _inits_(instance):
            
            # Do something useful
			return onion,pepper,cardamom,tomato,cheese,chillyflakes # Return something useful, this is a sample alone!

		def __call__(cls,*args,**kwargs):

			# The __call__ method will get invoked automatically, when the arguments are passed on the instance of the class
			print "The __call__ method will get invoked automatically, when the arguments are passed on the instance of the class ."
			print cls,args,kwargs

	return MySpecialPizza # Return the Class object . Please rember that you can return the instance too.. return MySpecialPizza()

# Create the Class
pizza = a_class_factory(onion=True,pepper=True,cardamom=True,tomato=True,cheese=True,chillyflakes=True)

# Create the instance of the Class
pizzaobj = pizza()

# Invoke the classmethod
print pizzaobj._inits_() # same as pizzaobj._inits_.__call__()

# Invoke the __call__ method

pizzaobj(100,200,300,400,500,{1:1000,2:20000,'I':"Arun Kumar Chandramouli"})


# Create a Class on the fly
def a_class_factory_fly(onion,pepper,cardamom,tomato,cheese,chillyflakes,name,mets):

	return type(name,(object,),{mets : lambda self:(onion,pepper,cardamom,
		tomato,cheese,chillyflakes)})  # Return something useful, this is an example only!


# Create the Class
pizza = a_class_factory_fly(onion=True,pepper=True,cardamom=True,tomato=True,cheese=True,chillyflakes=True,
	name='MySpecialPizzas',mets = "_inits_")
print pizza

# Create the Object
pizzaobj = pizza()

# Invoke the Method
print pizzaobj._inits_()




# A Class inside a Class

class Main(object):

	# This will return another class

	def __call__(cls,*args,**kwargs):

		return type(args.__getitem__(0),(object,),kwargs) # args.__getitem__(0) is same as args[0] :-)

objMain = Main()
print objMain('Dummy',{"x":1000,"y":2000})


# A Class inside a Class - This will return a Metaclass -:)

class Main(object):

	# This will return another class - This method will et invked when the instance has parameters passed

	def __call__(cls,*args,**kwargs): # This can be done via other special methods too

		class InsideMain(type):
			pass

		return InsideMain(InsideMain.__name__,(type,),kwargs)	# Return a Metaclass

objMain = Main() # This is an instance of Main, not InsideMain
theMetaclass =  objMain({"x":1000,"y":2000}) # The Metaclass
print objMain ,theMetaclass,objMain.__class__ ,theMetaclass.__class__,theMetaclass.__class__.__class__