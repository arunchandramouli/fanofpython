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

	
	def instanceMet(instance):

		return 'I can be accessed by an Instance'


# Create an instance of class MainRef

objOfMainRef = MainRef()

# Now I create a weakreference for the instance objOfMainRef
weakRefobjOfMainRef = weakref.ref(objOfMainRef)

# print the instances

print "Class Instance --- %s and Weakref object --- %s "%(objOfMainRef,weakRefobjOfMainRef)

# print the memory location of the instances

print "Memory location of Class Instance %s and Weakreference object %s "%(id(objOfMainRef), id(weakRefobjOfMainRef))

print "-----"*20,"\n\n\n"

print "Checking if deletion of class instance will affect the weakreference object ","\n\n"

# Now delete the instance objOfMainRef
del objOfMainRef # If we rather delete the classobject MainRef, weakref will still exist

# Check if Weakref exists

print "Weakreference object - post the deletion of class instance -- %s " %weakRefobjOfMainRef # Here weakref will be a dead object

# Create an instance of weakref

weakRefobjOfMainRefobj = weakRefobjOfMainRef() 

print "Create an instance of weakreference object once class instance is deleted  --- %s "%weakRefobjOfMainRefobj

print "-----"*20,"\n\n\n"
