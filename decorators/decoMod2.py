'''
	Use Case:  Using a decorator to execute a function object and also get information about other function objects
	in the module and execute it too.
'''

import decoMod1,sys
sys.setrecursionlimit(25)

class Metas(type):

	def __new__(klass,name,bases,attrs):

		return type.__new__(klass,name,bases,attrs)


	def __call__(klass,*args,**kargs):
		return type.__call__(klass)

	def __getattribute__(instance,name):

		getMethodName = type.__getattribute__(instance,name)
		getMethodName = decoMod1.execute(getMethodName)

		return getMethodName

@decoMod1.classdecorator
class Execute(object):

	#__metaclass__ = Metas

	
	def product(cls,param1,param2):

		'''
			Sample Func: Compute the Product
		'''
		return param1 * param2 

	
	def sumz(cls,z = None,s = None):

		'''
			Sample Func: Compute the Sum
		'''
		return z  +  s 

	
	def negate(cls,param1,param2):


		'''
			Sample Func: Compute the Negation
		'''
		return param1  -  param2 

print Execute.product(100,1000)

print Execute.sumz(800,900)

print Execute.negate(600,500)

