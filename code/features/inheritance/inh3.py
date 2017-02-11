'''
    Use Case: Inherit the Base Class and access it's attributes

    In this example, we would not use __init__ to initialize the base classes, but we shall
    be accessing the attributes of the parent class using an instance.


    ***** Please be informed that if we dont use initialize the base classes , we shall not have direct access to it's 
    instance specific attributes. *****
   

    Note : Instance specific attributes are those that are initialized inside the __init__ block.


'''



'''

    About mro - Method Resolution Order 

    A short note an how mro works in realtime

    Say we have a class - class Xyx(A,B,C,X,D,F,G)

    We have a class Xyx that has 7 parent classes namely (A,B,C,X,D,F,G)

    When we create an instance and access any method this is what happens;

    It first searches in the class Xyx to confirm if the method is present there, if found return and break

    Else it begins to search the parent classes(super classes)

    It will start as per the ranking, here we have the ranking as (A,B,C,X,D,F,G)

    It will first search for the method in class A, if found return and break, else it now checks if class A
    has got any Parent Classes, if yes, it will search all of it's parent classes, if found anywhere return and break .

    Else it goes to class B, it will search for the method in class B , if found return and break, else it now checks if class B
    has got any Parent Classes, if yes, it will search all of it's parent classes, if found anywhere return and break .

    The same procedure is done for all of the Parent Classes until the method is found.

    In any case if the method is not found any where it raises an AttributeError , meaning that method name is not to be
    found anywhere in the hierarchy.
     

'''


'''
    Use Case: A Class that inherits multiple base classes- Multiple Inheritance

'''


''' Define Class Alpha and it's methods and attributes '''

class Alpha(object):

    '''
        Class Alpha is a base class and it shall be inherited by its subclass!

        It has 3 methods namely method1, methodx, method2
    '''


    '''
        Alpha Class - method1
    '''

    def method1(self):

        return "Method-1 from Class Alpha"


    '''
        Alpha Class - method2
    '''

    def method2(self):

        return "Method-2 from Class Alpha"


    '''
        Alpha Class - methodx
    '''

    def methodx(self):

        return "Method-X from Class Alpha"



''' Define Class Beta and it's methods and attributes '''

class Beta(object):

    '''
        Class Beta is a base class and it shall be inherited by its subclass!

        It has 4 methods namely method1, methodx, method2, methodb
    '''


    '''
        Beta Class - methodb1
    '''

    def methodb1(self):

        return "Method-b1 from Class Beta"


    '''
        Beta Class - methodb2
    '''

    def methodb2(self):

        return "Method-b2 from Class Beta"


    '''
        Beta Class - methodbx
    '''

    def methodbx(self):

        return "Method-bX from Class Beta"



    '''
        Beta Class - methodb
    '''

    def methodd(self):

        return "Method-d from Class Beta"






''' Define Class Gamma and it's methods and attributes '''

class Gamma(object):

    '''
        Class Gamma is a base class and it shall be inherited by its subclass!

        It has 4 methods namely method1, method3, methodq, methodw
    '''


    '''
        Gamma Class - method1
    '''

    def method1(self):

        return "Method-1 from Class Gamma"


    '''
        Gamma Class - method3
    '''

    def method3(self):

        return "Method-3 from Class Gamma"


    '''
        Gamma Class - methodq
    '''

    def methodq(self):

        return "Method-Q from Class Gamma"

    '''
        Gamma Class - methodw
    '''

    def methodw(self):

        return "Method-W from Class Gamma"



''' Define a Sub-class by name Sub_Class and let it inherit Alpha, Beta, Gamma '''

class Sub_Class(Alpha,Beta,Gamma):


    '''
        Class Sub_Class inherits 3 parent classes namely Alpha,Beta,Gamma and thus has access to all of its methods and attributes.

        It has also got a method on it's own , say method_sub which returns "method_sub from class Sub_Class"

        Now When we create an instance of class Sub_Class , and access the methods of the Parents, it goes in an order

        and searches all the parent classes.
        
        Let's consider an example
    
        ******  Say we want to access methodw *****


        Now, Search begins at Class Sub_Class (if the method is found, it breaks here) if not then it goes to 

        Alpha and all of it's parents (if the method is found, it breaks here) ... 

        if still not then it goes to Beta and all of it's parents (if the method is found, it breaks here).. and if still not found it goes 

        to Gamma and all of it's parents (if the method is found, it breaks here).

        This concept is known as mro(Method Resolution Order)

        In any case if the method is not found in it's own class or any of it's parent's it raises an AttributeError

    '''


    ''' Define method method_sub '''

    def method_sub(self):

        return "Method method_sub from Class Sub_Class"



''' Execution Block '''

''' When we define the condition if __name__ == "__main__" , the code below it doesn't get executed on import . It runs only if run as a stand-alone file  '''
if __name__ == "__main__":


    ''' Now let us go-ahead and create an instance of class Sub_Class '''        

    instance_of_class_sub_class = Sub_Class()

    ''' Now let us begin to access all the methods one by one '''

    print "-"*50,"\n\n"
    print instance_of_class_sub_class.method1(),"\n\n"
    print instance_of_class_sub_class.method2(),"\n\n"
    print instance_of_class_sub_class.method3(),"\n\n"
    print instance_of_class_sub_class.methodx(),"\n\n"
    print instance_of_class_sub_class.methodw(),"\n\n"
    print instance_of_class_sub_class.methodq(),"\n\n"
    print instance_of_class_sub_class.methodd(),"\n\n"
    print instance_of_class_sub_class.methodb1(),"\n\n"
    print instance_of_class_sub_class.methodb2(),"\n\n"
    print instance_of_class_sub_class.methodbx(),"\n\n"
    print instance_of_class_sub_class.method_sub(),"\n\n"
    print "-"*50,"\n\n"