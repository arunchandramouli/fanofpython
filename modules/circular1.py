'''
	Use Case:  Understanding the problem of circular imports

	Here module circular1.py will import circular2.py which is in the same directory and vice-versa

	For causing circular imports the python files could be in any directory.

	*** Note: It is important to avoid circular imports since it causes errors during execution. ***
'''

from circular2 import Users

class UserDefined(object): # A new-style class inherits from object


	# An instance method
	def instanceMethod(this):

		return ' Hello - I am an Instance Method'


	# A Class method
	@classmethod
	def klassMethod(that): # that has no clue whatsoever about instance specific _foo

		return ' Hello - I am a Class Method'

