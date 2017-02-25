'''
	
    Use Case:  Exploring the Concept of Serializing and De-Serializing in Python

    Shortly called as pickling, the needs is to store the object and later resurrect it 

        ----> Use dump for serializing the records into a file
        ----> Use dumps for serializing the records into a string
        ----> Use load for serializing the records from a file
        ----> Use loads for serializing the records from a string

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


# Define a Dictionary

pickleme = {}

'''
    To this dictionary let's add several data types such as list, tuple, dictionary,int,str,float,boolean etc..
'''

pickleme['name'] = 'Einstein'
pickleme['type'] = True
pickleme['number']= 10000
pickleme[100] = 10000
pickleme['more'] = [100.12,700.90,800.22,900.20,300.6,1000,789,679,27,"21N"]
pickleme['data'] = [100,200,300,400,500,"Python","Javascript","C","Java",True,False,None]
pickleme['info'] = (100,200,300,400,500,"Python","Javascript","C","Java",True,False,None)
pickleme['currtime'] = datetime.datetime.now()

'''
    A Simple Class
'''

# New Style
class Me(object):

    hello = 'world'

    def simple_func(self):

        return "I belong to class Me"
    

# Old Style
class Python :pass

''' 
    
    Please remember that none of the class attributes will be restored while unpickling .
    In this case hello = 'world' will not be available while deserializing
    There are ways to do it but...

'''

pickleme['newstyleclass'] = Me
pickleme['oldstyleclass'] = Python



'''
    Lets pickle this information to a file
'''

if __name__ =="__main__":

    
    ''' 
         Step 1 :: Serialize it - load into some place

    '''
    with open('pickleme.pickle','wb') as writer:
        
        '''  
            Use dump for serializing the records into a file
            Use dumps for serializing the records into a string
        '''
        
        pickle.dump(pickleme,writer)


    ''' 
         Step 2 :: De-Serialize it - load from some place

    '''

    with open('pickleme.pickle','rb') as reader:

        '''  
            Use load for serializing the records from a file
            Use loads for serializing the records from a string
        '''


        ''' 

            When we load it actually returns a dictionary, hence we can  iterate on it 

            Iterate the dictionary and check for the items, if they are restored properly and do something more useful    

        '''

        getdata = pickle.load(reader)

        for key,val in getdata.items():

            print key,val,'\n'



        ''' Now lets pick the class object Me from the returned dict and analyse more '''
        myclass = getdata['newstyleclass']
        print myclass.__dict__

