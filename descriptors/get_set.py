__author__ = 'Home'

class A(object):

    def instance_method(self):
        return ' Instance Method '

    @classmethod
    def classmethod(cls):
        return(' Class Method ')

    @staticmethod
    def staticmethod():
        return(' Static Method ')


print(A().instance_method())
print(A.__dict__)
print(A().__dict__)
print(A.instance_method, id(A.instance_method))
print(A.classmethod , id(A.classmethod))
print(A.staticmethod , id(A.staticmethod))
print(A().instance_method , id(A().instance_method))
print(A().classmethod , id(A().classmethod))
print(A().staticmethod , id(A().staticmethod))
print(A.classmethod)
print(A.__dict__['classmethod'])
print('* ' * 200)
'''
print(A.__dict__['instance_method'])
print(A.__dict__['instance_method'].__get__(None,A))
print(A.__dict__['instance_method'].__get__(A(),A))
print(A.__dict__['instance_method'].__get__(A(),A)())
print(A.__dict__['instance_method'](A))
print('* ' * 20)
print(A.__dict__['classmethod'])
print(A.__dict__['classmethod'].__get__(None,A))
print(A.__dict__['classmethod'].__get__(A(),A))
print(A.__dict__['classmethod'].__get__(A(),A)())
'''