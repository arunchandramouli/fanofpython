'''
    Use Case: Explore the Use of Properties.
'''

# Global Variable
willHappenSoon = True

# User defined classes are those that aren't builtin

class ClassX(object): # A new-style class inherits from object

    '''
        A class with instance, class and static methods
    '''
    
    # Declaring Class level Attrs - visible for class and it's instance, but not for static method!

    Arun,Allison,Mark,__private = 'Python','Python','C++','You cant access me !'


    def __init__(me,code): # Instance variable are visible only to the instance methods of a class

        me._someVariable = "Java and Python, C#"
        me.codes = code

    '''
    	Properties are not callable .. i.e. .. 
    	they have to be invoked just like a normal attribute
    	
    	Eg :: classinstance.fooGetter , not classname.fooGetter()

    '''
    @property # Declaring the property getter which will actually return the values - Won't set
    def fooGetter(they):
        return they._someVariable,they._someVariables

    @fooGetter.setter # Declaring the property setter which will actually set and return the values.
    def fooGetter(them,someThingfooGetterish):
        them._someVariables = someThingfooGetterish


classXObj = ClassX(10000)

# Using Setter to set the values
classXObj.fooGetter = "I love to Code it now! An active mind is an Angel's playground"

# Using Getter to return the values
print classXObj.fooGetter

'''
	Output ::

	('Java and Python, C#', "I love to Code it now! An active mind is an Angel's playground")

'''