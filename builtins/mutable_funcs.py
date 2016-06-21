'''
	AIM: To demonstrate the difference between mutable & immutable
	In simple words;
	Mutable - pass it by reference and objects refer to the same memory location
	Immutable - pass it by value and objects refer to different memory location. Only these objects can be used
	as dictionary keys, since they are hashable

	--> Above quote is as per python glossary
'''


'''	
	We will now pass a mutable argument as a parameter for a 
	function and check how it behaves.
'''

import types

# A Sample function with crazy result!

def foobarz(passamutable=[]): # Get's called once @ function definition time!

	if passamutable.__class__ == types.ListType:		
		passamutable.append('David Beazley')
		passamutable.append('Tim Peters')
		passamutable.append('Allison Kaptur')

	return passamutable

'''
	Test the function!
'''
x = foobarz()
y = foobarz() 
#print x , y # Obtains Strange results!!

#print '---' * 25 , '\n\n'

# Now let's pass a list with args

# A Sample function with crazy result!

def foobarz(passamutables=['Maria']): # Get's called once @ function definition time!

	if passamutables.__class__ == types.ListType:		
		passamutables.append('David Beazley')
		passamutables.append('Tim Peters')
		passamutables.append('Allison Kaptur')

	return passamutables

'''
	Test the function!
'''
x = foobarz()
y = foobarz() 

#print x # Obtains Strange results!!
#print y # Obtains Strange results!!

#print '---' * 25 , '\n\n'



# Now let's pass a mutable argument outside of a function via the function object

'''
	A Sample function with correct result.
	It returns valid since new list/empty list is being passed at each function call
'''

def foobarz(passamutables): # Get's called once @ function definition time!

	if passamutables.__class__ == types.ListType:		
		passamutables.append('David Beazley')
		passamutables.append('Tim Peters')
		passamutables.append('Allison Kaptur')

	return passamutables

'''
	Test the function!
'''
x = foobarz([]) # pass an empty mutable container - list
y = foobarz([]) # pass an empty mutable container - list

#print x
#print y

x_1 = foobarz(['Arun']) # pass a mutable container - list
y_1 = foobarz(['Arun']) # pass a mutable container - list


#print x_1
#print y_1

#print '---' * 25 , '\n\n'



'''
	Now let's put this inside a class and check how it works
'''
class A(object):

	@classmethod
	def foonbarz(self,passamutables=['Maria']): # Get's called @ function creation time

		# if passamutables is not None : passamutables = [] # Uncomment this line to make it work properly!!

		if passamutables.__class__ == types.ListType:		

			passamutables.append('David Beazley')
			passamutables.append('Tim Peters')
			passamutables.append('Allison Kaptur')

		return passamutables
		

# Access via the Class --- Strange results ... 

#print A.foonbarz()		
#print A.foonbarz()
#print A.foonbarz()

#print '---' * 25 , '\n\n'


# Access via the Class Instance --- Strange results ... 

x = A()
#print x.foonbarz()		
#print x.foonbarz()
#print x.foonbarz()

#print '---' * 25 , '\n\n'

if __name__ == '__main__':
	x = A()
	x.foonbarz()		
	