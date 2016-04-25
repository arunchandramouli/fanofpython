
'''
	AIM: Write a Metaclass and examine the special method __getattribute__ (the default attribute access of the Class)

	This is a very simple metaclass with little or purpose, intention being to show the
	behavior of __getattribute__ method when the class's attribute is being invoked

	In the Metaclass :
		__getattribute__ will get invoked when the new classobject is accessing the attributes

	As you see below TheMetaClass is a Metaclass (those which inherit type) and Test is a Class whose metaclass is TheMetaClass

	When we add __metaclass__ = TheMetaClass inside Class Test's body, it means that TheMetaClass has the control of class Test and it's type is TheMetaClass

	So, 

	In the Metaclass TheMetaClass:
		__getattribute__ will get invoked when the new classobject Test is accessing it's attributes
		
'''

class TheMetaClass(type):

	'''
	 TheMetaClass is a Metaclass
	'''

	
	# Define a few class level attributes

	x , y = True,False
	

	def __getattribute__(cls,name):

		'''
			The Default attribute access gateway

			I am adding a print statement here to show that it's getting returned as expected
		'''

		print 'From __getattribute__ - class and attribute requested are %s , %s '%(cls,repr(name))

		return type.__getattribute__(cls,name)


'''
	 Create a class Test whose metaclass is TheMetaClass
'''

class Test(object):
	__metaclass__ = TheMetaClass

'''
	
	Access an attribute of the class Test and the __getattribute__ defined in the metaclass will get invoked

	Ex: __name__ is an attribute of the Class
'''

print 'Name is %s '%Test.__name__, "\n\n",'attribute x == %s '%Test.x, "\n\n","attribute y == %s"%Test.y, "\n\n"

'''
	Extract from Output Window:

		From __getattribute__ - class and attribute requested are <class '__main__.Test'> , '__name__'
		Name is Test

		From __getattribute__ - class and attribute requested are <class '__main__.Test'> , 'x'
		attribute x == True

		From __getattribute__ - class and attribute requested are <class '__main__.Test'> , 'y'
		attribute y == False
'''


