__author__ = 'Home'

'''
 Example of Decorator with arguments
 
'''

from functools import wraps, partial
import logging

def dec_args(prefix=''):
    def debug(func):
        logme = logging.getLogger(func.__module__)
        msg = func.__name__
        @wraps(func)
        def wrapper(*args,**kargs):
            print(prefix + msg)
            return func(*args,**kargs)
        return wrapper
    return debug


def debug(func = None , prefix = ''):
        if func is None:
            return partial(debug,prefix = prefix)
        msg = func.__name__
        @wraps(func)
        def wrapper(*args,**kargs):
            print(prefix + msg)
            return func(*args,**kargs)
        return wrapper


#@dec_args(prefix=' Awe ')
@debug(prefix='AWE')
def say_hello():
    a = 100
    print(' Hello ' , a)

print say_hello.__class__
say_hello.__call__()
print(say_hello.__dict__)
print(say_hello.func_name)
print(say_hello.func_code)
print(say_hello.func_dict)