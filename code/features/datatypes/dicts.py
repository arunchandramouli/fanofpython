

'''	
	Aim :: To demonstrate the use of a dictionary

	Define a simple dictionary , add values to it and iterate and print it	

	Dictionary works based on hashing principle ... simply said key,value pairs
'''



'''
	An Empty Dict
'''

dictA = dict() # same as dictA = {}



dictB = dict() # same as dictB = {}

'''
	Adding values to it 
'''

for i in [1,3,2,4,8,9,5,6,7]:

	dictB[i] = i

'''
	Adding values to a dict
'''
	

# Let us use a simple for loop to add values to a dict

for i in xrange(10):

	dictA[i] = i + 10


print dictA,'\n\n',dictB,'\n\n'



'''
	Adding same keys to the dict

	When @ run-time it see similar keys, the former key will be removed
	and the latter will be retained with its value.

'''

for i in [11,11,14,12,13]:

	dictB[i] = i * 10


print dictB,'\n\n'



'''
	Exploring a dict
'''


#print dir(dictB)

'''
	
	['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', 
	'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
	 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
	 '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 
	 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
'''

'''
	Lets explore them ... 
'''

print "__class__",' = ',dictB.__class__,'\n\n'
print "Values ",' = ',dictB.values(),'\n\n'
print "Keys ",' = ',dictB.keys(),'\n\n'
print "Items ",' = ',dictB.items(),'\n\n'
print "iteritems ",' = ',dictB.iteritems(),'\n\n'
print "iterkeys ",' = ',dictB.iterkeys(),'\n\n'
print "itervalues ",' = ',dictB.itervalues(),'\n\n'
print "viewitems ",' = ',dictB.viewitems(),'\n\n'
print "viewkeys ",' = ',dictB.viewkeys(),'\n\n'
print "viewvalues ",' = ',dictB.viewvalues(),'\n\n'


'''
	Check if the dict has certain key
'''

print "Check for Key = 0 in dictA and dictB ",'\n\n',dictA.has_key(0),'\n',dictB.has_key(1000),'\n'


'''
	Accessing the value of a dictionary
'''

'''
	Now I want to access dictA and get some values
'''

print "Acessing dictA using [] ",'\n'
print dictA[5] # same as dictA.__getitem__(5)

# This will generate KeyError 
#print dictA['Arun'] # same as dictA.__getitem__('Arun')

'''
	
	In the case above, when we access as dictA[5]
	if the key is not there we will get KeyError
	to avoid that use .get() method , it shall return None
	in that case

'''

print "Acessing dictA using .get() ",'\n'
print dictA.get(1000,"Key aint there yet"),'\n\n'



'''
	Iterate and print the keys and values
'''

print "Iterate and print the keys and values .... ",'\n\n'

for key , value in dictB.items():

	print "Key = %s and Value = %s "%(key,value),'\n\n'


'''
	Clear the Values in the dictionary
		** Before we clear, lets pick the memory location **
'''

'''
	When we use .clear to empty the dictionary
	the address will not get changed
'''

print "Memory Address dictB - Before Clear  %s "%id(dictB),'\n\n'

dictB.clear()

print "dictB = %s "%dictB,'\n\n'

print "Memory Address dictB - After Clear  %s "%id(dictB),'\n\n'



'''
	When we use {} to empty the dictionary
	the address will get changed
'''

print "Memory Address dictA - Before Clear  %s "%id(dictA),'\n\n'

dictA = {}

print "dictA = %s "%dictA,'\n\n'

print "Memory Address dictA - After Clear  %s "%id(dictA),'\n\n'
