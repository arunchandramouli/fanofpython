

'''
    Use Case: Inheritance and importance of __init__
'''

# If we dont init the super class we would miss the instance attrs of super class


# super is a keyword and it refers to an attribute in the parent classes, it follows the mro


'''
    Use Case: A Class that inherits many base classes - Multiple Inheritance

'''

class Person(object):

    '''
        Person Class contains 2 instance level attributes namely fName and lName and returns the same
        in the instance method - Name.

        *** Like I said in my previous articles, the instance specific attributes ae available only for it's instances
        and accessible via instance methods naturally. It can still be made available to other parts of the class but the Programmer has
        to explicitly write some code ***

    '''

    def __init__(self, first, last):
        '''
            Initialize the First and Last name
        '''
        print "__init__ from Person Class!", first, ' ',last
        self.fName = first
        self.lName = last

    def Name(self):
        '''
            Concatenate and return the first and last name
        '''
        return self.fName + " " + self.lName


class Office(object):

    def __init__(self, cabin, ecats):

        '''
            Initialize the Cabin ID and Employee Category
        '''

        print "__init__ from Office Class! ", cabin, ' ',ecats
        self.cabinID = cabin
        self.empCategory = ecats

    def Name(self):
        '''
            Concatenate and return the cabin id and employee category
        '''

        return self.cabinID + " " + self.empCategory





'''
    Use Case: Employee Class below inherits both Person and Office , but has no __init__ method defined explicitly.

    The Order is (Office,Person)

    Note: Employee Class below has no __init__ defined, in this case interpreter automatically invokes the
    base class that is first in mro ranking , i.e. in Employee(Office,Person), when an instance of
    Employee is created as --> y = Employee("Tim", "Peters"), the __init__ magic method in Office Class gets invoked
    where as not that of Person, hence the instance specific attributes of the Class Person is not visible to the
    instances of class Employee.

    The same is the behavior when class Employee will inherit 'n' number of classes.

    *** Note: But this is not the best way of doing thing in inheritance, please follow my next example. ***
'''

class Employee(Office,Person):

    def GetEmployeeData(self):
        '''
            Invoke the method Name in the Super Class
        '''
        return self.Name() # The method in the class Office will get invoked!

#y = Employee("Arun", "Chandramouli","P1-B1-W16","Programmer")

# Create an instance of class Employee and invoke the attributes

print " * " * 25, " \n"
y = Employee("Tim", "Peters")
print y.cabinID , " \n " # Instance Specific Attribute
print y.empCategory , " \n " # Instance Specific Attribute
print y.GetEmployeeData() , " \n " # Instance Method
print " * " * 25, " \n "



'''
    Use Case: Employee Class below inherits both Person and Office , and has __init__ method defined explicitly.

    The Order is (Office,Person)

    Note: Employee Class below has __init__ defined and it explicitly invokes all the base classes's constructors

'''

class Employee(Office,Person):


    def __init__(self,firstName,lastName,empCabinNumber,empCategory):
        
        Office.__init__(self,empCabinNumber,empCategory)
        Person.__init__(self,firstName,lastName)

    def GetEmployeeData(self):
        '''
            Invoke the method Name in the Super Class
        '''
        return self.Name() # The method in the class Office will get invoked!

# Create an instance of class Employee and invoke the attributes

y = Employee("Arun", "Chandramouli","P1-B1-W16","Programmer")
print " * " * 25, " \n"
print y.fName , " \n " # Instance Specific Attribute
print y.lName , " \n " # Instance Specific Attribute
print y.cabinID , " \n " # Instance Specific Attribute
print y.empCategory , " \n " # Instance Specific Attribute
print y.GetEmployeeData() , " \n " # Instance Method
print " * " * 25, " \n "
