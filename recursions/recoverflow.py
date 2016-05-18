import sys

sys.setrecursionlimit(10)


'''
	Given below are the few examples of Recursion!
'''

class Recursion(object):

	def  __init__(self):
		self.klass = self.__class__


	def __getattribute__(self,name):

		print self, ' ' , name		

		return getattr(self,name) # Recursion occurs since __getattribute__ is called by getattr()
		# The fix is here: - return super(Recursion,self).__getattribute__(name) or return object.__getattribute__(self,name)
		

# Uncomment the line below to feel recursion
#theRecursion = Recursion() 

#print theRecursion



def iAmNotRecursive(*args):

	def iAmRecursive():

		return args

	return iAmNotRecursive() # A function calls itself, hence recursive
	# The fix is here: - return iAmNotRecursive or return iAmRecursive

#print iAmNotRecursive(range(10))





def iAmNotRecursive(*args):

	def iAmRecursive():

		def amIRecursive():

			return 'Foolish!'

		return iAmRecursive() # A function calls itself, hence recursive
		# The fix is here: - return iAmRecursive or return amIRecursive

	return iAmRecursive


print iAmNotRecursive(range(10)).__call__()



# A recursion
def calcsum(n):

	if n == 0: 
		return n
	else:
		return n+calcsum(n+1) # The fix is here: - return n+calcsum(n-1)

print calcsum(10)




# The tail recursion


def calcsumz(n,theVals):

	if n == 0: 
		return theVals
	else:
 
		return calcsumz(n+1,theVals+n) # The fix is here: - calcsumz(n-1,theVals+n)

print 'calcsumz --', calcsumz(10,10)
