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
		

		if bool(gets):

			yield data,gets.re.pattern # Yield both pattern and the string , gets.group() also returns the string
			
 	return # return None is legal inside function that has a generator

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

	for data in re.finditer(pattern, string): 
		# yield match object and the pattern
		yield data,' --- ',data.re.pattern,' --- ',data.group()
			


gen(multipleMatches_findIter('abcd','abcdbaaabbbbaaaaa')) # returns value and states "Task Completed!"
gen(multipleMatches_findIter('12','abbaaabbbbaaaaa')) # just states "Task Completed!"



'''
	Forming groups from regular expression match object
'''

# Step 1 - Compile and get the object
getObject = re.compile('[a-z]+')

#Explore a compiled re-object

print dir(getObject)

# returns ['__copy__', '__deepcopy__', 'findall', 'finditer', 'match', 'scanner', 'search', 'split', 'sub', 'subn']

# Step 2 - findall :: get as a list 

findallmatches = getObject.findall("abbaaabbbbaaaaa1212abbcdefghy1985jklmnhgfrtyu")

print findallmatches # returns ['abbaaabbbbaaaaa', 'abbcdefghy', 'jklmnhgfrtyu']

# Step 3 - match/search and group

matchGroup = getObject.search("abbaaabbbbaaaaa1212abbcdefghy1985jklmnhgfrtyu")

print matchGroup.group() # returns abbaaabbbbaaaaa

p = re.compile('[a-z]*[0-9]*')
m = p.search('abcd1212klmnop')

print m.group() # returns abcd1212

# use findall and finditer on compiled re-object

m = p.findall('abcd1212klmnop')
print m # returns ['abcd1212', 'klmnop', '']


m = p.finditer('abcd1212klmnop')
print m # returns <callable-iterator object at 0x00000000012D1E48>
matchObject = m.next() # returns <_sre.SRE_Match object at 0x00000000011CA100>
print dir(matchObject) # returns ['__copy__', '__deepcopy__', 'end', 'expand', 'group', 'groupdict', 'groups', 'span', 'start']
# Get the match string and the pattern used from the match object
print matchObject.group(), ' - ', matchObject.re.pattern  # abcd1212  -  [a-z]*[0-9]*