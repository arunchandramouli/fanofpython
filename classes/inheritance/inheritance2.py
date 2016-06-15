'''
    Use Case: Explore the various scenarios of Inheritance

    Note: The instance specific attributes are visible only to the instance method of the class, unless
    explicitly set by the user and made available at the module or class level.
'''

# Global Variable
willHappenSoon = True

# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object

    # Declaring Class level Attrs - visible for class and it's instance, but not for static method!

    Arun,Allison,Mark,__private = 'Python','Python','C++','You cant access me !'

    def __init__(me,code): # Instance variable are visible only to the instance methods of a class

        me._someVariable = "Java and Python, C#"
        me.codes = code

    @classmethod
    def klassMethod(that): # that has no clue whatsoever about instance specific variables

        print "Calling klassMethod :: Base class - ", "\n\n",that.Arun,that.Allison,that.Mark
        that.className = 'Users'
        return ' Hello - I am a Class Method :: Base Class'

    def instanceMethod(this):

        print "Calling instanceMethod :: Base class - ", "\n\n",this.Arun,this.Allison,this.Mark,this.codes
        return ' Hello - I am an Instance Method :: Base Class'

    @staticmethod
    def staticMethod(nothingHere): # There is no positional param for static method, if specified must be given value by the uer

        return ' Hello - I am a Static Method ',willHappenSoon

    @property
    def fooGetter(they):
        return they._someVariable

    @fooGetter.setter
    def fooGetter(them,someThingfooGetterish):
        print "Setter " , them, ' ' ,someThingfooGetterish
        them._someVariable = someThingfooGetterish



# A class that inherits the UserDefined class
class InheritsUserDefined(UserDefined):

    # Override the __init__ of the super class
    '''
        Note: In case we don't override the super class's __init__, we couldn't be able to set
        any instance specific attributes in the sub-class __init__. A reference to superclass and then 
        adding instance specific attributes in the sub-class is the right way that ensures that sub-class
        has access to superclass and it's own instance specific attributes

    '''

    def __init__(me,code): 

        super(InheritsUserDefined,me).__init__(code)

    # Override the classmethod of the base class! - We are adding 2 more positional params here
    @classmethod
    def klassMethod(that,this,what): 

        print "Calling klassMethod :: Sub class - ", "\n\n",that.Arun,that.Allison,that.Mark
        return 'Hello - I am a Class Method :: SubClass'


    @property
    def fooGetter(they): # Override the base-class property descriptor
        print "Calling fooGetter.getter :: Sub class "
        return they._someVariable,they.Arun,they.Allison,they.Mark,they._someVariables,they.codes

    @fooGetter.setter
    def fooGetter(them,fooSets): # Override the base-class property descriptor
        print "Calling fooGetter.setter :: Sub class "
        them._someVariable = fooSets
        them._someVariables = fooSets + ' & Thats pretty Cool!'


    @staticmethod
    def staticMethod(): # Override the staticmethod of the base-class
        print "Calling staticMethod :: Sub class !"
        return ' Hello - I am a Static Method :: Sub-class !'

    def instanceMethod(this,param1,param2,*params,**superparams): # Override the instancemethod of the base-class

        print "Calling instanceMethod :: Sub-Class - ", "\n\n",this.Arun,this.Allison,this.Mark,this.codes,this._someVariable
        return ' Hello - I am an Instance Method :: Sub-Class'


# Creating an instance of the baseclass!
objInheritsUserDefined = InheritsUserDefined(InheritsUserDefined.__name__)

# Override Staticmethod - The calls below invoke the sub-class's staticmethod!
print "Override Staticmethod --- "
print objInheritsUserDefined.staticMethod()
print InheritsUserDefined.staticMethod()

print "\n\n"


# Override klassMethod - The calls below invoke the sub-class's classmethod!
print "Override klassMethod --- "
print objInheritsUserDefined.klassMethod("Hello","World")
print InheritsUserDefined.klassMethod("Yes","Happen!")

print "\n\n"


# Override instanceMethod - The calls below invoke the sub-class's instanceMethod!
print "Override instanceMethod --- "
print objInheritsUserDefined.instanceMethod("Hello","World")

print "\n\n"


# Override property - The calls below invoke the sub-class's property!
print "Override property --- "
objInheritsUserDefined.fooGetter = "Miami is a wonderful beach!"
print objInheritsUserDefined.fooGetter
print "\n\n"