
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
	
	
	Let us explore methods of a list
'''



'''
	Define a simple list with multiple datatypes
'''

def_list = [1,2,"1","100","Python","Anne","A!@345<>_()",True,False,{1:100,2:200,3:300},range(10)]



#print dir(def_list)

'''

	['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__',
	 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', 
	 '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
	 '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', 
	 '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

'''


'''
	Adding values to the list
	append takes only 1 argument
'''

'''
	Passing a string to append
'''
def_list.append("John") # This will be added as the last element

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'


'''
	Passing a tuple to append
	This tuple will remain as a tuple item inside the list
	But if you use extend it be shown as multiple items
'''

def_list.append(("John","Mike","Antony")) # This will be added as the last element

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'


'''
	When we want to extend the existing list with other args
	we can use extend, it will also take only 1 argument

	The difference is the list gets extended

'''

def_list.extend(range(-4,10)) # This will be added as the last element

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'

'''
	Use insert if you want to modify a certain position
	Say position 2 with value as "Tom & Jerry"
'''

def_list.insert(2,"Tom & Jerry")

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'


'''
	Lets pop an element using pop method

	The last element to be added will be first element to be popped out
	if we dont specify any position


'''

def_list.pop()

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'



'''
	Lets pop an element using pop method

	The last element to be added will be first element to be popped out
	if we dont specify any position

	Here we specify index as 7 , if its not valid
	we will get index error

	
'''

def_list.pop(7)

print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'



'''
	Lets remove an element using remove method

	We also need to specify at which value do we need to remove

	Say we want to remove value 2
	If the value doesnt exist no exceptions will be shown
'''


def_list.remove(2)


print "def_list updated ... %s "%(def_list),'\n\n' ,id(def_list),'\n\n\n\n'