
from functools import wraps, partial
import logging


'''
    This module is limited to metaprogramming tasks, no functionality is being dealt-with.

    This acts as a support to the core engine
'''

'''
    A Decorator that can be applied @ class level, to convert all methods as classmethods automatically
'''
def classdecorator(klassobject):

	for key,items in vars(klassobject).items():

		if hasattr(items,'__call__'):
			setattr(klassobject,key,classmethod(items))
	return klassobject

'''
    Apply an object to multiple attrs of a class
'''
def applyToMultipleAttrs(klassobject,attrList,whattoapply):
    	for items in attrList:
            if items in klassobject.__dict__.keys():                
                setattr(klassobject,items,whattoapply(items))
        return klassobject

'''
    A Decorator function used to execute the parts of engine
    *** This function takes another function as an input and executes the same.
'''

def debug(func = None , prefix = ''):
        if func is None:
            return partial(debug,prefix = prefix)
        msg = func.__name__

        core_engine_logger.info("Executing function --- %s "%msg)
        core_engine_logger.info("/n")
        core_engine_logger.info("Aim: "%func.__doc__)
        core_engine_logger.info("/n")

        if not prefix is None:
            core_engine_logger.info("Category %s"%prefix)
            core_engine_logger.info("/n")

        @wraps(func)
        def wrapper(*args,**kargs):
            return func(*args,**kargs)
        return wrapper

'''
    A Co-routine function to simulate the pipeline activity inside the engine
'''

def pipeline(func):
	def theGenerator(*args,**kargs):
		theResult = func(*args,**kargs)
		theResult.next()
		return theResult
	return theGenerator
