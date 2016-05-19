'''
	AIM: Write a Metaclass and check the instance creation

	*** Here we will be inheriting the metaclass instead of using __metaclass__ ***

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

	def loveShouldbeTrue(cls):
		return True


'''
 	We have a class Test and we inherit the metaclass, and we try to access it's attributes.
'''

class Test(TheMetaClass):
	pass


# Now access the attributes of the metaclass

print Test.jesus # returns True

# Now access the attributes of the metaclass via the instances of class Test

testNow = Test('SubClass',(),{}) # You need to pass 3 parameters namely name,bases,attrs to create an instance!

print testNow.jesus # Will print True :-)
print testNow.loveShouldbeTrue.__call__() # same as testNow.loveShouldbeTrue() 

# Here's a neat trick .. how do you call an instance method of a class without actually creating an instance...

print Test.loveShouldbeTrue.__get__(Test,Test) # Use Descriptor :-)
print Test.loveShouldbeTrue.__get__(Test,Test).__call__() # Use Descriptor :-) .. same as print Test.loveShouldbeTrue.__get__(Test,Test)()

