__author__ = 'Home'

class propertycache(object):
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    def __get__(self, obj, type=None):
        result = self.func(obj)
        self.cachevalue(obj, result)
        return result
    def cachevalue(self, obj, value):
        setattr(obj, self.name, value)

class foo(object):
    @propertycache
    def expensive(self):
        print 'created'
        return [1, 2, 3]
f = foo()
f.expensive
f.expensive



class Property(object):

	def __init__(instance,a,b):
		instance._a = a
		instance._b = b

	@property
	def foo(self):
	    return self._a

	@foo.setter
	def foo(self,value):
		self._a = value
