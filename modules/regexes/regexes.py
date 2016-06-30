'''
	Use Case:  Understanding the regular expressions

'''


import re





'''
	Get results from the generator object
'''

def gen(getData):
	
	try:
		while True:

			print getData.next()

	except StopIteration as SI:
		print SI

	finally:

		print "Task Completed!"



'''
	Compile :: re.compile
'''


def re_compile(textString,compile_str):

	'''
		Compile and check pattern
	'''

	'''
		param textString :: String to be searched
		param compile_str :: list -> All the elements will be compiled
		yield match object and the string
	'''

	getRegex = [re.compile(data) for data in compile_str]
	

	for data in getRegex:

		gets = data.search(textString)
		if bool(gets):yield data,gets.re.pattern # Yield both pattern and the string
			
 	return # return None is legal inside generator

getData = re_compile("Arun is in London",["Arun","Kumar"])



'''
	Finding multiple matches
'''

def multipleMatches(pattern,string):

	'''
		pattern :: The Pattern to find in the String
		string :: The string being examined
		yield list of matched strings
	'''

	yield re.findall(pattern, string)
			


gen(multipleMatches('ab','abbaaabbbbaaaaa'))





'''
	Finding multiple matches - finditer
'''

def multipleMatches_findIter(pattern,string):

	'''
		pattern :: The Pattern to find in the String
		string :: The string being examined
		yield match object and matched string
	'''

	for data in re.finditer(pattern, string): yield data,' --- ',data.re.pattern
			


gen(multipleMatches_findIter('ab','abbaaabbbbaaaaa'))



