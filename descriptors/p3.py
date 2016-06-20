class Circle(object):
     PI = 3.14
     def __init__(self, radius):
         self.radius = radius



class MyDescriptor(object):
	  	 
     def __init__(self):
         self.mDict = {}

     def __get__(self, obj, type):
         print self, obj, type
         return self.mDict.__getitem__(obj)
     def __set__(self, obj, val):
         print "Got %s" % val
         self.mDict.__setitem__(obj,val)
         

class MyClass(object):
     x = MyDescriptor() # Attached at class definition time!
     y = range(100)


h = MyClass()

#print MyClass.x
#print h.x
print "*"*50, "\n\n"
h.x = 5000000
print h.x

print "*"*50, "\n\n"


class D(object):
     def f(self, x):
          return x


print D.__dict__['f'].__get__(None,D)