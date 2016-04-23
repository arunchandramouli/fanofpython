
# Import the abc

import abc

'''

	 Implementation of Abstract base class . Classes inheriting the abstract base class a.k.a abc must override all of the super class methods else
	 interpreter will raise an Error - NotImplementedError

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
