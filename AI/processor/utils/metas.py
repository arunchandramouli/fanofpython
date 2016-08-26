from functools import wraps, partial
import logging


'''
    This module is limited to metaprogramming tasks, no functionality is being dealt-with.

    This acts as a support to the core engine
'''

core_engine_logger = None

'''
    A Decorator that can be applied @ class level, to convert all methods as classmethods automatically
'''
def classdecorator(klassobject):

    '''
        Convert all the methods of a class as classmethods
    '''

    for key,items in vars(klassobject).items():

    	if hasattr(items,'__call__'):
    		setattr(klassobject,key,classmethod(items))
    return klassobject

'''
    Apply an object to multiple attrs of a class
'''
def applyToMultipleAttrs(klassobject,attrList,whattoapply):

    '''
        Apply an object to multiple atttributes
    '''

    for items in attrList:
        if items in klassobject.__dict__.keys():                
            setattr(klassobject,items,whattoapply(items))
    return klassobject

'''
    A Decorator function used to execute the parts of engine
    *** This function takes another function as an input and executes the same.
'''
def execute(func = None , prefix = ''):
    '''
        A Decorator function that executes another function and logs the result
    '''
    if func is None:
        return partial(debug,prefix = prefix)
    msg = func.__name__

    core_engine_logger.info("Executing function --- %s "%msg)
    core_engine_logger.info("\n")
    core_engine_logger.info("Aim: %s "%func.__doc__)
    core_engine_logger.info("\n")

    @wraps(func)
    def wrapper(*args,**kargs):
        theResult = func(*args,**kargs)
        theResult.next()
        return theResult
    return wrapper

'''
A Co-routine function to simulate the pipeline activity inside the engine
'''

def pipeline(func):

    '''
        A Co-routine used for execution
    '''

    def theGenerator(*args,**kargs):
    	theResult = func(*args,**kargs)
    	theResult.next()
    	return theResult
    return theGenerator


'''
From the given list determine the most occuring
'''

def most_occurring(inputList):

    '''
        Identify the most occuring
    '''

    loadData = {}

    for items in inputList:
        
        if items in loadData.keys():
            loadData.__setitem__(items,loadData.__getitem__(items)+1)
        else: loadData.__setitem__(items,1)

    return loadData

'''
    From the given list determine the n.o. occurrences of an item
'''    
def find_occurrences(ipList):
    
    '''
        Find the count of occurrence
    '''
    storeCount = {}

    for items in ipList:
        storeCount.__setitem__(items,ipList.count(items))        
    return storeCount

'''
    Analyse the table and filter against the variables
    Return the count of occurrence and variables as a dict
'''
def calcprobability(getFilteredTable,supervariables):

    # An empty dict for calculation
    finalRef ,finalpos = {},[]
    
    for pos,data in enumerate(getFilteredTable):
        for keywords in supervariables._finitemsToConsider:
            finalpos.append(data.__getitem__(keywords))

        getDatainTuple = tuple(finalpos)    
        finalpos = []
        finalRef.__setitem__(getDatainTuple,1) if not getDatainTuple in finalRef.keys() else \
            finalRef.__setitem__(getDatainTuple,finalRef.__getitem__(getDatainTuple)+1)
    return finalRef

