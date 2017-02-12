
'''
    Use Case: Inherit the Base Class and access it's attributes

    ***** Please be informed that if we dont use initialize the base classes , we shall not have direct access to it's 
    instance specific attributes. *****   

    Note : Instance specific attributes are those that are initialized inside the __init__ block.


    We will use super keyword to access the parent classes

    ***** The following is an example of a Diamond Pattern *****

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
    Use Case: A Class that inherits many base classes - Multiple Inheritance

'''


''' Lets us define a few classes and inherit them '''


class Alpha(object):

    '''
        class Alpha is a base class and has a method named practice
    '''

    def practice(self):

        print "Alpha - Practice"


class Beta(Alpha):

    '''
        class Beta is a subclass, it inherits class Alpha and has a method named practice
    '''

    def practice(self):

        print "Beta - Practice"
        super(Beta,self).practice()





class Gamma(Alpha):

    '''
        class Gamma is a subclass, it inherits class Alpha and has a method named practice
    '''

    def practice(self):

        print "Gamma - Practice"
        super(Gamma,self).practice()




class Delta(Beta,Gamma):

    '''
        class Delta is a subclass, it inherits class Alpha and has a method named practice
    '''

    def practice(self):

        print "Delta - Practice"
        super(Delta,self).practice()





''' Execution Block '''

''' When we define the condition if __name__ == "__main__" , the code below it doesn't get executed on import . It runs only if run as a stand-alone file  '''
if __name__ == "__main__":


    ''' Now let us go-ahead and create an instance of class Sub_Class '''        

    instance_of_class_delta = Delta()

    ''' Now let us begin to access all the methods one by one '''

    instance_of_class_delta.practice()