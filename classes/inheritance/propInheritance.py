'''
    Use Case: Explore the Use of Properties.

    Inherit and use the Properties
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


print 'From ClassX ', "\n\n"
# Using Setter to set the values - This value will not reflect for the Sub-Classes!
classXObj.fooGetter = "I love to Code it now! An active mind is an Angel's playground"

print classXObj.fooGetter


class ClassY(ClassX):
	pass




# Accessing Property via classY
classYObj = ClassY(100)

# Using Setter to set the values - This value will not reflect for the Sub-Classes!
classYObj.fooGetter = "I love to Code it now! An active mind is an Angel's playground!"

print 'From ClassY ', "\n\n"
print classYObj.fooGetter


class ClassZ(ClassY,ClassX):

	@property
	def fooGetter(instance):

		return instance._someVariable , "My Angel's with me!"

print 'From ClassZ ', "\n\n"
classZobj = ClassZ(1000)
print classZobj.fooGetter