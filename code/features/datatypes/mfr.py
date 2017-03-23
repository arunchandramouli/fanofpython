import __builtin__


'''	
	Aim :: To demonstrate map, filter, reduce
		
'''



'''
	Define a simple tuple with multiple datatypes
'''

def_tuple = 1,2,"1","100","Python","Anne","A!@345<>_()",True,False,{1:100,2:200,3:300},range(10)



'''
	Use filter - Pick only hashable items
'''

print "Use filter - Pick only hashable items ... ",'\n\n'

print filter(lambda x : hasattr(x,"__hash__"),def_tuple)

print "\n\n"

'''
	Use filter - Pick only items that has __getitem__
'''

print "Use filter - Pick only items that has __getitem__ ",'\n\n'

print filter(lambda x : hasattr(x,"__getitem__"),def_tuple)

print "\n\n"




'''
	Use filter - Pick only items that has __iter__
'''

print "Use filter - Pick only items that has __iter__ ",'\n\n'

print filter(lambda x : hasattr(x,"__iter__"),def_tuple)

print "\n\n"



''' A Function to check hashability '''

def is_hashable(objtohash):

	'''
		Parameters

			objtohash - Pass the object
	'''

	try:

		return bool(hash(objtohash))

	except Exception as E:

		print "Exception %s "%E

		return False



'''
	Use filter - Pick only items that has hash values
'''

print "Use filter - Pick only items that has hash values ",'\n\n'

print filter(is_hashable,def_tuple)

print "\n\n"




''' Let's use maps '''

print "Use Maps to analyze .... ",'\n\n'
print map(is_hashable,def_tuple)
print "\n\n\n"



''' Let's use reduce '''

print "Using reduce .... ",'\n\n'
print reduce(int.__add__,range(100))
print '\n\n'


''' List Comprehension '''

print "Using List Comprehension .... ",'\n\n'

for i in xrange(100):

	if i % 3 == 0 : print i



print [i for i in xrange(100) if i % 3 == 0 and i%5 !=	 0 ]