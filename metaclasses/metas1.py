
'''
	AIM: Write a Metaclass and check the instance creation

	This is a very simple metaclass with little or purpose, intention being to show the
	new class object creation and instantiation

	In the Metaclass :
		__new__ will get invoked when the new classobject is being created
		__init__ will get invoked when the new classobject is being instantiated
		__call__ will get invoked when an instance is being created

	As you see below Circle is a Metaclass (those which inherit type) and Test is a Class whose metaclass is Circle

	When we add __metaclass__ = Circle inside Class Test's body, it means that Circle has the control of class Test and it's type is Circle

	So, 


	In the Metaclass Circle:
		__new__ will get invoked when the new classobject Test is being created
		__init__ will get invoked when the new classobject Test is being instantiated
		__call__ will get invoked when an instance of Test is being created

'''

class Circle(type):

	'''
	 Circle is a Metaclass
	'''

	def __new__(cls,name,bases,attrs):

		print('Metaclass - Creating new Class Object --- %s  '%super(Circle,cls).__new__(cls,name,bases,attrs))
		return super(Circle,cls).__new__(cls,name,bases,attrs)

	def __init__(cls,name,bases,attrs):
		
		print('Metaclass - Instantiation of the new Class Object --- %s  '%super(Circle,cls).__init__(name,bases,attrs))
		return super(Circle,cls).__init__(name,bases,attrs)



	def __call__(cls,*args,**kargs):

		print('Metaclass - Creating Instance ---  %s '%super(Circle,cls).__call__(*args,**kargs))
		return super(Circle,cls).__call__(*args,**kargs)



'''
	Circle is now our Metaclass  and we can access instance methods of Circle via class Test  directly without actually
	creating an instance of Test

	The instance methods of Circle aren't accessible to instances of Class Test
'''

class Test(object):
	__metaclass__ = Circle

'''
	When an object of Class Test is being created the __call__ method of Metaclass Cirlce gets invoked.

	This is because Circle is the metaclass of Test and it is stored in it's dictionary.

	Inspect the dictionary of Test . Test.__dict__ and check for the key '__metaclass__'
'''
x = Test()
print("Inspect the dictionary of Test . Test.__dict__ and check for the key '__metaclass__'")
print(Test.__dict__) # Will have the Circle class object as value for key '__metaclass__'

'''

Extract from Output Window:

	{'__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, 
	'__module__': '__main__', '__metaclass__': <class '__main__.Circle'>, '__doc__': None}
'''
print("Inspect the dictionary of Test's instance . x.__dict__ and it will be empty ")
print(x.__dict__) # Empty - No entries

'''

Extract from Output Window:

	 {}

'''