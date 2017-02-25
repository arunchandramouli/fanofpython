'''
	
    Use Case:  Exploring the Concept of Serializing and De-Serializing in Python

    Shortly called as pickling, the needs is to store the object and later resurrect it 

        ----> Use dump for serializing the records into a file
        ----> Use dumps for serializing the records into a string
        ----> Use load for serializing the records from a file
        ----> Use loads for serializing the records from a string

    In this case we create an user defined class and add attributes to it. We then pickle the class instance
    and unpickle later
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
        Define __getstate__ and __setstate__ methods to supporting pickling the attributes of the class 

        Customize here, what to return and what not!

    '''

    
    ''' Method __getstate__ will be executed during serialization '''

    def __getstate__(instance):

        ''' 
            **** This method is called while we actually serialize the class i.i. create a pickle file / pickling ****
        '''

        ''' Return the class dictionary '''

        ''' *** instance.__class__ - Returns the Class object *** '''



        #return instance.__class__.__dict__  # Return the dict without modification



        ''' Assume we want to make some customizations while we pickle, say we want to exclude some attributes '''

        ''' Step - 1 -> Create a copy of the dictionary '''


        ''' 
            
            Please remember that here we are creating a copy of the class instance dictionary not the class dictionary,
            since we dont want to alter the original copy

                Class instance dictionary ->   instance.__dict__

                Class dictionary -> instance.__class__.__dict__

        '''

        get_instance_dictcopy = instance.__dict__.copy()

        ''' 
            Delete any wanted attributes -> Use del keyword 

            *** Once deleted here, the attributes wouldn't be available while unpickling ***

            *** 
                Like I mentioned before , this method __getstate__ gets called at the time
                we create the pickle file , hence this is the right place to customize 

            ***
        '''

        ''' Delete instance attribute location, and it wouldn't be available while unpicking/deserialization '''

        del get_instance_dictcopy['location']

        return get_instance_dictcopy



    ''' Method __setstate__ will be executed during deserialization '''

    def __setstate__(instance,value):

        ''' 
            **** This method is called while we actually deserialize the class i.i. load a pickle file / unpickling ****
        '''

        ''' Set the Value '''

        
        instance.__dict__.update(value)




'''
    Lets pickle this information to a file
'''

if __name__ =="__main__":

    

    ''' Create an instance of class Me and pickle it '''

    instanceofme = Me('Tom','Male','NewYork',20300)


    '''gets = pickle.dumps(instanceofme)

    print pickle.loads(gets).__dict__'''


    ''' We are going to pickle the class instance and later unpickle it '''

    ''' 
         Step 1 :: Serialize it - load into some place

    '''
    with open('Me.pickle','wb') as writer:
        
        '''  
            Use dump for serializing the records into a file
            Use dumps for serializing the records into a string
        '''
        
        pickle.dump(instanceofme,writer)




    ''' 
         Step 2 :: De-Serialize it - load from some place

    '''

    with open('Me.pickle','rb') as reader:

        '''  
            Use load for serializing the records from a file
            Use loads for serializing the records from a string
        '''


        ''' When we load it actually returns a class instance '''
        getdata = pickle.load(reader)

        '''
            getdata returns the instance of the class since we had actually pickled the instance not the class

            getdata.__dict__ # Returns the instance dictionary 

        '''

        '''
            
            Remember that instance attribute location is not to be seen 
            Iterate the dictionary and check for the items, if they are restored properly and do something more useful    
            
        '''

        for key,value in getdata.__dict__.items():

            print "Key = %s and Value = %s "%(key,value)



        print "\n\n"
