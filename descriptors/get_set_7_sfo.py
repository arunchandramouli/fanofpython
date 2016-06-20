__author__ = 'Home'

class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5
    z = RevealAccess(13, 'var "z"')
    n = False
    def foo(self):
        self.n = True
        self.z = RevealAccess(13, 'var "z"')
        self.__class__.n = 'Tim'
        self.__dict__.update(dict(name = ' Arun '))

m = MyClass()
m.foo()
m.z # no print
m.x # prints var x
print(MyClass.__dict__)
print(m.__dict__)