
'''
        Use Case:  Exploring the User defined Class, checking the availability of attributes of methods in a class
'''

# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


    # Declaring Class level Attrs - visible for class and it's instance

    Arun,Allison,Mark = 'Python','Python','C++'


    def __init__(me):

        '''
            The Constructor to initialize the attributes
        '''

        me._foo = " Hello Java Guys!"
        me._java = "Coffee Mug!"

        me.instanceContainer = []
        me.instanceContainer.append(me._foo)
        me.instanceContainer.append("Python is dynamic")
        me.instanceContainer.append("Java is strongly typed")
        me.instanceContainer.append(1000)

        setattr(me.__class__,"peterEngland",me.instanceContainer)
        setattr(me.__class__,"iLoveJava",me._java)

        # setattr(object,name,value)

    def instanceMethod(this):

        return 'Hello - I am an Instance Method -- > class name - %s , container - %s'%(this._foo,this.instanceContainer)


    @classmethod
    def klassMethod(that):
        print "I can access instance specific attribute - container %s "%that.peterEngland
        print "I can access instance specific attribute - directly %s "%that.iLoveJava
        return ' Hello - I am a Class Method'


    @staticmethod
    def staticMethod(): # There is no positional param for static method, if specified must be given value by the user
        return ' Hello - I am a Static Method'


# Check if an object is callable

# Check for instance method
print hasattr(UserDefined.instanceMethod,"__call__") # if it returns True, then the object is callable

# Check for class method
print hasattr(UserDefined.klassMethod,"__call__") # if it returns True, then the object is callable

# Check for static method
print hasattr(UserDefined.staticMethod,"__call__") # if it returns True, then the object is callable


# List the content - Explore an object - using dir built-in function


# Check for instance method
print dir(UserDefined.instanceMethod) # List the contents applicable for an instance method

# Check for class method
print dir(UserDefined.klassMethod) # List the contents applicable for classmethod

# Check for static method
print dir(UserDefined.staticMethod) # List the contents applicable for staticmethod
