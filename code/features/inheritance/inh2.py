'''
    Use Case: Inherit the Base Class and access it's attributes


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

''' Define Class Person and it's methods and attributes '''

class Person(object):

    '''
        Person Class contains 2 instance level attributes namely fName and lName and returns the same
        in the instance method - state_details.

        ***** The instance specific attributes ae available only for it's instances
        and accessible via instance methods naturally. It can still be made available to other parts of the class but the Programmer has
        to explicitly write some code ****


        Class Person is the base class, it shall be inherited by it's subclasses

    '''

    def __init__(self, first, last):

        '''
            Initialize the First and Last name

            * * * These are instance specific attributes * * *
        '''
        
        self.fName = first
        self.lName = last

    
    def state_details(self):
    
        '''
            Concatenate and return the first and last name
        '''
        return self.fName + " " + self.lName


'''
    Office Class contains 2 instance level attributes namely cabinID and empCategory and returns the same
    in the instance method - state_details.

    ***** The instance specific attributes are available only for it's instances
    and accessible via instance methods naturally. It can still be made available to other parts of the class but the Programmer has
    to explicitly write some code ****


    Class Person is the base class, it shall be inherited by it's subclasses

'''


''' Define Class Office and it's methods and attributes '''

class Office(object):

    def __init__(self, cabin, ecats):

        '''
            Initialize the Cabin ID and Employee Category

            * * * These are instance specific attributes * * *
        '''

        self.cabinID = cabin
        self.empCategory = ecats


    def state_details(self):
        
        '''
            Return the cabin id and employee category
        '''

        return (self.cabinID,self.empCategory)



'''
    Use Case: Employee Class below inherits Person and shall have access to all of its attributes
'''

''' Define Class Employee and it's methods and attributes '''

class Employee(Person,Office):

    ''' Initialize Employee Class '''

    def __init__(self,fName,lName):

        ''' 
            When we call super, it will refer to the parent class and will refer to call the required attributes..

            In this case it will call the __init__ method of the super class (Person), and initialize it with

            First name and Last name . . .

            Since we are initializing the __init__ of the super Class Person, we shall have access to it's
            instance specific variables such as fName and lName , those present in the __init__ block of Class Person...

            We can thus access them as self.fName, self.lName ....

        '''

        super(Employee,self).__init__(fName,lName)


    def state_details(self):

        return "Friend - Employee Class"


    def get_details(self):

        '''
            Invoke the method Name in the Super Class
        '''

        ''' ***** Please understand the difference carefully between the method calls below ***** '''

        ''' 

            Will call state_details method, will initially search in this class(Employee), if not found will refer to Parent Class .

            Since we have state_details method in the Employee Class , only that will get executed .

        '''
        
        print "Hello " + self.state_details()


        
        ''' 
            Will call state_details method, will ***** not initially search ***** in this class(Employee), 
            it will refer to Parent Class directly since we have used super()

            We have 2 super(parent) classes and both of it define state_details method, but the first in our order is

            Person, which is defined Employee(Person,Office) which means that state_details of Person Class will get called .

            It follows the order known as mro(Method Resolution Order). It will search all parents and their ancestors in order

            until the required method is found at some point .

            If it's not there with any of the Parents , then an exception shall be raised (AttributeError).

        '''

        print "Hello " + super(Employee,self).state_details() # The method in the class Person will get invoked!




''' Create an instance of class Employee '''

class_emp = Employee("Allan","Donald")
class_emp.get_details()


''' Print all the parent classes of Employee (Also called as base classes) '''


print "-"*50,'\n'

print "Base Classes of Employee is/ are - ",(Employee.__bases__)
print "-"*50,'\n'