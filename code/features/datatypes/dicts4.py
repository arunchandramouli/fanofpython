
'''	
	Aim :: To demonstrate the use of a dictionary

	Define a simple dictionary , add values to it and iterate and print it	

	Dictionary works based on hashing principle ... simply said key,value pairs


	** A dictionary object is a mutable datatype which means it couldnt be hashed
	Anything that cant be hashed cant be set as a dictionary key **

	Here we will deal with modifying an existing dictionary
	

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
	
	Lets modify an existing dictionary

	*** Address before and after modification will remain the same ***

'''

print "dictB before modification %s "%(dictB),'\n\n'
print "Address of dictB before modification %s "%(id(dictB)),'\n\n'

dictB[11] = "Hello World"


print "dictB after modification %s "%(dictB),'\n\n'
print "Address of dictB after modification %s "%(id(dictB)),'\n\n'


'''
	Assigning the dictB to a variable
'''

vara = dictB

print "Address of vara and dictB before altering vara %s and %s "%(id(vara),id(dictB)),'\n\n'

'''
	Modifying vara will result in modifying dictB and vice-versa
'''

vara.update({100:200})


print "Address of vara and dictB after altering vara %s and %s "%(id(vara),id(dictB)),'\n\n'

print "vara and dictB after modification ",'\n\n'

'''
	As we can observe both vara and dictB are now modified
'''
print "vara = %s "%(vara),'\n'
print "dictB = %s "%(dictB),'\n'