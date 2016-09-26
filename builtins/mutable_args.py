'''
	AIM: To demonstrate the difference between mutable & immutable
	In simple words;
	Mutable - pass it by reference and objects refer to the same memory location
	Immutable - pass it by value and objects refer to different memory location. 
	Only these objects can be used as dictionary keys, since they are hashable

	--> Above quote is as per python glossary
'''


'''	
	We will now pass a mutable argument as a parameter for a 
	function and check how it behaves.
'''

import types

# A Sample function with correct result!

def foobarz(passamutable): # Get's called @ function execution time!

	if passamutable.__class__ == types.ListType:		
		passamutable.append('David Beazley')
		passamutable.append('Tim Peters')
		passamutable.append('Allison Kaptur')

	return passamutable


def immutable(passImmutable):

	passImmutable = None
	return passImmutable


def foobars(): # Get's called @ function execution time!
	
	passamutable = []	

	if passamutable.__class__ == types.ListType:		
		passamutable.append('David Beazley')
		passamutable.append('Tim Peters')
		passamutable.append('Allison Kaptur')
		passamutable.append('Linuss Torvalds')

	return passamutable


def foobarsgonecrazy(passamutable = []): # Get's called @ function definition time!	

	if passamutable.__class__ == types.ListType:		
		passamutable.append('David Beazley')
		passamutable.append('Tim Peters')
		passamutable.append('Allison Kaptur')
		passamutable.append('Linus Torvalds')

	return passamutable


'''
	Test the function!
	x is a list outside a function and when it is passed to a function, it's value is affected
'''

if __name__ == '__main__':
	
	# Mutable

	x = [1,2,3]
	print foobarz(x) # returns [1, 2, 3, 'David Beazley', 'Tim Peters', 'Allison Kaptur']
	print x # returns [1, 2, 3, 'David Beazley', 'Tim Peters', 'Allison Kaptur']

	# Immutable

	x = tuple((100,200,300,400))
	print immutable(x)# returns None
	print x # returns (100, 200, 300, 400)

	# Testing foobars
	print foobars()
	print foobars()
	print foobars()


	# Testing foobarsgonecrazy with no params, the default gets called and values get appended to same memory location
	print foobarsgonecrazy()
	print foobarsgonecrazy()
	print foobarsgonecrazy()	


	# Testing foobarsgonecrazy with a param as []
	print foobarsgonecrazy([])
	print foobarsgonecrazy([])
	print foobarsgonecrazy([])	