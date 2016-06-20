
class A(object):
    _mefoo = 200
    @property
    def foo(self):
        print(' Foo - A')
        return self._mefoo

    @foo.setter
    def foo(self, val):
        print(' Foo - A - Now Setting foo value as %s '%val)
        self._mefoo = val * 2


class ATimesTwo(A):
    @A.foo.setter
    def foo(self, val):
        print(' Foo - ATimesTwo - Now Setting foo value as %s '%val)
        self._mefoo = val * 4

X = ATimesTwo()
X.foo = 100000
print(X.foo)
print('*'*25)
ATimesTwo.foo = 20000
print(ATimesTwo.foo)
