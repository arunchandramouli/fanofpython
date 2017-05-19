
'''	
	Aim :: To demonstrate the use of a list - copy and deepcopy
'''

import copy

'''
	Create a simple list
'''


listA = [1,2,3,4,6,7,3,[100,400,200,600,800,900]]

'''
	Create both shallow and deepcopy
'''


print "\n\n" , "Making a shallowcopy ... ",'\n\n'

listAShallow = listA[:]



'''
	Iterate the lists and find out address of each element
'''

def iterate_address(listA,listB):

	for i , j in zip(listA,listB):

		print id(i),id(j), i , j,'\n\n'



'''
	Before modification of lists - check address
'''

print "Before modification of lists - check address",'\n\n'
iterate_address(listA,listAShallow)

'''
	Output ::

		18834232 18834232


		18834208 18834208


		18834184 18834184


		18834160 18834160


		18834112 18834112


		18834088 18834088


		18834184 18834184


		20679304 20679304 -> Sublists in listA and listAShallow have same addresses , this is trouble since it's mutable,
							 modification of any item will reflect in both the lists

'''



'''
	Modify the Sublist in the list
'''

listAShallow[7][5] = ['Great','High']
listAShallow[7].append(['Batman','Robin',range(10)])


'''
	After modification of lists - check address
'''

print "After modification of lists - check address",'\n\n'
iterate_address(listA,listAShallow)


'''
	Output ::


			17851192 17851192 1 1


			17851168 17851168 2 2


			17851144 17851144 3 3


			17851120 17851120 4 4


			17851072 17851072 6 6


			17851048 17851048 7 7


			17851144 17851144 3 3


			20744840 20744840 [100, 400, 200, 600, 800, ['Great', 'High'], ['Batman', 'Robin', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]] 
			[100, 400, 200, 600, 800, ['Great', 'High'], ['Batman', 'Robin', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]

			 - As we can see both are modified

'''



'''

	Making  a deepcopy and editing the lists

	In the previous example, we made a shallow copy -listAShallow = listA[:] , now deepcopy would be listADeep = listA[::]

	When a deep copy is made , each and every element in listA will be copied and placed in a different memory location

'''

print "\n\n" , "Making a deepcopy ... ",'\n\n'


'''
	Create a simple list
'''


listA = [1,2,3,4,6,7,3,[100,400,200,600,800,900]]



listADeep = copy.deepcopy(listA)



'''
	Before modification of lists - check address
'''

print "Before modification of lists - check address",'\n\n'
iterate_address(listA,listADeep)



'''
	Modify the Sublist in the list
'''

listA[7][5] = ['Great','High']

'''
	After modification of lists - check address
'''

print "After modification of lists - check address",'\n\n'
iterate_address(listA,listADeep)
