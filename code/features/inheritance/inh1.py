
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
    Use Case: A Class that inherits only one base class - Single Inheritance

'''

class Person(object):

    '''
        Person Class contains 2 instance level attributes namely fName and lName and returns the same
        in the instance method - state_name.

        ***** The instance specific attributes ae available only for it's instances
        and accessible via instance methods naturally. It can still be made available to other parts of the class but the Programmer has
        to explicitly write some code ****

    '''

    def __init__(self, first, last):

        '''
            Initialize the First and Last name

            * * * These are instance specific attributes * * *

        '''
        
        self.fName = first
        self.lName = last

    def state_name(self):
        '''
            Concatenate and return the first and last name
        '''
        return self.fName + " " + self.lName



'''
    Use Case: Employee Class below inherits Person and shall have access to all of its attributes
'''

class Employee(Person):

    ''' Initialize Employee Class '''

    def __init__(self,fName,lName):

        ''' 
            When we call super, it will refer to the parent class and will refer to call the required attributes..

            In this case it will call the __init__ method of the super class (Person), and initialize it with

            First name and Last name . . .

            Since we are initializing the __init__ of the super Class Person, we shall have access to it's
            instance specific variables such as fName and lName , those present in the __init__ block of Class Person...

            We can thus access them as self.fName, self.lName ....

            * * * These are instance specific attributes * * *

        '''

        super(Employee,self).__init__(fName,lName)


    def state_name(self):

        return "Friend - Employee Class"

    def get_name(self):

        '''
            Invoke the method Name in the Super Class
        '''

        ''' ***** Please understand the difference carefully between the method calls below ***** '''

        ''' Will call state_name method, will initially search in this class(Employee), if not found will refer to Parent Class '''
        
        print "Hello " + self.state_name()

        ''' 
            Will call state_name method, will ***** not initially search ***** in this class(Employee), 
            it will refer to Parent Class directly since we have used super()
        '''

        print "Hello " + super(Employee,self).state_name() # The method in the class Person will get invoked!



''' Execution Block '''

''' When we define the condition if __name__ == "__main__" , the code below it doesn't get executed on import . It runs only if run as a stand-alone file  '''
if __name__ == "__main__":

    ''' Create an instance of class Employee '''

    class_emp = Employee("Allan","Donald")
    class_emp.get_name()
