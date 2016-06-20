
'''
        Use Case:  Exploring the User defined Class, inherting a class and overriding properties

        We have a base class named "B" and a sub-class named "C", we have both getter and setter in the parent class,
        but we have only setter available in the sub-class
'''


class B(object):

    def __init__(instance):
        instance.prop = None

    @property
    def samTest(instance):
        print "Getter - class B " , instance
        return instance.prop

    @samTest.setter
    def samTest(instance,value):
        print "Setter - class B " , instance,value
        instance.prop = value


class C(B):

    @B.samTest.setter
    def samTest(instance,value):
        print "Setter - class C " , instance,value
        instance.prop = value + 50000

# An instance of class C
C_obj = C()

# Setter invoked - in class C
C_obj.samTest = 10000

# Getter invoked - in class B
print C_obj.samTest

'''
    Output from Command Line

        Setter - class C  <playground.Arun_Chandramouli.Workshop.nets2.C object at 0x124F1030> 10000
        Getter - class B  <playground.Arun_Chandramouli.Workshop.nets2.C object at 0x124F1030>
        60000
'''

print " \n\n\n"
print " * " * 50




'''
        Use Case:  Exploring the User defined Class, inherting a class and overriding properties

        We have a base class named "B" and a sub-class named "C", we have both getter and setter in the parent class,
        but we have nothing in the sub-class
'''


class B1(object):

    def __init__(instance):
        instance.prop = None

    @property
    def samTest(instance):
        print "Getter - class B " , instance
        return instance.prop

    @samTest.setter
    def samTest(instance,value):
        print "Setter - class B " , instance,value
        instance.prop = value


class C1(B1):

    pass



# An instance of class C
C_obj = C1()

# Setter invoked - in class B1
C_obj.samTest = 10000

# Getter invoked - in class B1
print C_obj.samTest

'''
    Output from Command Line

        Setter - class B  <playground.Arun_Chandramouli.Workshop.nets2.C1 object at 0x124F1C10> 10000
        Getter - class B  <playground.Arun_Chandramouli.Workshop.nets2.C1 object at 0x124F1C10>
        10000
'''
