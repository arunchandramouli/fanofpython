'''
	Use Case:  Understanding the importance of weak-references. Objects that are weakly referenced get garbage collected easily.

	The need for using weakreferences is that they get gc'ed easily compared to others. (gc'ed -- Garbage Collected)

	For an User defined class's instance(say A), create a weakreference (say B) to the instance. 
	But 'B' doesn't have access to attributes of A's class, for that we need to create an instance of B.

	When "A" is deleted, "B" transforms as a dead object since "B" references "A", but if an instance of weakreference is created, then if
	"A" would be deleted, "B" would still exist.

	*** Note: But please note that weakreferences are not applicable for all objects

	As per the Docs :- https://docs.python.org/2/library/weakref.html

	Not all objects can be weakly referenced; those objects which can include class instances, functions written in Python (but not in C), 
	methods (both bound and unbound), sets, frozensets, file objects, generators, type objects, DBcursor objects from the bsddb module, 
	sockets, arrays, deques, regular expression pattern objects, and code objects.

	***
'''

import weakref

'''

 Use Case 1: Deleting the original object(referent) causes the weak-ref object to return None

 Let's say I have a class 'Class MainRef' and it's instance 'objOfMainRef' is weakly referenced.

 If I will delete the class's instance, weakly reference object becomes void

'''

class MainRef(object):

	
	def instanceMet(instance):

		return 'I can be accessed by an Instance'


# Create an instance of class MainRef

objOfMainRef = MainRef()

# Now I create a weakreference for the instance objOfMainRef
weakRefobjOfMainRef = weakref.ref(objOfMainRef)

# print the instances

print "Class Instance --- %s and Weakref object --- %s "%(objOfMainRef,weakRefobjOfMainRef),"\n\n"

# print the memory location of the instances

print "Memory location of Class Instance %s and Weakreference object %s -- aren't the same "%(id(objOfMainRef), id(weakRefobjOfMainRef)),"\n\n"

print "-----"*20,"\n\n\n"

print "Access the class attribute via the weakreference - It will result in AttributeError, solution is " +\
"to create an instance for the weakreference object","\n" 
#print weakRefobjOfMainRef.instanceMet# returns AttributeError: 'weakref' object has no attribute 'instanceMet'
print "-----"*20,"\n\n\n"


#weakRefobjOfMainRefobj = weakRefobjOfMainRef() 
#print "+++"*20,"\n\n\n"
#for keys in gc.get_referrers(weakRefobjOfMainRef): print keys
#print "+++"*20,"\n\n\n"

print "Checking if deletion of class instance will affect the weakreference object ","\n\n"

# Now delete the instance objOfMainRef
del objOfMainRef # If we rather delete the classobject MainRef, weakref will still exist

# Check if Weakref exists

print "Weakreference object - post the deletion of class instance = %s #weakrefobject is dead a object now" %weakRefobjOfMainRef ,"\n\n" # Here weakref will be a dead object

# Create an instance of weakref

print "Create an instance of weakreference object once class instance is deleted ","\n\n"

weakRefobjOfMainRefobj = weakRefobjOfMainRef() 

print "New instance of weakreference object once class instance is deleted  is = %s  #returns None as expected "%weakRefobjOfMainRefobj

print "-----"*20,"\n\n\n"