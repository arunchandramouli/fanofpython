
import re

'''
	Aim :: Express various object types in python

	Anything to the right side of that '=' sign is an object in python
	and one to the left hand side the name binding to that object
'''


'''
	A list
'''

alist = [1,2,3,4,True,False]
'''
	A tuple
'''

atuple = (1,2,3,4,True,False)

'''
	A Dict
'''

adict = {1:1,2:2,3:3,4:4,False:True}

'''
	A Class
'''

class AClass :pass

aclass = AClass
aclassinstance = AClass()
aclassinstance1 = aclass()

'''
	A Function
'''

def love():

	return "I love my code .. {My Life is Code } "

saylove = love()




'''
	Are all of the types hashable ? ?
'''


print hasattr(alist,"__hash__")



'''
	Check for contains
'''
somelist = ["Robert De Niro","Angelina Jolie","Brad Pitt","Emma Watson","Roger Federer","Annabelle"]

'''
	Check for a substring Ang in that lst
'''

'''
	Using __contains__
'''
for items in somelist:

	if items.__contains__("Ang"):

		print items

	if "Ang" in str(items):

		print items


'''
	Using RE
'''
for items in somelist:

	''' 
		re.search -> This will return True if substring Ang is present 
		in any part of the string 
		Say it return True for Anglais as well as Language - We will convert both to lower
	'''
	if re.search("son".lower(),items.lower()):

		print items

	if re.match("Em".lower(),items.lower()):

		print items

