'''
	Use Case:  Exploring the User defined Class - Property

	Define Getter and Setter using Properties

	Mostly used for validations, getter and setter are used for getting and setting values

	Property Getter -
	
		@property
		def method
	
	Property Setter -

		@method.setter
		def method

	
	A Class can have any n.o. properties

    **** Here we define multiple properties ****

'''


''' Define an User defined class - Person '''

class Person(object):

    def __init__(self, name,age):
        
        ''' Initialize the name and age '''

        self.fname = name
        self.theage = age


    ''' 
    	Return the person name
    	Remember Setter needs to be invoked before the Getter
    '''
    @property
    def fname(self):

        ''' 
            Return the name  as self.myname

            *** Please note that self.myname has been used in the setter
            as self.myname = value and being returned in the getter ***

            **** If that self.myname = value hadn't been set in the setter - @fname.setter 
                then program will raise an exception - AttributeError ****

        '''

        return self.myname


    '''
    	Set the name - Raise an error in case of invalid value
    	isinstance is a built-in function used for type checking
    '''
    @fname.setter
    def fname(self, value):

        if not isinstance(value, str):
            
            raise TypeError('Expected a string')

        self.myname = value



    ''' Return the person age '''

    @property
    def theage(self):



        ''' 
            Return the age  as self._theage

            *** Please note that self.myname has been used in the setter
            as self._theage = value and being returned in the getter ***

            **** If that self._theage = value hadn't been set in the setter - @fname.setter 
                then program will raise an exception - AttributeError ****

        '''


        return self._theage



    '''
        Set the age - Raise an error in case of invalid value
        isinstance is a built-in function used for type checking
    '''
    @theage.setter
    def theage(self,value):

        if not isinstance(value,int):

            raise TypeError("Value must be an integer")

        self._theage = value



if __name__ =="__main__":

    pers = Person("Tom",10)
    pers.fname= 12 # Will raise an exception since 100 is an interger and the program expects a string
    pers.theage = '12'