
'''	
	Aim :: To demonstrate the use of a list

	Define a simple list , add values to it and iterate and print it	

	A list consists of comma seperated values which could be of any type

	which is reprsented as [,,,,] .. all values are enclosed between '[' and ']'

	** A list object is a mutable datatype which means it couldn't be hashed
	Anything that can be hashed can be set as a dictionary key **

	Modifying an exisiting list will not result in a new list object,
	memory address will not be changed too.

	There are 2 scenarios of modification;

		-> Edit the existing item 

			-> Both Mutable and Immutable datatypes can be edited, memory location not changed
			
		-> Replace the existing item
	
			-> Both mutable and immutable can be replaced
	
	
'''



'''
	Define a simple list with multiple datatypes
'''

def_list = [1,2,"1","100","Python","Anne","A!@345<>_()",True,False,{1:100,2:200,3:300},range(10)]
