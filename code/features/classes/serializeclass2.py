'''
	
    Use Case:  Exploring the Concept of Serializing and De-Serializing in Python

    Shortly called as pickling, the needs is to store the object and later resurrect it 

        ----> Use dump for serializing the records into a file
        ----> Use dumps for serializing the records into a string
        ----> Use load for serializing the records from a file
        ----> Use loads for serializing the records from a string

    In this case we create an user defined class and add attributes to it. We then pickle the entire class
    and unpickle later

    *** Here we are not using __getstate__ and __setstate__ 

'''


'''
    Module needed for pickling  
'''

import pickle

'''
    Date and time 
'''
import datetime



'''
    Lets serialize some basic data-types
'''


'''
    A Simple Class
'''

# New Style
class Me(object):

    ''' An user defined class with multiple attributes '''

    hello = 'world'
    me = 'Programmer'
    lang ='Python'
    file_handle = open('serialize.py','r')


    '''
        
        Please remember that none of the class attributes will be restored while unpickling .
        In this case hello = 'world' will not be available while deserializing
        There are ways to do it ;

        Define magic / special methods namely ; __getstate__ and __setstate__

    '''


    ''' 

        An init block to instantiate the instance attributes

    '''
    def __init__(instance,name,gender,location,income):


        instance.name = name
        instance.gender = gender
        instance.location = location
        instance.income = income        


    ''' Define a Getter - Setter to set and return the name '''

    ''' Getter - name '''
    @property
    def name(instance):

        return instance._name

    
    ''' Setter - name , value '''
    @name.setter
    def name(instance,value):

        instance._name = value


    ''' Define an instance method to return the attributes of the class '''
    
    def return_attrs(instance):

        ''' Return the instance and class attributes as a Tuple ! '''

        return instance.name,instance.gender,instance.location,instance.hello,instance.me,instance.lang

    
    ''' Define a Static method to perform some calculations '''

    @staticmethod
    def calc_bonus(income):

        '''
            Parameters
                -> income - An integer representing the income of an individual

            Return
                Percentage of bonus based on income 
        '''

        if income <= 10000 :
            return "10%"
        elif income >  10000 and income <=  20000:
            return "20%"
        elif income > 20000 and income <= 50000:
            return "50%"

        else :return "55%"






'''
    Lets pickle this information to a file
'''

if __name__ =="__main__":

    

    ''' Create an instance of class Me and pickle it '''

    instanceofme = Me('Tom','Male','NewYork',20300)


    #gets = pickle.dumps(Me)

    #print pickle.loads(gets).__dict__


    ''' We are going to pickle the class itself and later unpickle it '''

    ''' 
         Step 1 :: Serialize it - load into some place

    '''
    with open('MyClass.pickle','wb') as writer:
        
        '''  
            Use dump for serializing the records into a file
            Use dumps for serializing the records into a string
        '''
        
        pickle.dump(Me,writer)




    ''' 
         Step 2 :: De-Serialize it - load from some place

    '''

    with open('MyClass.pickle','rb') as reader:

        '''  
            Use load for serializing the records from a file
            Use loads for serializing the records from a string
        '''


        ''' When we load it actually returns a class '''
        getdata = pickle.load(reader)


        '''
            getdata returns the class since we had actually pickled the class

            getdata.__dict__ # Returns the class dictionary 

        '''

        '''
            Iterate the dictionary and check for the items, if they are restored properly and do something more useful    
        '''

        for key,value in getdata.__dict__.items():

            print "Key = %s and Value = %s "%(key,value)



        print "\n\n"
