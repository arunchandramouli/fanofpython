
'''
	Aim :: Demonstrate modules and their purpose
'''

import m2



'''
	Execute funcA from module m2
'''

print m2.funcA(100)

'''
	A Function to append numbers to a list and return it

	***** 
			
			Here we have defined containery=[] which means that the container is initialized at function
			definition time .

	*****
'''

def funcB(containerx,containery=[]):

	'''
		Add numbers in containerx to containery and return it

		Parameters:

			containerx - A List of numbers
			containery - A List to add numbers from containerx
			return containery

	'''

	''' 
		Make sure containery is empty before the action .
		When we add this if condition before, the container gets re-initialized each time
		the function is called.
	'''

	if not containery is None : containery = []

	for numbers in containerx:
		containery.append(numbers)

	return containery




if __name__ == "__main__":

	funcB(range(100))