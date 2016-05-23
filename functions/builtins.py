import __builtin__
'''
	Use Case:  Demonstrate the use of builtin functions!

	--> compile
	--> eval
	--> exec
'''


# Compile - Create a codeobject

# using exec
print compile('1+1',__name__,'exec') # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

# using eval - We can compile an expression but not a statement
print compile('1+1',__name__,'eval') # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

#using exec compile a statement

print compile('print 1+1','stmts','exec') # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

#using eval compile a statement will raise an exception

#print compile('print 1+1','stmts','eval') # will raise an exception

#using exec compile a statement

print compile('aaa = 1+1','stmts','exec') # returns <code object <module> at 00000000011254E0, file "__main__", line 1>

exec(compile('aaa = 1+1','stmts','exec')) # pass the codeobject

print aaa # returns 2
print eval("aaa") # returns 2

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
print Alpha, eval('Alpha') # returns __main__.Alpha __main__.Alpha ..the class got created

# Access the attributes of Alpha ! and it works!!
print Alpha.mem1
print Alpha.mem2
print Alpha.mem3

'''
	Output:
		<unbound method Alpha.mem1>
		<classmethod object at 0x00000000012CFEB8>
		<unbound method Alpha.mem3>
'''
# using exec - class gets created and populate the container

tempdict = {}

exec classA in tempdict # dictionary gets populated
print tempdict.keys() # returns ['__builtins__', 'Alpha']


'''
	Exploring __builtins__
'''

print tempdict.__getitem__('__builtins__') # same as __builtin__ . It's just an alias for __builtin__


assert __builtin__.__dict__ == __builtins__.__dict__ # True