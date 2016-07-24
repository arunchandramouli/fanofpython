'''
								       Learning based query handler

# ****************************************************************************************************************** #

Implementation of Machine learning algorithm to process some input from an User in a text format

The Following Pattern follows a Structured Supervised approach with labelled data and it's instance knowledge based.

Steps:

        --> Read and store machine feeds (training data)
    	--> Categorize training data and save for further processing
    	--> Create a model from data and response (Knowledge feed to the machine)
    	--> Get the User query and process it - say split and store it in a container
    	--> Get the query(new input) from the User and classify it (say True/False/Valid/Invalid/0/1 ... etc...)
    	--> Process the query against the model and draft a prediction
    	--> Write the result to an output file. Also log it in the UI.


Note :: In-depth information is classified in the readme file.
https://github.com/arunchandramouli/fanofpython/blob/master/AI/processor/readme.txt

# ****************************************************************************************************************** #

'''
import os,sys
sys.path.append("..\utils")
import metas as theMetas

'''
    The Machine responsible for performing tasks listed in steps above
'''
class Core_Engine(object):

    '''
        Send the file and input query for processing
    '''
    def loadFile(klass,fileName,ipQuery,targetfunctopush):

       if os.path.exists(fileName):
		          targetfunctopush.send((open(fileName,"r"),ipQuery))
       else:
            raise Exception('File path is invalid %s '%fileName)

    '''
     The Function that adds value to the container
    '''
    @theMetas.pipeline
    def addtoContainer(klass,targetfunctopush):

      while True:

        containerObject = yield
        fileObject,inputQuery = containerObject

        with fileObject as reader:
          for lines in (reader.readlines()):
            for data in lines.split(","):
              print(str(data).lower().strip())
            print "\n\n"
        #targetfunctopush.send(adds)

    '''
        Invoke the pipeline
    '''
    def execute(klass,fileName,ipQuery):
        print fileName,ipQuery
        getattr(klass,'loadFile').__call__(fileName,ipQuery,getattr(klass,'addtoContainer').__call__(None))
