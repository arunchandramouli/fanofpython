

'''
    Use Case: Inheritance and importance of __init__
'''

# If we dont init the super class we would miss the instance attrs of super class


# super is a keyword and it refers to an attribute in the parent classes, it follows the mro

class Person(object):

    def __init__(self, first, last):
        self.fName = first
        self.lName = last

    def Name(self):
        return self.fName + " " + self.lName



class Employee(Person):

    def __init__(self, first, last, staffnum):
        # If we dont init the super class we would miss the instance attrs of super class - Person
        # super(Employee,self).__init__(first, last) is same as
        # Person.__init__(self,first, last)
        super(Employee,self).__init__(first, last)
        self.snum = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.snum

x = Person("Tim", "Sanders") # its not mandatory to create an instance of super class
y = Employee("Arun", "Chandramouli", "11242")

# Print the Attrs
print(x.Name())
print(y.GetEmployee())


# How to find the mro - Method order resolution!

print Employee.mro(), "\n\n" , Person.mro(), "\n\n"


'''
    Output:
       [<class 'playground.Arun_Chandramouli.inherit.Employee'>, <class 'playground.Arun_Chandramouli.inherit.Person'>, <type 'object'>]

        [<class 'playground.Arun_Chandramouli.inherit.Person'>, <type 'object'>]
'''


# List the subclasses if any


print Employee.__subclasses__() # returns an empty list since this class has no subclass


print Person.__subclasses__() # returns [<class 'playground.Arun_Chandramouli.inherit.Employee'>]
