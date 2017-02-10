
from functools import wraps, partial
import logging

'''
	Set the logger
'''

logging.basicConfig(level = logging.INFO)
core_logger = logging.getLogger("Python")

'''
	Aim :: Write a function and access it.. In Simple Words, a function can 
	take a set of arguments as an input, and return the calculated result

	It can be used to perform repetitive actions
	
'''


'''
	A Function to print the sum of numbers
'''

def funcA(a,b,c):

	'''
		Add a,b,c and return the result

	'''

	sum_numbers = a + b + c 

	return sum_numbers


'''
	A Function to print the sum of 'n' numbers
'''

def funcB(args):

	'''
		Add all values in the container and return the result

		The function takes a container as an argument

	'''

	set_initial_sum = 0
	
	for i in args:
		set_initial_sum = set_initial_sum + i

	return set_initial_sum



'''
	A Function to print the sum of 'n' numbers given as *args

	* args means the program will accept any n.o. arguments seperated by a ","
'''

def funcC(*args):

	'''
		Add all values in the container and return the result

		The function takes any number of arguments

		*args is also known as a Tuple, a data-type in python that has values seperated by a "," 

	'''

	set_initial_sum = 0
	
	for i in args:
		set_initial_sum = set_initial_sum + i

	return set_initial_sum



'''
	A Function to print the sum of 'n' numbers given as a dictionary

	The program will accept any n.o. arguments given as a key, value pairs

	It is also known as dictionary, which is represented as key,value

'''

def funcD(kargs):

	'''
		Add all values in the container and return the result

		The function takes any number of arguments, given as key,value

	'''

	set_initial_sum = 0

	''' Iterate the dictionary and add the values '''
	
	for key,value in kargs.items():

		set_initial_sum += value

	return set_initial_sum




'''
	A Function to print the sum of 'n' numbers given as keyword arguments

	The program will accept any n.o. arguments given as a keyword

	It is represented as funcE(a=1,b=2,c=3,d=4,e=5)

'''

def funcE(**kargs):

	'''
		Add all values given as keyword arguments and return the result

		The function takes any number of arguments, given as keyword seperated by a ","

	'''

	set_initial_sum = 0

	''' Iterate the dictionary and add the values '''
	
	for key,value in kargs.items():

		set_initial_sum += value

	return set_initial_sum





'''
	A Function to print the sum of 'n' numbers given as *args and also keyword arguments

	The program will accept any n.o. arguments given as *args and as keywords

	It is represented as funcE(1,2,3,4,5, a=1,b=2,c=3,d=4,e=5)

'''

def funcF(*args,**kargs):

	'''
		Add all values given as a tuple and as keyword arguments and return the result

		The function takes any number of arguments, given as keyword seperated by a ","

		and also accepts values seperated by a ","

	'''

	set_initial_sum = 0

	''' Iterate the *args , the tuple and add the values '''

	for i in args:
		set_initial_sum += i

	''' Iterate the keyword arguments and add the values '''
	
	for key,value in kargs.items():

		set_initial_sum += value

	return set_initial_sum




if __name__ == "__main__":

	# ************************************************************************************** #
	
	''' Calculate sum of 3 numbers and return the result .. 
		if we dont pass 3 numbers , it will raise an exception
	'''

	print funcA(100,200,300)

	''' Here we pass a container and the function will add all values in the container and return the result '''
	print funcB([1,2,3,4,5]) # A container ,a list with 5 items
	print funcB(range(100)) # A container,a list with 100 items starting 0

	''' Here we can pass any n.o. arguments seperated by a ',' '''

	''' If we compare funcA to funcC,we can now get that funcC is better since it can accept any n.o arguments seperated by a "," '''

	''' *args is also known as a Tuple, a data-type in python that has values seperated by a "," '''

	print funcC(100,200,300)

	''' Here we can pass a dictionary with any n.o keys, values '''

	print funcD({1:100,2:200,3:300,4:400,5:500,6:600,7:700,8:800})


	''' Here we can pass keyword arguments and add all the values '''

	''' 
		*****  Please notice the difference between funcC and funcE below  *****

		In case of funcC which had *args we passed arguments seperated by a "," but in case of
		funcE we are passing arguments as keywords, say a=1,b=2 etc... seperated by ","

	'''

	print funcE(a=1000,b=2000,c=3000,d=4000,e=5000)


	'''  Here we are passing values seperated by "," and also keyword values seperated by "," '''

	print funcF(-1,-22,500,-900,10000,a1=500,ad=600,f2=90,df=55)


	# ************************************************************************************** #

