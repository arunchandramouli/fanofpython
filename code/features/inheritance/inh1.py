

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
        
        self.fName = first
        self.lName = last

    def state_name(self):
        '''
            Concatenate and return the first and last name
        '''
        return self.fName + " " + self.lName



'''
    Use Case: Employee Class below inherits both Person and shall have access toall of its attributes
'''

class Employee(Person):

    ''' Initialize Employee Class '''

    def __init__(self,fName,lName):

        super(Employee,self).__init__(fName,lName)


    def state_name(self):

        return "Friend"

    def get_name(self):
        '''
            Invoke the method Name in the Super Class
        '''

        ''' *** Please understand the difference carefully between the function calls below *** '''

        ''' Will call state_name function, will initially search in this class(Employee), if not found will refer to Parent Class '''
        print "Hello " + self.state_name()

        ''' Will call state_name function, will *** not initially search *** in this class(Employee), it will refer to Parent Class directly
            since we have used super()
        '''

        print "Hello " + super(Employee,self).state_name() # The method in the class Person will get invoked!


''' Create an instane of class Employee '''

class_emp = Employee("Allan","Donald")
class_emp.get_name()
