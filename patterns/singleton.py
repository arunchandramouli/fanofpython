
__author__ = 'Arun Chandramouli'


'''
 	
 	Singleton is a Creational Pattern - Only one instance of the Class is even created!

'''

class OnlyOneInstance(object):

	'''
	 OnlyOneInstance is a Class
	'''
	singleInstance = dict()
	def __new__(cls,*args,**kargs):

		
		cls.singleInstance.__setitem__('instance',
			super(OnlyOneInstance,cls).__new__(cls,*args,**kargs))if not 'instance' in cls.singleInstance.keys() else None
		return cls.singleInstance.__getitem__('instance')
		
tests = OnlyOneInstance()
tests0 = OnlyOneInstance()
tests1 = OnlyOneInstance()

print tests,tests0,tests1
print id(tests),id(tests0),id(tests1)


class TheMetaclass(type):

	singleInstance = dict()

	def __call__(cls,*args,**kwargs):


		cls.singleInstance.__setitem__('instance',
			type.__call__(cls,*args,**kwargs))if not 'instance' in cls.singleInstance.keys() else None
		return cls.singleInstance.__getitem__('instance')


class Sample(object):

	__metaclass__ = TheMetaclass


x = Sample()
x1 = Sample()
x2 = Sample()

print x,x1,x2
print id(x),id(x1),id(x2)

