
'''
    Use Case: Invoke the rich comparison operators!
'''
class Klass(object):

    def __init__(self, obj, *args):
        self.obj = obj

    def __lt__(self, other):
        print " __lt__ ",self, other
        return (self.obj, other.obj) < 0

    def __gt__(self, other):
        print " __gt__ ",self, other
        return (self.obj, other.obj) > 0

    def __eq__(self, other):
        print " __eq__ ",self, other
        return (self.obj, other.obj) == 0

    def __le__(self, other):
        print " __le__ ",self, other
        return (self.obj, other.obj) <= 0

    def __ge__(self, other):
        print " __ge__ ",self, other
        return (self.obj, other.obj) >= 0

    def __ne__(self, other):
        print " __ne__ ",self, other
        return (self.obj, other.obj) != 0

# Creating instances
klass1 = Klass(100)
klass2 = Klass(1000)

# Check for operator "<", this will invoke __lt__
print klass1 < klass2 # returns  __lt__  <playground.Arun_Chandramouli.sorted_2.Klass object at 0x1154A330> <playground.Arun_Chandramouli.sorted_2.Klass object at 0x1154A350>, False
