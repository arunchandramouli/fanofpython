__author__ = 'Home'
import sys
sys.setrecursionlimit(10)

class RevealAccess(object):
    """
        A data descriptor that sets and returns values
        normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val


class Myclass(object):
    '''
        Declare descriptor objects
    '''

    x = RevealAccess("C","Arun")
    y = RevealAccess("C1","Kumar Chandramouli")
    z = 'Arun Kumar Chandramouli'

    def __init__(self,ans,yes):
        self.x = ans
        self.y = yes




class C(object):
    def getx(self):         
        return self.y

    def setx(self, value):         
        self.y = value

    def delx(self):         
        del self.y

    x = property(getx, setx, delx, "I'm the 'x' property.")


x1 = C()
x1.setx("__author__ = Arun Chandramouli")
print x1.x