

'''
	Use Case: Demostrate the concept of Tail Recursion
	Differentiate it from ordinary recursion
'''


'''
	An Ordinary recursion function to calc factorial - product

	This function is not tail recursive
'''

def calctheProduct(intn):

	if intn == 0 : 
		return 1

	else :

		return intn * calctheProduct(intn-1)


print calctheProduct(5)


'''
	Now let us write a tail recursive function

	A function is said to be tail recursive if the return value of the function is the final thing to be computed!
'''

def iAmTailRecursive(intn,theValue):

	if intn == 0:
		return theValue # Here you must return the param 'theValue'

	else:

		return iAmTailRecursive(intn-1, intn+theValue) # Last thing to be returned

print iAmTailRecursive(10,10)