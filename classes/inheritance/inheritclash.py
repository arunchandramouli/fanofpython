'''
	Use Case :: A Base class inherited by multiple sub-classes
	The tuple of those subclasses are inherited by a Class
	We will now evaluate the mro
'''

class Base(object):

	def __init__(self):
		print('Base.__init__')


class A(Base):

	def __init__(self):
		super(A,self).__init__()
		print('A.__init__')

	@classmethod
	def hello(self):
		return 'Hello from A!'



class B(Base):

	def __init__(self):
		super(B,self).__init__()
		print('B.__init__')


	@classmethod
	def hello(self):
		return 'Hello from B!'



class C1(Base):

	def __init__(self):
		super(C1,self).__init__()
		print('C1.__init__')


	@classmethod
	def hello(self):
		return 'Hello from C1!'



class X1(C1,Base,B): # X1 inherits C1, Base , B ... but C1(Base) and B(Base) - Mro Issue!

	def __init__(self):
		super(X1,self).__init__()
		print('X1.__init__')


	@classmethod
	def hello(self):
		return 'Hello from X1!'


x = X1()
print X1.__mro__

'''
	Output ::

			Traceback (most recent call last):
				  File "inheritclash.py", line 51, in <module>
				    class X1(C1,Base,B):
				TypeError: Error when calling the metaclass bases
				    Cannot create a consistent method resolution
				order (MRO) for bases Base, B

'''