
'''
    Use Case: Inherit the Base Class and access it's attributes

    ***** Please be informed that if we dont use initialize the base classes , we shall not have direct access to it's 
    instance specific attributes. *****   

    Note : Instance specific attributes are those that are initialized inside the __init__ block.


    We will use super keyword to access the parent classes and check the order

    *** The following is an example of multiple-inheritance - chain ***

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
    Use Case: A Class that inherits multiple base classes - Multiple Inheritance

'''


''' Lets us define a few classes and inherit them '''


class XYZ(object):

    '''
        class XYZ is a base class and has methods named practice,tests
    '''

    def practice(self):

        print "XYZ - Practice"


    def tests(self):

        print "XYZ - Tests"



class Alpha(XYZ):

    '''
        class Alpha is a base class and has a method named practice
    '''

    def practice(self):

        print "Alpha - Practice"


class Gamma(object):

    '''
        class Gamma is a base class, and has a method named practice
    '''

    def practice(self):

        print "Gamma - Practice"
        

class Beta(Gamma,Alpha):

    '''
        class Beta is a sub-class, inherits class Alpha and has a method named practice
    '''

    def practice(self):

        print "Beta - Practice"

        

class Delta(Beta,XYZ):

    '''
        class Delta is a sub-class, inherits classes (Beta,XYZ) and has a method named practice
    '''

    def practice(self):

        print "Delta - Practice"
    


class Test(Delta):

    '''
        class Test is a sub-class , inherits class Delta and has a method named practice
    '''

    def practice(self):

        print "Test - Practice"

        ''' Invoke the practice method in the super-class '''
    
        ''' 
            This particular call will search for the method practice in all of it's parent classes and their ancestors 
            The method practice() is available in the first parent class Delta hence it will get invoked
        '''
        super(Test,self).practice()
        


        ''' Invoke the tests method in the super-class '''

        ''' 
            This particular call will search for the method practice in all of it's parent classes and their ancestors 
            The method tests() is available in a parent class XYZ hence it will get invoked
        '''
        super(Test,self).tests()
            


''' Execution Block '''

''' When we define the condition if __name__ == "__main__" , the code below it doesn't get executed on import . It runs only if run as a stand-alone file  '''
if __name__ == "__main__":


    ''' Now let us go-ahead and create an instance of class Sub_Class '''        

    instance_of_class_Test = Test()

    ''' Now let us begin to access all the methods one by one '''

    instance_of_class_Test.practice()

        
    ''' 
        Find the Order of search by calling the mro method which actually return the list that represents the Order 

        ***** Please remember that if the list is not returned , then the inheritance structure is invalid, in which case an 
              exception will be raised *****

    '''

    print Test.mro()

    ''' [<class '__main__.Test'>, <class '__main__.Delta'>, <class '__main__.Beta'>, <class '__main__.Gamma'>, <class '__main__.Alpha'>, <class '__main__.XYZ'>, <type 'object'>] '''
