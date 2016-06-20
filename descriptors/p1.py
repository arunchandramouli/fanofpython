import sys

sys.setrecursionlimit(5)

class A(object):

	def __init__(instance, a,b):
		instance.a = a
		instance.b = b

	def sample(instance):
		return instance.a**instance.b

	sampleIT = property(fget = sample, doc = 'Property Tests')

class B(object):

	__slots__ = ['xa','yb','zc']

	def sample(instance):
		return 1000

	@property
	def samTest(instance):
		return getattr(instance,'xa')

	def sample_f(instance):
		return instance.sample()

	sampleIT = property(sample_f)


class C(B):

	#@property
	def sample(instance):
		return 10000

	@B.samTest.setter
	def samTest(instance,value):
		setattr(instance,'xa',value)
	    
	#@B.sampleIT.setter
	'''def sample(instance,value):
		setattr(instance,'xa',100)
		return instance.xa'''


C_obj = C()
B_obj = B()

print B_obj.sample_f()

print B_obj.sampleIT

print '*' * 25

print C_obj.sample_f()

print C_obj.sampleIT

print '*' * 25

C_obj.samTest = 'Arun'
print C_obj.samTest