import collections


'''	
	
	Aim :: To demonstrate the use of a dictionary

	Define a simple dictionary , add values to it and iterate and print it	

	Dictionary works based on hashing principle ... simply said key,value pairs

	Here we will explore about OrderedDict , defaultdict

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
	setdefault method
'''

# Define an empty dict as {}

iamemptynow = {}

'''
	Lets setdefault as as []

	Say we have a range of values
'''

for i in xrange(100):

	'''
		This creates values as lists
	'''

	iamemptynow.setdefault(i,[]).append(i+10)


#print iamemptynow,'\n\n'


'''
	Lets add something that gives multiple values
	Say we have a list of tuples

	Lets use .clear() method to remove all values
'''

iamemptynow.clear()


'''
	
	Let us form a tuple of lists
	Here I am utilizing the features of both dict and list
	Say I want to have a dict that has keys with multiple values

'''

zippeddata = ([1,True],[0,True],[1,False],[10,'Run'],[10,'Sit'],[10,'Walk'])


'''

	Here What I am actually doing is ....

	[1,True],[0,True],[1,False],[10,'Run'],[10,'Sit'],[10,'Walk']

	At run time ;
	i= 1 ; j=True
	i= 0 ; j=True
	i= 1 ; j=False
	i= 10 ; j='Run'
	i= 10 ; j='Sit'
	i= 10 ; j='Walk'

'''

for i,j in zippeddata : 

	'''

		Inside any loops use try - catch with continue
		This will ensure that in case of errors it goes to next record

		In this example let us use defaultdict as list, which can allow for
		duplicates

	'''

	try:

		iamemptynow.setdefault(i,[]).append(j)

	except Exception as E:
		continue

print iamemptynow,'\n\n'


'''
	Clear all values
'''

iamemptynow.clear()

for i,j in zippeddata : 

	'''

		Inside any loops use try - catch with continue
		This will ensure that in case of errors it goes to next record

		In this example let us use defaultdict as dict, in which case 
		duplicates are not allowed

	'''

	try:

		iamemptynow.setdefault(i,{}).__setitem__(i,j)

	except Exception as E:
		continue

print iamemptynow,'\n\n'




'''
	Now let us explore ordered dict

	An ordinary dictionary doesnot maintain insertion order
	since it's based on hashing , locations are determined
	at run-time by the hash function

	Here comes ordered dict to the rescue
'''

'''
	Let's clear'em up
'''
iamemptynow.clear()

'''
	Now I am adding values to the dict  - iamemptynow
'''

iamemptynow["Name"] ="Arun"
iamemptynow["x"] =100
iamemptynow[0] = True
iamemptynow[0,1] =1000
iamemptynow[True] = False

'''
	Now I am iterating and printing the values
'''

'''
	We can see that the insertion order is not
	maintained
'''

print "Ordinary Dict .... ",'\n\n'
for key , value in iamemptynow.items():

	print "Key ==== %s and Value ==== %s "%(key,value),"\n"



'''
	Now Let's use OrderedDict
'''


'''
	Let's clear'em up
'''
iamemptynow.clear()

iamemptynow = collections.OrderedDict()


'''
	Now I am adding values to the dict  - iamemptynow
'''

iamemptynow["Name"] ="Arun"
iamemptynow["x"] =100
iamemptynow[0] = True
iamemptynow[0,1] =1000
iamemptynow[True] = False

'''
	Now I am iterating and printing the values
'''

'''
	We can see that the insertion order is maintained
'''
print "\n\n\n\n"

print "Ordered Dict .... ",'\n\n'

for key , value in iamemptynow.items():

	print "Key ==== %s and Value ==== %s "%(key,value),"\n"

