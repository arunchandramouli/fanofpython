
'''
        Use Case:  Exploring the User defined Class, making instance-specific attributes available to
        classmethod and staticmethod
'''

# User defined classes are those that aren't builtin


# Global Container

containerGlobal = {}

class UserDefined(object): # A new-style class inherits from object


    # Declaring Class level Attrs - visible for class and it's instance

    Arun,Allison,Mark = 'Python','Python','C++'


    def __init__(me):

        '''
            The Constructor to initialize the attributes
        '''

        me._foo = me.__class__.__name__
        me.instanceContainer = []
        me.instanceContainer.append(me._foo)
        setattr(me.__class__,"instanceContainer",me.instanceContainer)
        #containerGlobal["instanceContainer"] = me.instanceContainer
        containerGlobal.__setitem__("instanceContainer",me.instanceContainer)


    def instanceMethod(this):

        return 'Hello - I am an Instance Method -- > class name - %s , container - %s'%(this._foo,this.instanceContainer)


    @classmethod
    def klassMethod(that):
        print "I can access instance specific attribute - container %s "%that.instanceContainer
        return ' Hello - I am a Class Method'


    @staticmethod
    def staticMethod(): # There is no positional param for static method, if specified must be given value by the user
        print "I can access instance specific attribute - container %s "%containerGlobal["instanceContainer"]
        return ' Hello - I am a Static Method'


objUserDefined = UserDefined()
print objUserDefined.instanceMethod()
objUserDefined.klassMethod()
objUserDefined.staticMethod()
