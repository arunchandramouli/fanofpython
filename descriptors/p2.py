import sys
sys.setrecursionlimit(10)

class Prop(object):

	'''
		Read-Only Property
	'''

	_foo = 'Foobarz'

	
	def foo(self):
	    return self._foo

	def _theGetter(self):
		return self.foo()

	barz = property(fget=_theGetter,fset=None,fdel=None,doc="The @property")    


Prop_object = Prop()

#print Prop.foo
#print Prop.barz
#print Prop_object.foo
#print Prop_object.barz
print "*"*50,"\n\n"

class InProp(Prop):
	
	@Prop.barz.setter
	def fooz(self,vl):
		self._foo = vl
		return self._foo


InProp_object = InProp()


print InProp.foo
print InProp.barz
InProp_object.fooz = 'Greeks!'
print InProp_object.barz

print "*"*50,"\n\n"


"""
class Prop_Set(object):


	'''
		Read & Write Property
	'''

	def foo(self):
	    return self._foo


	def __getattr__(self,name):
		return False



Prop_set_object = Prop_Set()
print Prop_set_object.foo()
"""