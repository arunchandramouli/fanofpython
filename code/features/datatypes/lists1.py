
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
	Empty Mutable Types ...
'''

list1 = []

dict1 = {}

set1 = set()


'''
	Empty Immutable Types ...
'''

tuple1 = ()

str1 = ""





'''
	Define a simple list with multiple datatypes
'''

def_list = [1,2,"1","100","Python","Anne","A!@345<>_()",True,False,{1:100,2:200,3:300},range(10)]


'''
	Now create a variable	
'''

vara = def_list

'''
	Modification of vara will result in modifying def_list
'''

vara.append("Hero")

print "Address of vara and def_list %s and %s "%(id(vara),id(def_list)),'\n\n'
print "vara = %s "%(vara),'\n\n'
print "def_list = %s "%(def_list),'\n\n'


'''
	
	Now creating a Partial Slice ...

	When a slice is created partially , we are actually breaking a container
	into pieces , hence it shall represent a new memory location.
	Hence modification of such will not affect the original container

'''

getmeasliceofit = def_list[3:]


print "Address of getmeasliceofit and def_list %s and %s "%(id(getmeasliceofit),id(def_list)),'\n\n'
print "getmeasliceofit = %s "%(getmeasliceofit),'\n\n'
print "def_list = %s "%(def_list),'\n\n'





'''
	
	Now creating a Full Slice ...

	When a slice is created fully , we are actually creating a container
	which has its original values but represents the same address.
	Hence modification of such will affect the original container

	for eg :: 
	
	If you verify all of the address below, but for getmeasliceofit, rest are all the same

	if I edit as def_list[0:] = range(5) , def_list will also get modified
	Meanwhile also If I edit as def_list[3:] = range(5), def_list will get modified
	But If I edit getmeasliceofit def_list will not get modified

'''

getmeasliceofit = def_list[:]


print "Address == ",id(def_list),'\n',id(def_list[3:]),'\n',id(getmeasliceofit),'\n',id(def_list[::]),'\n',id(def_list[0:]),'\n',id(def_list[:]),'\n'


'''
	Modifying def_list[3:] will affect def_list , but modifying getmeasliceofit doesn't
	This is because getmeasliceofit resides at a different memory location.
'''

print '\n\n' , def_list , '\n\n'

def_list[3:] = range(50)
getmeasliceofit = None

print def_list , '\n\n\n',def_list[3:],'\n\n' , getmeasliceofit,'\n\n\n'



print 'Analyze memory locations of mutables examples ... ... ','\n\n'

sayx = [1,2,3,4,5]
print id(sayx),'\n'


sayx = [4,5,6,7,8]
print id(sayx),'\n'

x = range(10)

print id(x),'\n'

x = range(10,50)

print id(x),'\n'



print 'Modify a mutable it shall still refer same location  ... ... ','\n\n'

''' A Simple list '''
sayx = [1,2,3,4,5]
print id(sayx),'\n'

''' A Simple list modified - change element @ position 4 '''
sayx[4] = range(10)
print id(sayx),'\n'