'''
	Use Case:  Understanding the problem of circular imports

	Here module circular1.py will import circular2.py which is in the same directory and vice-versa

	For causing circular imports the python files could be in any directory.

	*** Note: It is important to avoid circular imports since it causes errors during execution. ***
'''

# I am importing a class named UserDefined from circular1 - *** This will cause an Error ***
from circular1 import UserDefined 

class Users(object): # A new-style class inherits from object


	# An instance method
	def instanceMet(this):

		return ' Hello - I am an Instance Method from class :: Users'


	# A Class method
	@classmethod
	def klassMet(that):

		return ' Hello - I am a Class Method from class :: Users'


 #When i ran this module I got NameError, as shown below;
'''
	Output: 

			D:\Code\holy\python\presentation\fanofpython\modules>D:\python26\python circular2.py
			Traceback (most recent call last):
			File "circular2.py", line 11, in <module>
			    from circular1 import UserDefined
		  	File "D:\Code\holy\python\presentation\fanofpython\modules\circular1.py", line 11, in <module>
		    	from circular2 import Users
		    File "D:\Code\holy\python\presentation\fanofpython\modules\circular2.py", line 11, in <module>
		    	from circular1 import UserDefined
			ImportError: cannot import name UserDefined

'''


'''
	Reason for Error: 

	 When I ran circular2.py , the first line has an import statement --- from circular1 import UserDefined
	 In the module circular1.py  , the first line has an import statement --- from circular2 import Users
	 These 2 imports collide and causes a cycle and we get an exception "ImportError"
'''