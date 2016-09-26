import mutable_funcs

'''
	AIM: To inspect and determine the type of objects without using inspect module
'''

# How do check if an object is of type class

print mutable_funcs.A # returns <class 'mutable_funcs.A'>
x =  dir(mutable_funcs.A)

y = dir(mutable_funcs.foobarz)


print x , ' \n\n',y

