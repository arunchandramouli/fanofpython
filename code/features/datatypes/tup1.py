
'''	
	Aim :: To demonstrate the use of a tuple

	Define a simple tuple , add values to it and iterate and print it	

	A tuple consists of comma seperated values which could be of any type

	which is reprsented as (,,,,) .. all values are enclosed between '(' and ')'

	** A tuple object is an immutable datatype which means it could be hashed
	Anything that can be hashed can be set as a dictionary key **

	Modifying an exisiting tuple will result in a new tuple object,
	memory address will be changed too.

	There are 2 scenarios of modification;

		-> Edit the existing item 

			-> Only Mutable datatypes can be edited, memory location not changed
			-> Editing immutable datatypes results in an error (TypeError) exception

		-> Replace the existing item
	
			-> Both mutable and immutable can be replaced
	
	
'''



'''
	Define a simple tuple with multiple datatypes
'''

def_tuple = 1,2,"1","100","Python","Anne","A!@345<>_()",True,False,{1:100,2:200,3:300},range(10)


'''
	Print and view the tuple
'''


print "Printing the tuple  - " , def_tuple, '\n\n'

'''
	Output ::

	(1, 2, '1', '100', 'Python', 'Anne', 'A!@345<>_()', True, False, {1: 100, 2: 200, 3: 300}, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

'''


print "Printing the tuple's address - " , id(def_tuple),'\n\n'# The address is subject to change

'''
	Output ::

	19858976

'''


print "Tuple Modification - Scenario Replace",'\n\n'

'''
	Let us modify an existing tuple

		-> Scenario Replace
'''


def_tuple = 1,2,"1","100","Python","Anne",("Mario & Luigi","Tom & Jerry",0,1,bool(1>2)),True,False,{1:100,2:200,3:300},range(10)



'''
	Print and view the tuple
'''


print "Printing the tuple  - " , def_tuple, '\n\n'

'''
	Output ::

	(1, 2, '1', '100', 'Python', 'Anne', ('Mario & Luigi', 'Tom & Jerry', 0, 1, False), True, False, {1: 100, 2: 200, 3: 300}, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

'''


print "Printing the tuple's address - " , id(def_tuple),'\n\n' # The address is subject to change

'''
	Output ::

	17038872 
'''


print '\n\n\n\n'

print "Tuple Modification - Scenario Editing a Mutable datatype",'\n\n'

'''
	Let us try and edit a mutable data-type such as list

	Last element is the list - so we can take it as; 

	def_tuple[-1]

	Address before and after modification remains the same
'''

'''
	Get the list
'''

getList = def_tuple[-1]

print "Address of getList and def_tuple[-1] %s and %s "%(id(getList),id(def_tuple[-1])),'\n\n'

print "Tuple and address before editing a mutable datatype -- ",def_tuple, ' ',id(def_tuple),'\n\n'

getList[2] += 100 # Add 100 to the element at position 2 , list indices start with 0

getList[4] *= 150 # Multiply element at position 2 with 150

print "Tuple and address before editing a mutable datatype -- ",def_tuple, ' ',id(def_tuple),'\n\n'





print '\n\n\n\n'

print "Tuple Modification - Scenario Editing a Immutable datatype",'\n\n'



'''
	Let us take the number at position o which is immutable
'''

print "Tuple and address before editing a immutable datatype -- ",def_tuple, ' ',id(def_tuple),'\n\n'

getNum = def_tuple[0]

getNum = 200

print "Address of getNum and def_tuple[0] %s and %s "%(id(getNum),id(def_tuple[-1])),'\n\n'

'''
	Address of getNum and def_tuple[0] are different
	hence even if we set a value as getNum = 200
	it will not alter the original tuple
'''

print "Tuple and address after editing a immutable datatype -- ",def_tuple, ' ',id(def_tuple),'\n\n'


'''
	Now lets try and edit the immutable item in the tuple directly
'''

print "Editing immutable datatype directly ",'\n\n'

#def_tuple[0] = True # This will result in a TypeError


'''
	Traceback (most recent call last):
	  File "tup1.py", line 168, in <module>
	    def_tuple[0] = True # This will result in a TypeError
	TypeError: 'tuple' object does not support item assignment
'''


print "Slicing an existing Tuple",'\n\n'

'''
	In this case the sliced and original tuple's memory address remains the same
	** Bcoz def_tuple[0:] and def_tuple[:] both represent the entire tuple itself
'''

print "From 0 to end ",def_tuple[0:],'\n',id(def_tuple[0:]),'\n',id(def_tuple),'\n\n'


'''

	In this case the sliced and original tuple's memory address will change

	** Bcoz when we slice from -5 to 0 , we are actually taking a part of the
	tuple not the entire one, hence a new tuple object gets created with a 
	new memory address . To complement this behavior please remember
	that tuple is an immutable , any such modification is limited.

'''

print "From -5 to end ",def_tuple[-5:],'\n',id(def_tuple[-5:]),'\n',id(def_tuple),'\n\n'



'''
	Storing the tuple in a variable
'''

vara = def_tuple

print "Address of vara and def_tuple %s and %s "%(id(vara),id(def_tuple)),'\n\n'

print "Modifying vara ",'\n\n'
vara = (1,2,3,4,5)

'''
	As we can notice when vara is modified , the address location
	also changes and vara and def_tuple are no more in same memory address
'''
print "Address of vara and def_tuple %s and %s "%(id(vara),id(def_tuple)),'\n\n'

print "vara =  ",vara,'\n\n'
print "def_tuple =  ",def_tuple,'\n\n'