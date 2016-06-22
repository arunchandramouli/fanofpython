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

'''
	In this example we will create a calback function that gets executed while an instance of the class is getting deleted
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

	def __del__(instance):
		print "Deleting instance %s "%instance

'''
	A Callback function will get automatically invoked while deletion of an instance of a Class
	This has to be passed as an argument while creating the weakreference object

	*** Note: This gets invoked before the __del__ method of the class ***
'''
def callback(self):

		print "I get executed automatically on deletion of class instance"

# Create an instance of class MainRef

objOfMainRef = MainRef()

# Now I create a weakreference for the instance objOfMainRef
weakRefobjOfMainRef = weakref.ref(objOfMainRef,callback) # pass the class instance and the callback function

# Now I delete the class instance objOfMainRef - this will trigger the __del__ method post calling the callback function

del objOfMainRef