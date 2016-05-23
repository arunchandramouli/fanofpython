'''
	Use Case:  Demonstrate the power of code object.
	Apply a function's code object to another function 
	and check the behavior

'''


# A Simple function

def iAmaSimpleFunc(age,sex,location):

	return age,sex,location

# Another Function
def func2(x,y,z,a):
	return x+y+z+a


# Codeobject of iAmaSimpleFunc
theCodeObject = iAmaSimpleFunc.func_code

print theCodeObject


'''
	Output:
	<code object iAmaSimpleFunc at 00000000005F9DC8, file "funccodes.py", line 10>
'''

# Codeobject of func2
theCodeObjectfunc2 = func2.func_code

print theCodeObjectfunc2

'''
	Output:
	<code object func2 at 00000000006764E0, file "funccodes.py", line 15>
'''

# Run both the Functions

print iAmaSimpleFunc(30,"Male",'CHN')

'''
	Output:
	(30, 'Male', 'CHN')
'''

print func2(1,2,3,4)

'''
	Output:
	10
'''

# Now assign the codeobject of func2 to iAmaSimpleFunc and check it's behavior

iAmaSimpleFunc.func_code = func2.func_code

#print iAmaSimpleFunc(30,"Male",'CHN') # It will raise an Exception, since different codeobject was assigned in previous step!

'''
	Output:
		Traceback (most recent call last):
		  File "funccodes.py", line 60, in <module>
		    print iAmaSimpleFunc(30,"Male",'CHN')
		  File "funccodes.py", line 16, in func2
		    return x+y+z
	    	TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# Lets Analyze why it raised an exception

'''
	As per iAmaSimpleFunc we expect it to return a tuple namley age (int) ,sex (str) and location (str).
	But func2 returns sum of x,y,z,a .. all ints. 
	After assigning the codeobject the arguments get changed;

	iAmaSimpleFunc.func_code = func2.func_code

'''

# Now let's print and analyze the attributes of codeobject! It will print attributes of func2 :-)

print iAmaSimpleFunc.func_code.co_argcount # returns  4
print iAmaSimpleFunc.func_code.co_cellvars # returns  ()
print iAmaSimpleFunc.func_code.co_varnames # returns  ('x', 'y', 'z', 'a')