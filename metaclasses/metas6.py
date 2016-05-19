'''
	AIM: Write a Metaclass and check the instance creation

	This is a very simple metaclass with little or purpose, intention being to show the
	new class object creation and instantiation

	In the Metaclass :
		__new__ will get invoked when the new classobject is being created
		__init__ will get invoked when the new classobject is being instantiated
		__call__ will get invoked when an instance is being created

	As you see below TheMetaClass is a Metaclass (those which inherit type) and Test is a Class whose metaclass is TheMetaClass

	When we add __metaclass__ = TheMetaClass inside Class Test's body, it means that TheMetaClass has the control of class Test and it's type is TheMetaClass

	So, In the Metaclass TheMetaClass:
	
		__new__ will get invoked when the new classobject Test is being created
		__init__ will get invoked when the new classobject Test is being instantiated
		__call__ will get invoked when an instance of Test is being created

'''

class TheMetaClass(type):

	'''
	 TheMetaClass is a Metaclass
	'''

	jesus,mary,moses,thomas,krishna = True,True,True,True,True

	def __new__(cls,name,bases,attrs):

		return super(TheMetaClass,cls).__new__(cls,name,bases,attrs)

	def __init__(cls,name,bases,attrs):
		
		cls.jesus = cls.jesus
		return super(TheMetaClass,cls).__init__(name,bases,attrs)



	def __call__(cls,*args,**kargs):
	
		return super(TheMetaClass,cls).__call__(*args,**kargs)



'''
	TheMetaClass is now our Metaclass  and we can access instance methods of TheMetaClass via class Test  directly without actually
	creating an instance of Test

	The callable/non-callable of TheMetaClass aren't accessible to instances of Class Test. For them to be accessible we need to override __init__
	in the Metaclass!
'''

class Test(object):
	__metaclass__ = TheMetaClass


# Now access the attributes of the metaclass

print Test.jesus

# Now access the attributes of the metaclass via the instances of class Test

testNow = Test()

print testNow.jesus # Will print True :-)

# Now access the attributes of the metaclass by the metaclass itself

print TheMetaClass.jesus # Will print True :-)
print TheMetaClass.mary # Will print True :-)

# Now Let's create an instance of the Metaclass itself and access it's own attributes

objectOfMetas = TheMetaClass('IamTheMetas',(),{}) # Create an object of the Metaclass
print objectOfMetas.jesus,objectOfMetas.mary # Will print True :-)