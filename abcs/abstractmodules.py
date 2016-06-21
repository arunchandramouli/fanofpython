
# Import the abc module

import abc

'''

	 Implementation of Abstract base class . Classes inheriting the abstract base class a.k.a abc must 

	 override all of the super class methods else interpreter will raise an Error - NotImplementedError

	 In real life the Use Case is the abc acts as an interface and ensures that it's subclasses are properly defined.

	 The ABC can also be a Metaclass

	 @abc.abstractmethod is a decorator to the function

'''


class IamAbstract(object):

	'''

	  The following are the instance methods associated with the class
	  Aim - Do perform some basic operations on a Bank Account
	  We are gonna do;

	  	-> Read the File
	  	-> Parse the Records
	  	-> Split by Delimiter
	  	-> Validate the Data
	  	-> Filter by special rules
	  	-> Push to the Database

	'''


	def readTheConfig(instance):
	
		'''
			Read the Config line by line
		'''
		raise NotImplementedError


	def parseTheInputs(instance):
	
		'''
			Syntactic Analysis - Check if the Guidelines are followed
		'''
		raise NotImplementedError



	def splitByDelimiter(instance):
	
		'''
			Split by Delimiter - Split the inputs and send for validation
		'''
		raise NotImplementedError


	def validateTheInputs(instance):
	
		'''
			Business Analysis - Check if the rules are defined
		'''
		raise NotImplementedError


	def filterTheInputs(instance):
	
		'''
			Records Filter - A Special Case Scenario where-in I check for special i/p types in Banking Data
		'''
		raise NotImplementedError


	def pushToPyGrills(instance):
	
		'''
			Database Operation - All the filtered records are now pushed to the Database
		'''
		raise NotImplementedError

'''

	Now Let's inherit the Abstract Class and check for Implementation Errors
'''

class InheritAbc(IamAbstract):

	'''
		
		Here I declare a single instance method and it does really nothing
		I override only 1 method and ignored the rest
		While I run the run this module - interpreter will raise an Exception if I access the methods that aren't overridden

		*** The big disadvantage of this method is that the Error "NotImplementedError" 
		will be raised only if the non-overridden methods are accessed

	'''
	def readTheConfig(instance):

		return 'I read the Contents'


# Create an object of InheritAbc

objectAbcs = InheritAbc()

# Access the valid and overridden method

print objectAbcs.readTheConfig()

# Access the non-implemented method *** An Exception will be raised here ***

print objectAbcs.pushToPyGrills()


'''

Extract from Output Window:

	I read the Contents
	Traceback (most recent call last):
	  File "abstractmodules.py", line 120, in <module>
	    print objectAbcs.pushToPyGrills()
	  File "abstractmodules.py", line 87, in pushToPyGrills
	    raise NotImplementedError
	NotImplementedError
'''