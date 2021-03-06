
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
	Are all of the types callable ??
'''


print hasattr(alist,'__call__'),'\n\n',list(),'\n\n'
print hasattr(atuple,'__call__'),'\n\n',tuple(),'\n\n'
print hasattr(adict,'__call__'),'\n\n',dict(),'\n\n'
print hasattr(AClass,'__call__'),'\n\n',AClass(),'\n\n'
print hasattr(love,'__call__'),'\n\n',love(),'\n\n'



print list == list() , list.__class__ , list().__class__,id(list()),id(list)