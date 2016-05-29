
'''
	AIM: To demonstrate the difference between mutable & immutable
	In simple words;
	Mutable - pass it by reference and objects refer to the same memory location
	Immutable - pass it by value and objects refer to different memory location. Only these objects can be used
	as dictionary keys, since they are hashable

	--> Above quote is as per python glossary
'''
#Lets define a global dict to be used to for adding keys - only immutable objects can be added as keys!
# Lets start with user-defined class , are they mutable or immutable?
superDict = {}

print 'Testing for Mutability - User defined Class!','\n\n'

# ****** User defined classes are immutable! ******

class Test:pass # An old style class
class NewTest(object):pass # An old style class

print hash(Test), hash(NewTest) # returns the valid hash values -- 18907208 6604264

superDict.__setitem__(Test,'OldClass')
superDict.__setitem__(NewTest,'NewClass')
print superDict,'\n\n'

# The output below shows classes are hashes and can be used as dict keys

'''
	Output:
	{<class __main__.Test at 0x0000000001375048>: 'OldClass', <class '__main__.NewTest'>: 'NewClass'}
'''

class simple(object):pass

simple = NewTest # Equal

# Now check their hashvalue which is same as id()

print hash(simple) == hash(NewTest) # returns True
print id(simple) == id(NewTest) # returns True
del simple # delete class simple
print NewTest # returns <class '__main__.NewTest'>

print ' . ' * 50 ,'\n\n'



print 'Testing for Mutability - Instance of User defined Class!','\n\n'

# ****** Instances of user defined classes are immutable! ******

object1 = Test()
object2 = NewTest()
# Instances of user defined classes are hashable can be used as dict keys and set item
print hash(object1),hash(object2) # returns 18883144 18864616
print '\n\n'
superDict.__setitem__(object1,'Instance of Class Test')
superDict.__setitem__(object2,'Instance of Class NewTest')
print superDict,'\n\n' # returns valid output

# Now check their hashvalue which is same as id()
object1 = object2

assert hash(object1) == hash(object2) ,'\n\n'
assert id(object1) == id(object2) , '\n\n'

print ' . ' * 50 ,'\n\n'


print 'Testing for Mutability - builtin type list!','\n\n'

# ****** Builtin types lists are mutable! ******

listA = range(10)
#print hash(listA) # lists are not hashable - can't be set as dict key or set item

'''
	Output:		

		Traceback (most recent call last):
		  File "mutables.py", line 78, in <module>
		    print hash(listA)
		TypeError: unhashable type: 'list'
'''

listB = listA
# since they refer same memory location, when listB is modified it will affect listA too... pass by reference!
listB.extend(range(10,21)) 
print listA, listB,'\n\n'

# As we could see in the output below both the lists are affected!
'''
	Output:

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

'''

# Now check their hashvalue which is same as id()

assert id(listB) == id(listA) , '\n\n' # returns True

del listA # delete listA, but listB will still exist!
print listB # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print ' . ' * 50 ,'\n\n'

print 'Testing for Mutability - builtin type set!','\n\n'

# ****** Builtin types sets are mutable! but frozensets are immutable ******
# A Set is an unordered collection of items!

mySet = set()
print mySet, mySet.__class__

# Are sets hashable?

#print hash(mySet)

'''
	Traceback (most recent call last):
	  File "mutables.py", line 121, in <module>
	    print hash(mySet)
	TypeError: unhashable type: 'set'
'''

mySet2 = mySet # Mutable objects

# Now if I perform action on mySet, mySet2 will be updated automatically!

mySet.add('Tim Peters')
print mySet, mySet2 # returns set(['Tim Peters']) set(['Tim Peters'])

# A mutable object cannot be a set element
#mySet2.add(range(4))

'''
	Traceback (most recent call last):
  	File "mutables.py", line 137, in <module>
    	mySet2.add(range(4))
	TypeError: unhashable type: 'list'
'''

print ' . ' * 50 ,'\n\n'


print 'Testing for Mutability - builtin type bytearray!','\n\n'

# ****** Builtin types bytearray are immutable , they can be used as dict keys and set items******

print hash(bytearray) # returns 505762448

print ' . ' * 50 ,'\n\n'