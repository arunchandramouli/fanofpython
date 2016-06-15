
'''
    Use Case: Show how python generates and executes the bytecode
'''
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def whatisIt(self):
        return 'Hello %s , any problem ?'%self.first_name + ' ' + self.last_name

    @classmethod
    def whatisCIt(self):
        return 'Hello %s , any problem ?'%self.first_name + ' ' + self.last_name

    @staticmethod
    def whatSIt():
        return 'Hello %s , any problems ?'


    @property
    def full_name(self):
        return " Say hello to " + self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        del self.first_name
        del self.last_name



import dis

print dis.dis(Person)



'''
    Output:
        Disassembly of __init__:
 14           0 LOAD_FAST                1 (first_name)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (first_name)

 15           9 LOAD_FAST                2 (last_name)
             12 LOAD_FAST                0 (self)
             15 STORE_ATTR               1 (last_name)
             18 LOAD_CONST               0 (None)
             21 RETURN_VALUE

Disassembly of whatisIt:
 18           0 LOAD_CONST               1 ('Hello %s , any problem ?')
              3 LOAD_FAST                0 (self)
              6 LOAD_ATTR                0 (first_name)
              9 BINARY_MODULO
             10 LOAD_CONST               2 (' ')
             13 BINARY_ADD
             14 LOAD_FAST                0 (self)
             17 LOAD_ATTR                1 (last_name)
             20 BINARY_ADD
             21 RETURN_VALUE

None
'''

print dis.dis(Person.whatisCIt)

'''
    Output:
         22   0 LOAD_CONST               1 ('Hello %s , any problem ?')
              3 LOAD_FAST                0 (self)
              6 LOAD_ATTR                0 (first_name)
              9 BINARY_MODULO
             10 LOAD_CONST               2 (' ')
             13 BINARY_ADD
             14 LOAD_FAST                0 (self)
             17 LOAD_ATTR                1 (last_name)
             20 BINARY_ADD
             21 RETURN_VALUE
None

'''


persons = Person("Tim","Peters")

print persons.full_name

persons.full_name = "Arun Chandramouli"

print persons.full_name

del persons.full_name
