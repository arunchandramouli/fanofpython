
'''
    Use Case: Creating a property @ run-time and setting it's value via the setter

    We have a base class named "B" and a sub-class named "C", we are binding the instance method of B as a property

    Then in the sub-class we are setting it's value and invoking the getter

    Below, I have shown 2 methods of doing it and they return the same result!
'''

# Method - 1 -- Binding happens outside the Class
class B(object):

    def sample(instance):
        return getattr(instance,'xa')



B.sampleIT = property(B.sample)


class C(B):

    @B.sampleIT.setter
    def samTest(instance,value):
        print "Set ", instance,value
        setattr(instance,'xa',value)


C_obj = C()
B_obj = B()

C_obj.samTest = 'Hello World'
print C_obj.samTest



# Method - 2 -- Binding happens inside the Class


class B(object):

    def sample(instance):
        return getattr(instance,'xa')

    sampleIT = property(sample)

class C(B):

    @B.sampleIT.setter
    def samTest(instance,value):
        print "Set ", instance,value
        setattr(instance,'xa',value)


C_obj = C()
B_obj = B()

C_obj.samTest = 'Hello World'
print C_obj.samTest
