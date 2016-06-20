__author__ = 'Arun Chandramouli'

import sys


class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, name, type, default=None):
        self.names = name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        #if instance:
        #    print(' Get From Class Object!')
        print " __get__ %s %s %s "%(self,instance,cls), '\n\n\n'
        return getattr(instance, self.names)
        #else :
        #    print(' Get From Class!')
        #    getattr(cls, self.name,'Nothing to Return @ class')
    def __set__(self, obj, val):
        #if obj:
        #    print 'Updating Obj', self.name , '  ', obj
        setattr(obj, self.names, val)
        #else:
        #    print 'Updating Obj Class', self.name , '  ', obj.__class__
        #    setattr(obj.__class__, self.name, val)

class MyClass(object):
    name = RevealAccess("names", str, 'Arun')
    names_2 = RevealAccess("name_2", str, 'Anne')
    y = 5

MyClass_object = MyClass()
#print MyClass_object.name, '\n\n\n'
MyClass_object.name_2 = 'S11'
print MyClass.name
print MyClass_object.__dict__, '\n\n\n'
print MyClass.__dict__, '\n\n\n'
