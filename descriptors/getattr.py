import copy
import sys

sys.setrecursionlimit(10)
class Tricky(object):
    def __init__(self):
        self.special = ["foo"]
  
t1 = Tricky()
#assert t1.foo == "yes"
t2 = copy.copy(t1)
#assert t2.foo == "yes"
#print "This runs, but isn't covered."

a = [0,1,2,3,4,5,6,7,8,9,10]
print id(a)
b = copy.copy(a)
c = copy.deepcopy(a)
print b , id(b)
print c, id(c)
d = a[:]
a= tuple(range(20))

print a
print b
print c
print d

print '*-*'*15



a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = c

print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
d = range(7)
print a
print b
print c
print d
d[2]=10
print c

