

'''
    Use Case: Explore the dictinory object of the super-class and the sub-class

    --> The Class dictionary will display the class-level variables, methods and other attributes, it will not have
    visiblity on the instance specific attributes that are declared inside the __init__ method of a class, those will be
    available in the dictionary of the class's instance.

    --> When class A(B) i-e- when Class A inherits Class B, A or it's instance's dictionary will not have info about Class B
'''

# Global Variable
willHappenSoon = True

# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object

    '''
        A class with instance, class and static methods
    '''

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
        A class InheritsUserDefined that inherits the base class UserDefined

        Note: In case we don't override the super class's __init__, we couldn't be able to set
        any instance specific attributes in the sub-class __init__. A reference to superclass and then
        adding instance specific attributes in the sub-class is the right way that ensures that sub-class
        has access to superclass and it's own instance specific attributes.

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



'''
    Examine the dictionary of super-class UserDefined

    The Class dictionary will display the class-level variables, methods and other attributes, it will not have
    visiblity on the instance specific attributes that are declared inside the __init__ method of a class, those will be
    available in the dictionary of the class's instance.
'''

print UserDefined.__dict__

'''

   Output:
        {

        'klassMethod': <classmethod object at 0x1104AFD0>, --> The Classmethod defined inside the class body

        '__module__': 'playground.Arun_Chandramouli.tests', --> Comes by default, refers to the module in which the class resides

        'fooGetter': <property object at 0x11048CF0>, --> The Property defined inside the class body

        '__dict__': <attribute '__dict__' of 'UserDefined' objects>, --> The Class's dictionary Object

        '_UserDefined__private': 'You cant access me !', --> Private attributes such as __private are stored this way

        'Mark': 'C++', --> Class level attribute

        'instanceMethod': <function instanceMethod at 0x1105D1B0>,  --> The instance method defined inside the class body

        'Allison': 'Python',  --> Class level attribute

        'staticMethod': <staticmethod object at 0x10CE9410>,  --> The static method defined inside the class body

        'Arun': 'Python',  --> Class level attribute

        '__weakref__': <attribute '__weakref__' of 'UserDefined' objects>, --> Comes by default, refers to the weakref module

        '__doc__': '\n        A class with instance, class and static methods\n    ',  --> The doc info of the Class

        '__init__': <function __init__ at 0x1104EEB0> --> The class constructor defined inside the class body

            }
'''


'''
    Examine the dictionary of sub-class InheritsUserDefined

    *** It will not have any Info on the Super-Class ***
'''
print InheritsUserDefined.__dict__


'''

   Output:

    {

    'klassMethod': <classmethod object at 0x1105B650>, --> The Classmethod defined inside the class body

    'instanceMethod': <function instanceMethod at 0x1105C3F0>,  --> The instance method defined inside the class body

    '__module__': 'playground.Arun_Chandramouli.tests', --> Comes by default, refers to the module in which the class resides

    'fooGetter': <property object at 0x1105A720>,  --> The Property defined inside the class body

    'staticMethod': <staticmethod object at 0x1105B630>,   --> The static method defined inside the class body

    '__doc__': "\n        A class InheritsUserDefined that inherits the base class UserDefined\n\n
    Note: In case we don't override the super class's __init__, we couldn't be able to set\n
    any instance specific attributes in the sub-class __init__. A reference to superclass and then\n
    adding instance specific attributes in the sub-class is the right way that ensures that sub-class\n
    has access to superclass and it's own instance specific attributes.\n\n    ",   --> The doc info of the Class

    '__init__': <function __init__ at 0x1105C430>  --> The class constructor defined inside the class body

    }
'''
