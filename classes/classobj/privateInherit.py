'''
    Use Case:  Exploring the User defined Class, checking the availability of attributes of methods in a class

    Exploring the Private Attributes on inheritance
'''

# User defined classes are those that aren't builtin

class UserDefined(object): # A new-style class inherits from object


    # Declaring Class level Attrs - visible for class and it's instance

    Arun,Allison,Mark,__codex = 'Python','Python','C++','Beautiful Classics'

    def __init__(me,attrs):

        '''
            The Constructor to initialize the attributes
        '''

        me._foo = " Hello Java Guys!"
        me._java = "Coffee Mug!"
        

    def instanceMethod(this):


        return 'Hello - I am an Instance Method -- > class name - %s '%(this._foo)


    def __privateFunction(instance):

    	return " Private Function inside the class"



class UserDefined2(object):

        _codex = 'Beautiful World of Classics!!'

        def __init__(me,attrs):

            '''
                The Constructor to initialize the attributes
            '''

            me._foo = " Hello Java Guys!"
            me._java = "Coffee Mug!"            
            me.attrs = attrs        


        def defAttrs(me):

            return me.attrs
  

class Subs(UserDefined,UserDefined2): 
    
    def __init__(me,values):

        super(Subs,me).__init__(values)
        UserDefined2.__init__(me,values)


# Create an instance of Subs

x = Subs(1000)
print x.instanceMethod()
print x.defAttrs()
print x._codex
print x.__codex # Impossible to access the private attrs

'''
 Output ::

       Traceback (most recent call last):
              File "privateInherit.py", line 72, in <module>
                print x.__codex # Impossible to access the private attrs
            AttributeError: 'Subs' object has no attribute '__codex'
'''