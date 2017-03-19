
'''
	Aim :: Express various object types in python
'''


'''
	Create a simple class Alpha
'''

class Alpha(object):

	def Wow(self):

		return 'Wow'


'''
	Now Create an instance
'''

x = Alpha()

y = x

'''
	Make a dictionary with x , y
	We know the fact that dict doesn't accept duplicate keys
'''
print {x:True,y:False}

'''
	Access Alpha
'''

print 'id(x) and id(y) ', id(x) ,id(y),'\n' # Same memory location
print "Via x ",'\n',x.Wow(),'\n'
print "Via y ",'\n',y.Wow(),'\n'

'''
	Now Modify x and check if it works for y
	# It will
'''

x.value = 1000

print "Via x ",'\n',x.value,'\n'
print "Via y ",'\n',y.value,'\n'


'''
	Now del x
'''

del x # use del keyword to delete stuff

'''
	y will still contain the value
'''
print "Via y ",'\n',y.value,'\n'
print "Via y ",'\n',y.Wow(),'\n'


'''
	Accessing Types
'''

print "type (Alpha) ==  %s  "%type(Alpha),'\n\n'
print "type (y) ==  %s  "%type(y),'\n\n'
