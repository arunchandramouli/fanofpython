
__author__ = 'Arun Chandramouli'


'''
 	Proxy class will hide the real details!
	Using the Proxy Pattern - the Client doesn't access the attributes of a class via the real instance
	but via the proxy instance!
'''

'''
 	Let's write a sample class to illustrate the behavior
'''

class TheMainSubject(object):

	'''
		Again let's take a simple but inrealistic example!
	'''

	def __init__(self,income,allownce,tax):
		self.income = income
		self.allownce = allownce
		self.tax = tax		

	
	def getTax(self):
		# A funny way to get the tax
		return self.tax * 10 if self.income > 10000000 else self.tax * 2

	def determineAllowances(self):

		# Let's say allowances are based on income level
		
		allowanceBands = {self.income:{
		self.income<10000:50,
		self.income>10000 and self.income < 25000:100, 
		self.income>25000 and self.income < 50000:500,
		self.income>50000 and self.income < 75000:1000,
		self.income>75000 and self.income < 100000:5000,
		self.income>100000 and self.income < 125000:7000,
		self.income>150000:10000}}

		return allowanceBands.__getitem__(self.income)[True]



objectTheMain = TheMainSubject(11000,200000,100)

print objectTheMain.getTax()
print objectTheMain.determineAllowances()


'''
	Now Let's use the Proxy object for the same class
'''


class TheGreatProxy(object):

	def __init__(self,klass):

		self.klass = klass

	def __getattr__(self,name):
		
		return getattr(self.klass,name)


# Now pass the instance objectTheMain into class TheGreatProxy

objectTheGreatProxy = TheGreatProxy(objectTheMain)

print 'Accessing via the Proxy! '

'''
 Note : When you create a proxy please note that the attributes that are visible to main instance are not applicable for proxt
 Uncomment code below to realize the same!
'''
#print objectTheMain.__class__.__dict__, '\n\n\n'
#print objectTheGreatProxy.__class__.__dict__
print objectTheGreatProxy.getTax()

print objectTheGreatProxy.determineAllowances()


'''
	The Class that inherits Proxy can access it too
'''

class IinheritProxy(TheGreatProxy):pass

		#def getTax(self):
		# A funny way to get the tax
		#print ' Getting tax from inherited class ! :-)'

		#return super(IinheritProxy,self).__dict__.__getitem__('klass').__class__.__dict__.__getitem__('getTax').__call__(self)



objectIinheritProxy = IinheritProxy(objectTheMain)

print 'Accessing via the Proxy inherited class ! '

print objectIinheritProxy.getTax()

print objectIinheritProxy.determineAllowances()

