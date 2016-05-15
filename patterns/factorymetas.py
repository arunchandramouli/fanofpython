__author__ = 'Arun Chandramouli'

'''
	Factory Pattern is a Creational Design Pattern - 
	It deals with the way the instance is being created!
	We will see how we can acheive it using the metaclass
'''

'''
	A Class factory - Pass in parameters to a function and return a class.
	The Functions below act as a factory and they produce classes on demand,
	in this way we needn't hardcode the classes, they are created as per the need.

	Here we use the __call__ operator to identify the arguments passed. As you know __call__ gets invoked
	automatically while the arguments are passed to ths instance of a class
'''

class IamtheMetaclass(object):

	  	def __init__(self, func, *a):
		    self.func = func
		    self.args = a

		def __call__(self, *a):

			# Add some useful logic here

		    return self.func(*a)
		

@IamtheMetaclass
def a_class_fact(onion,pepper,cardamom,tomato,cheese,chillyflakes):

	class A(object):
		'''
		 Please do something more useful in this block.
		 This being an example alone!
		'''

		def theProcessor():

			# Here we multiply and process the pizza . This is an example of duck typing too !
			return (onion*3)+(pepper*1)+(cardamom*2)+(tomato*5)+(cheese*2)+(chillyflakes*2)
		theProcessor = staticmethod(theProcessor)	

	return A # Return the Class


newPizzzzza =  a_class_fact(True,True,True,True,True,True) # Return the Class
print newPizzzzza.theProcessor()