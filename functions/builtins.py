import __builtin__
'''
	Use Case:  Demonstrate the use of builtin functions!

		--> compile
		--> eval
		--> exec

	All the 3 above takes only string,file or codeobject!
'''


# Compile - Create a codeobject

# using exec
print compile('1+1',__name__,'exec'), '\n\n' # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

# using eval - We can compile an expression but not a statement
print compile('1+1',__name__,'eval'), '\n\n' # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

#using exec compile a statement

print compile('print 1+1','stmts','exec'), '\n\n' # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

#using eval compile a statement will raise an exception

#print compile('print 1+1','stmts','eval'), '\n\n' # will raise an exception

#using exec compile a statement

print compile('aaa = 1+1','stmts','exec') # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

exec(compile('aaa = 1+1','stmts','exec')) # pass the codeobject

print aaa, '\n\n' # returns 2
print eval("aaa"), '\n\n' # returns 2

''' 
	Sample Class
'''

classA = '''   
class Alpha:
	def mem1(cls):
			return True

	def mem2(cls):
			return False
 	mem2 = classmethod(mem2)			


	def mem3(cls):
			return 100
 	mem2 = staticmethod(mem2)			


	def instanceMem(cls):
			return cls
			 	
'''
# using exec - class gets created - do not use exec this way as it alters the namespace!!
exec classA 

#Now use classA and operate on it...
# After exec classA using eval('Alpha') results in an answer!
print Alpha, eval('Alpha'), '\n\n' # returns __main__.Alpha __main__.Alpha ..the class got created

# Alpha's __dict__

print Alpha.__dict__, '\n\n'

# Access the attributes of Alpha ! and it works!!
print Alpha.mem1, '\n\n'
print Alpha.mem2, '\n\n'
print Alpha.mem3, '\n\n'

'''
	Output:
		<unbound method Alpha.mem1>
		<classmethod object at 0x00000000012CFEB8>
		<unbound method Alpha.mem3>
'''
# using exec - class gets created and populate the container

tempdict = {}

exec classA in tempdict # dictionary gets populated
print tempdict.keys(), '\n\n' # returns ['__builtins__', 'Alpha']


'''
	Exploring __builtins__
'''

#print tempdict.__getitem__('__builtins__'), '\n\n' # same as __builtin__ . It's just an alias for __builtin__


assert __builtin__.__dict__ == __builtins__.__dict__ # True

'''
	Using exec inside a function and exec'ing a string as shown below....
'''

newBie =  '''class execIsMagic:pass'''

def myFuncwithExec(a):

	exec a # When you exec inside the function, the class execIsMagic is not visible outside this scope...
	print execIsMagic # returns __main__.execIsMagic
	return eval('execIsMagic')

# pass the string as a parameter to the function and exec it
print myFuncwithExec(newBie) # returns __main__.execIsMagic

#print execIsMagic # raises an exception since it is not visible @ this global scope

'''
	Output: 

		Traceback (most recent call last):
		File "builtins.py", line 111, in <module>
	    print execIsMagic # raises an exception
		NameError: name 'execIsMagic' is not defined
'''


# Now compile and pass the codeobject as a parameter!

print myFuncwithExec(compile(newBie,'grand','exec')) # returns __main__.execIsMagic