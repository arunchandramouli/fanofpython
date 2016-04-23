
# Import the abc module

import abc

'''

	 Implementation of Abstract base class . Classes inheriting the abstract base class a.k.a abc must 

	 override all of the super class methods else interpreter will raise an Error - NotImplementedError

	 In real life the Use Case is the abc acts as an interface and ensures that it's subclasses are properly defined.

	 The ABC can also be a Metaclass

	 @abc.abstractmethod is a decorator to the function

'''

'''

	Note - In this tutorial we will use class IamAbstract as a metaclass for class InheritAbc

	In the example module abstractmodules.py we used inheritance, that is not the best way to make it abstract.

	Key Points:
	-----------

		*** In the baseclass If I decorate a method with decorator @abc.abstractmethod it means that it has to be overridden in the subclasses. 
			Also not all the methods of the abstract base class needs to be overridden ***

		***	When we declare __metaclass__ = abc.abcmeta  inside a class's body it means it is an abstract base class ***

		*** It is not necessary for all the methods of an abstract base class to be an abstractmethod, we need to be sure
		that in the subclass we do override the methods that are defined as @abc.abstractmethod in the superclass ***

'''


class IamAbstract(object):

	__metaclass__ = abc.ABCMeta

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


	@abc.abstractmethod
	def readTheConfig(instance):
	
		'''
			Read the Config line by line
		'''
		raise NotImplementedError

	@abc.abstractmethod	
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

	Now Let's create a class InheritAbc that inherits IamAbstract

	We are suppossed to override the metaclass's methods because they have been defined as abstract else
	interpreter will raise an exception
'''

class InheritAbc(IamAbstract):

	pass


# Create an object of InheritAbc --- It will show an error here

objectAbcs = InheritAbc()


'''

	Extract from Output Window:

	Traceback (most recent call last):
		  File "abcswithmetaclass.py", line 124, in <module>
		    objectAbcs = InheritAbc()
		TypeError: Can't instantiate abstract class InheritAbc with abstract methods parseTheInputs, readTheConfig

'''