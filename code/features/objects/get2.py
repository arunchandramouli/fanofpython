
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