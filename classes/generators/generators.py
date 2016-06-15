
'''
    Use Case: Use a generator object to yield values, raise StopIteration exception
'''

def getDatafromGen(*load):

    for iterables in load:
        yield iterables


print getDatafromGen # returns <function getDatafromGen at 0x0EBC5DB0>
print getDatafromGen(range(10),range(100),range(1000,10000,1000)) # <generator object getDatafromGen at 0x111A4710>

# A Generator is an object that actually yields values, it consumes little or no memory

# How do you get values from a generator??

'''
 This block of code results in infinite overflow!

while True:

    getDatafromGen(range(10),range(100),range(1000,10000,1000)).next()

'''

'''
 This block of code results in infinite overflow!

while True:

    x = getDatafromGen(range(10),range(100),range(1000,10000,1000)).__iter__()
    print x.next()

'''


# Set the Iter

x = getDatafromGen(range(10),range(100),range(1000,10000,1000)).__iter__()

'''
 This block of code results in StopIteration exception!

while True:

    print x.next()
'''



'''
    A good way of writing is to handle exceptions wisely!
'''

try:
    while True:

        print x.next()

except StopIteration:

    print ' Loop Execution completed successfully '


print " * " * 50

'''
A key point to note with generators is that the values are exhausted once an iteration is over,
that means if you execute the same block of code more than once it resuls in a StopIteration exception, reason is
you will be iterating over nothing!
'''

try:
    while True:

        print x.next()

except StopIteration as N:
    print ' Loop Execution completed successfully '
