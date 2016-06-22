
class Cacheme(object):

    '''
         The Objective is to cache the result of a function call using Non-Data descriptor
         An example is given below
    '''

    def __init__(instance,func):
        instance._func = func
        instance._name = func.__name__

    def __get__(instance,obj,type=None):
        result = instance._func(obj)
        instance.stayCached(obj,result)
        return result

    def stayCached(instance,obj,value):
        setattr(obj,instance._name,value)
