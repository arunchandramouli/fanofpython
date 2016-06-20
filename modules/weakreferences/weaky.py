'''
	Use Case:  Understanding the importance of weak-references. Objects that are weakly referenced get garbage collected easily.

	The need for using weakreferences is that they get gc'ed easily compared to others. (gc'ed -- Garbage Collected)

	*** Note: But please note that weakreferences are not applicable for all objects

	As per the Docs :- https://docs.python.org/2/library/weakref.html

	Not all objects can be weakly referenced; those objects which can include class instances, functions written in Python (but not in C), 
	methods (both bound and unbound), sets, frozensets, file objects, generators, type objects, DBcursor objects from the bsddb module, 
	sockets, arrays, deques, regular expression pattern objects, and code objects.

	Changed in version 2.4: Added support for files, sockets, arrays, and patterns.

	Changed in version 2.7: Added support for thread.lock, threading.Lock, and code objects.

	***
'''

import weakref


'''

 Use Case 1: Deleting the original object(referent) causes the weak-ref object to return None

 Let's say I have a class 'Class MainRef' and it's instance 'objOfMainRef' is weakly referenced.

 If I will delete the class and instance, weakly reference object becomes void

'''



class MainRef(object):

	pass # pass means do nothing


# Create an instance of class MainRef
#objOfMainRef = MainRef({11000:"Arun Chandramouli",11001:"Tim Peters",11002:"Allison Kaptur",11003:"David Beazley",11004:"Raymond Hettinger"})
objOfMainRef = MainRef()

# Now I create a weakreference for the instance objOfMainRef
weakRefobjOfMainRef = weakref.ref(objOfMainRef)

# print the instances

print objOfMainRef, ' ', weakRefobjOfMainRef

# print the memory location of the instances

print id(objOfMainRef), ' ', id(weakRefobjOfMainRef)


# Now delete the instance objOfMainRef

del objOfMainRef # If we rather delete the classobject MainRef, weakref will still exist

# Check if Weakref exists

print weakRefobjOfMainRef # Here weakref will be a dead object

# Create an instane of weakref

weakRefobjOfMainRefobj = weakRefobjOfMainRef() 

# print the new instance

print weakRefobjOfMainRefobj # Returns None