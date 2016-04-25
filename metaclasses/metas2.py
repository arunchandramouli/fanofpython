
'''
	AIM: Write a Metaclass and examine the special method __str__

	This is a very simple metaclass with little or purpose, intention being to show the
	behavior of __str__ method when the class is being invoked by it's instance

	In the Metaclass :
		__str__ will get invoked for the new classobject's string representation

	As you see below Circle is a Metaclass (those which inherit type) and Test is a Class whose metaclass is Circle

	When we add __metaclass__ = Circle inside Class Test's body, it means that Circle has the control of class Test and it's type is Circle

	So, 

	In the Metaclass Circle:
		__str__ will get invoked when the new classobject Test is being printed
		__str__ will get invoked when the new classobject Test's instance calls for type ; eg: type(x)
		
'''

class Circle(type):

	'''
	 Circle is a Metaclass
	'''

	def __str__(cls):

		return ' I am the Hacker! Metaclass '


'''
	 Create a class Test whose metaclass is Circle
'''

class Test(object):
	__metaclass__ = Circle


'''
	When I print Test it will show an output of it's metaclass's __str__. This is because class Test is an
	instance of class Circle, hence the special methods defined inside Circle will get invoked for operations performed
	on class Test.

	*** An Instance is an instance of Class, a Class is an instance of Metaclass
'''
print Test


'''

	Extract from Output Window:

		' I am the Hacker! Metaclass '
'''