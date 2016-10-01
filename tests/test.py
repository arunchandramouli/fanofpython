'''

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" 
instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''


def tests(randomNo):
	'''
		Takes a param and works on the condition above
	'''

	for i in range(1,randomNo):		
		
		if (i % 3 == 0 and i%5 == 0) : print 'FizzBuzz'
		elif i % 5 == 0 : print 'Buzz'
		elif i % 3 == 0 : print 'Fizz'
		else : print i

#tests(50)


'''
Write a function that takes a string as an input. The string contains items in a list separated by white spaces. 
The function should return a string with all duplicates in the list removed and in reverse order. 
E.g. "1 3 5 3 7 3 1 1 5" -> "7 5 3 1"
'''

# A list to hold filtered values;


def filters(data,newlist = []):
	'''
	 Take the data, split by the whitespaces and add to newlist
	 Reverse the newlist and return the value
	'''

	if not newlist is None : newlist = []
	getdata = data.split(" ") # Forms a list

	for vls in getdata: # Iterate and append
		if not vls in newlist: newlist.append(vls)

	return reversal(str(''.join(newlist)))


def reversal(inputs):
	'''
		Takes an inputs and reverses it
	'''
	sample = ''
	for i in reversed(inputs):	
		sample += i
		sample += ' '
	return repr(sample.rstrip())


print filters("1 3 5 3 7 3 1 1 5")


