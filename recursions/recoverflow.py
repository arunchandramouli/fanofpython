import sys

sys.setrecursionlimit(10)


'''
	Use Case:- Demonstrate Stackoverflow (recursion overflow!) - How to cause maximum recursion depth exceeded state?

	*** Please make sure that you don't actually do this in Dev/Staging/PROD. I have given given it as an example case
	to make it clear and self realize that the mistake isn't done at any stage ***

	__getattribute__ will not work with Old Style Classes!

	Given below are the few examples of Recursion!

'''

'''
	A Simple class whose __getattribute__ causes recursion
'''

class Recursion(object):

	def  __init__(self):
		self.klass = self.__class__


	def __getattribute__(self,name):

		#print self, ' ' , name		

		return getattr(self,name) # Recursion occurs since __getattribute__ is called by getattr() again!
		# The fix is here: - return super(Recursion,self).__getattribute__(name) or return object.__getattribute__(self,name)
		

# Uncomment the line below to feel recursion
#theRecursion = Recursion() 

##print theRecursion


'''
	Here inner function causes recursion since a function cannot call itself!
'''

def iAmNotRecursive(*args):

	def iAmRecursive():

		return args

	return iAmNotRecursive() # A function calls itself, hence recursive
	# The fix is here: - return iAmNotRecursive or return iAmRecursive

##print iAmNotRecursive(range(10))


'''
	Again an inner function causes recursion!
'''
def iAmNotRecursive(*args):

	def iAmRecursive():

		def amIRecursive():

			return 'Foolish!'

		return iAmRecursive() # A function calls itself, hence recursive
		# The fix is here: - return iAmRecursive or return amIRecursive

	return iAmRecursive


#print iAmNotRecursive(range(10)).__call__()


'''
	Function below causes recursion since else block increments infinitely!
'''
# A recursion
def calcsum(n):

	if n == 0: 
		return n
	else:
		return n+calcsum(n+1) # The fix is here: - return n+calcsum(n-1)

#print calcsum(10)


'''
	Here's an example of tail recursion causing infinite overflow! -- else block increments infinitely!
'''

# The tail recursion

def calcsumz(n,theVals):

	if n == 0: 
		return theVals
	else:
 
		return calcsumz(n+1,theVals+n) # The fix is here: - calcsumz(n-1,theVals+n)

#print 'calcsumz --', calcsumz(10,10)



'''
	Causing recursion while using Proxy class!
'''

'''
	Let's say I have class Main and Class Proxy, I pass the instance of Main to Proxy to access the former's attributes
	__getattribute__ will again cause recursion overflow
'''

# The Main Class
class Main(object): # Will work with Old Style Class also


	_x = 10000

	def caller(self):

	  	return True

# Proxy Class
class Proxy(object):
	
	def __init__(self,getObj):

		self._main = getObj


	def __getattribute__(self,name):

		return object.__getattribute__(self._main,name) 
		# Recursion occurs since __getattribute__ is called by self._main!
		# The Fix is return object.__getattribute__(self,name) .. but that still doesn't give us the required result!
		# Use __getattr__ to get the result please refer path: patterns/proxy.py

xProxy = Proxy(Main())

#print xProxy,xProxy._x




'''
	Here we override the __getattribute__ of an ordinary class and 
	let's cause recursion overflow again! :-)
'''


class OrdinaryClass(object):

	def __init__(self,a,b):
		
		self.a = a
		self.b = b

	def __getattribute__(self,names):

		return self.a # Recursion occurs since __getattribute__ is called by self.a . A function cannot call itself!
		# The Fix is object.__getattribute__(self,names)


objectOrdinaryClass = OrdinaryClass(100,200)
print objectOrdinaryClass.a # causes overflow