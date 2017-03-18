import copy


'''	
	Aim :: To demonstrate the use of a dictionary

	Define a simple dictionary , add values to it and iterate and print it	

	Dictionary works based on hashing principle ... simply said key,value pairs


	** A dictionary object is a mutable datatype which means it couldnt be hashed
	Anything that cant be hashed cant be set as a dictionary key
	
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

	Lets explore few more

'''


'''
	Create a copy of an existing dictionary

	*** When we create a copy as dictB.copy() it refers to a different memory location
	The changes made to new copy will not affect existing

'''

copyofdictB = dictB.copy()

print "Memory Location of dictB , copyofdictB   %s , %s  "%(id(dictB),id(copyofdictB)),'\n\n\n\n'

'''

	The changes made to new copy must not affect the existing , since they
	reside at different location

'''

copyofdictB['Superman'] = "Cool"

'''
	Also let's use update method to add values
	When using update method we must pass a dict as an argument..
'''

copyofdictB.update({"Batman":"Robin"})

print "dictB = %s " %dictB ,'\n',"copyofdictB = %s "%copyofdictB,'\n\n',
print "dictB Address = %s " %id(dictB) ,'\n',"copyofdictB = %s "%id(copyofdictB),'\n\n',



'''
	Using pop and popitem
'''

'''
	Say I want to remove key '11' from dictB
	This is what I would do;
'''

print "Let's use pop method to pop key 11 from  dictB ",'\n\n'
dictB.pop(11)

print "dictB modified ",'\n\n',"Famous saying .. When key is gone it's value is also gone :) ",'\n\n'
print dictB.keys(),'\n',dictB.values(),'\n\n'



print "Let's use popitem method to pop keys from  dictB ",'\n\n'


'''
	popitem method will pop the first key in the dict by default
'''
dictB.popitem()

print "dictB modified using popitem ",'\n\n',"Famous saying .. When key is gone it's value is also gone :) ",'\n\n'
print dictB.keys(),'\n',dictB.values(),'\n\n'