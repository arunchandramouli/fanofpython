
# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


    #__slots__ = ['_fooGetter'] # limit the Attrs

    # Declaring Class level Attrs - visible for class and it's instance

    Arun,Allison,Mark,__private= 'Python','Python','C++','You cant access me !'

    def __init__(me,code):

        me._someVariable = "Java and Python, C#"
        me.codes = code

    @classmethod
    def klassMethod(that): # that has no clue whatsoever about instance specific _fooGetter

        print "Calling klassMethod :: Base class - ", "\n\n",that.Arun,that.Allison,that.Mark,that.code
        that.className = 'Users'
        return ' Hello - I am a Class Method :: Base Class'

    @classmethod
    def klassMethod2(that):

        print that.className
        return ' Hello - I am a Class Method'

    def instanceMethod(this):

        print "Calling instanceMethod :: Base class - ", "\n\n",this.Arun,this.Allison,this.Mark,this.code
        return ' Hello - I am an Instance Method :: Base Class'

    @staticmethod
    def staticMethod(nothingHere): # There is no positional param for static method, if specified must be given value by the uer

        return ' Hello - I am a Static Method'

    @property
    def fooGetter(they):
        return they._someVariable

    @fooGetter.setter
    def fooGetter(them,someThingfooGetterish):
        print "Setter " , them, ' ' ,someThingfooGetterish
        them._someVariable = someThingfooGetterish


class InheritsUserDefined(UserDefined):

    def __init__(me,code):

        #UserDefined.__init__(me,code)
        super(InheritsUserDefined,me).__init__(code)

    @classmethod
    def klassMethod(that): # Override the classmethod of the base class!

        print "Calling klassMethod :: Sub class - ", "\n\n",that.Arun,that.Allison,that.Mark
        return 'Hello - I am a Class Method :: SubClass'


    @property
    def fooGetter(they):
        print "Calling fooGetter :: Sub class - "
        return they._someVariable,they.Arun,they.Allison,they.Mark,they._someVariables,they.codes

    @fooGetter.setter
    def fooGetter(them,someThingfooGetterish):
        print "Calling fooSetter :: Sub class - "
        them._someVariable = someThingfooGetterish
        them._someVariables = someThingfooGetterish + ' & Thats pretty Cool!'


    @staticmethod
    def staticMethod(nothingHere):
        print "Calling staticMethod :: Sub class !"
        return ' Hello - I am a Static Method :: Sub-class !'

    def instanceMethod(this):

        print "Calling instanceMethod :: Sub-Class - ", "\n\n",this.Arun,this.Allison,this.Mark,this.codes,this._someVariable
        return ' Hello - I am an Instance Method :: Sub-Class'


# Creating an instance of the baseclass!
objInheritsUserDefined = InheritsUserDefined(InheritsUserDefined.__name__)

# Override Instancemethod

print "Override instanceMethod --- "
print objInheritsUserDefined.instanceMethod()


'''

# Override Classmethod
print "Override Classmethod --- "
print InheritsUserDefined.klassMethod()


# Override Property
print "Override Property --- "
objInheritsUserDefined.fooGetter = 'God is Beautiful!'
print objInheritsUserDefined.fooGetter

# Override Staticmethod
print "Override Staticmethod --- "
print objInheritsUserDefined.staticMethod('Nothing')
print InheritsUserDefined.staticMethod('Nothing')
'''
