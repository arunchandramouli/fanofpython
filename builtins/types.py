
'''
	AIM: To demonstrate the use of builtin types

	- basestring, bool, buffer, classmethod,complex, dict,enumerate,file,frozenset
'''


# basestring
'''
	basestring is is used for assertions mainly
	It has 2 subclasses namely str and unicode
	It is abstract and not instantiable	
'''

print 'About .. basestring ','\n\n'

print basestring, type(basestring),basestring.__subclasses__()
print 'Assertions -- ','\n\n'
print isinstance(100,basestring) # int is not of type basestring - returns false
print isinstance('100',basestring) # str is basestring - returns true
print isinstance(u'100',basestring) # unicode is basestring - returns true

print ' . '*25,'\n\n'

'''
	bool -- Check for a Condition and returns true or false.
	bool is a subclass of int. While True is same as While 1
	You can pass an expression, but not a statement
'''
print 'About .. bool ','\n\n'

print bool("Luxury redefined!") # True
print bool() # Void hence returns False
print bool('')# Void hence returns False
print bool(10000) # True
print bool(10000>100000) # False
#print bool(if 10>20: True) # Invalid

while bool(10>20): # Wont run since condition fails
	print True

while bool(100>20): # Runs
	print 'True Run!!'
	break


print ' . '*25,'\n\n'


'''
	buffer -- Readonly buffer object! Can be used for slicing data
'''
print 'About .. buffer ','\n\n'

print buffer('') # None
print buffer('Hello Arun!') , buffer('Hello Arun!').__class__ # returns  Hello Arun! <type 'buffer'>
print buffer('Hello',0,9) # takes (obj,offset,size) -- returns 'Hello' since offset is 0.
#print buffer('Hello',-1,9) # Invalid - offset must be zero or positive!
print ' . '*25,'\n\n'

x = buffer("I Love to Code")
print buffer(x)

'''
 	complex - convert an integer to a complex number which has real and imaginary part!
'''

print 'About .. buffer ','\n\n'

print complex # returns <type 'complex'>
# print complex('arun') # invalid - malformed str

'''
	Output:
		Traceback (most recent call last):
		  File "types.py", line 70, in <module>
		    print complex('arun')
		  ValueError: complex() arg is a malformed string
'''
# Note you can pass a str , but it must be an int converted to str

# pass a valid string
print complex(100) # returns (100+0j)
# pass a valid string
print complex('100') # returns (100+0j)
# pass a complex number
print complex(complex(100)) # returns (100+0j)
# pass a float
print complex(1000.300) # returns (1000.3+0j)
# pass a float
print complex(10009990000.31110) # returns (10009990000.3+0j)
# pass a -ve number
print complex(-10000) # returns (-10000.9999889+0j)
# pass a -ve number
print complex(-10000.999988877) # returns (-10000+0j)
print ' . '*25,'\n\n'

# Get the real and imag parts

xx = complex(10000.99987)
print xx.real , xx.imag , xx # returns 10000.99987 0.0 (10000.99987+0j)


