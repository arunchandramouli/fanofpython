
__author__ = 'Arun Chandramouli'

import copy

'''
	Prototype/Clone Pattern is a Creational Design Pattern - It deals with the way the instance is being created!
	Use copy module to create a copy of an existing instance or any object,while doing so, a new object gets created
	in a different memory location!
'''

'''
	Here we create a class and get the copy of it's instance
'''

# Factory to create the Classes!
def a_class_factory(onion,pepper,cardamom,tomato,cheese,chillyflakes):

	class MySpecialPizza(object): # A Class inside a function!

		@classmethod #This can be  classmethod or anything...
		def _inits_(instance):
            
            # Do something useful
			# Return something useful, this is a sample alone!
			return onion,pepper,cardamom,tomato,cheese,chillyflakes

		def __call__(cls,*args,**kwargs):

			# The __call__ method will get invoked automatically, 
			#when the arguments are passed on the instance of the class
			print "The __call__ method will get invoked automatically, when the arguments " +\
			"are passed on the instance of the class ."
			print cls,args,kwargs

	# Return the Class object . Please rember that you can return the instance too.. return MySpecialPizza()
	return MySpecialPizza 

# Create the Class
pizza = a_class_factory(onion=True,pepper=True,cardamom=True,tomato=True,cheese=True,chillyflakes=True)

# Create the instance of the Class
pizzaobj = pizza()

# Now I wanna clone the instance of pizza, without actually creating a new instance
clone1 = copy.copy(pizzaobj)
clone2 = copy.deepcopy(pizzaobj)

# Now let's print and check the value, the ID of these instances will differ
print pizzaobj,clone1,clone2,id(pizzaobj),id(clone1),id(clone2)

# The Copied objects can access the methods of the Class

print pizzaobj._inits_,clone1._inits_,clone2._inits_



# We can use a class or function factory to do that job for us!

def copy_instance_factory(copies = True):

	class Main(object):

		def __new__(cls,*args,**kwargs):

			return super(Main,cls).__new__(cls) if not copies else copy.copy(super(Main,cls).__new__(cls))
	return Main() # Calls the __new__ method above and returns the instance of class Main
print copy_instance_factory(False) # Returns the Main Class instance , embedded inside the function -- copy_instance_factory
print copy_instance_factory(False) # Returns the Main Class instance copy, embedded inside the function -- copy_instance_factory