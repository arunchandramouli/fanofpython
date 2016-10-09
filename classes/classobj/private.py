'''
    Use Case:  Exploring the User defined Class, checking the availability of attributes of methods in a class

    Exploring the Private Attributes
'''

# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


    # Declaring Class level Attrs - visible for class and it's instance

    Arun,Allison,Mark = 'Python','Python','C++'

    __private = 100000000

    ___name = 'Tim' # Triple or more than double underscores @ start of an attributes doesn't qualify to be private


    def __init__(me):

        '''
            The Constructor to initialize the attributes
        '''

        me._foo = " Hello Java Guys!"
        me._java = "Coffee Mug!"
        
        # Instance specific private variable - can be accessed only inside the instance methods
        me.__privateNew = 'Arun' 

        # Open a Container and add the values;
        me.instanceContainer = []
        me.instanceContainer.append(me._foo)
        me.instanceContainer.append("Python is dynamic")
        me.instanceContainer.append("Java is strongly typed")
        me.instanceContainer.append(1000)
        
        # When we set instance specific attrs using setattr to class, it can be accessed by classmethods
        setattr(me.__class__,"peterEngland",me.instanceContainer)
        setattr(me.__class__,"iLoveJava",me._java)


    def instanceMethod(this):

    	print 'I can access class level and instance level Private Attrs inside the instancemethod - %s : %s '%(this.__private, this.__privateNew)

    	print 'Name is %s '%this.___name

        return 'Hello - I am an Instance Method -- > class name - %s , container - %s'%(this._foo,this.instanceContainer)





    @classmethod
    def klassMethod(that):
    	
    	print 'I can access only class level Private Attrs inside the classmethod - %s : '%(that.__private)
        print "I can access instance specific attribute - container %s "%that.peterEngland
        print "I can access instance specific attribute - directly %s "%that.iLoveJava
        
        return "Hello - I am a Class Method"


    @staticmethod
    def staticMethod(): 

        # There is no positional param for static method, if specified must be given value by the user

        return ' Hello - I am a Static Method'


    def __privateFunction(instance):

    	return " Private Function inside the class"


objectNew = UserDefined()
print objectNew.instanceMethod()
print objectNew.klassMethod()

# Try and access the private function

#print objectNew.__privateFunction

'''
	Output ::

    	 Traceback (most recent call last):
		  File "private.py", line 78, in <module>
		    print objectNew.__privateFunction
		AttributeError: 'UserDefined' object has no attribute '__privateFunction'
'''