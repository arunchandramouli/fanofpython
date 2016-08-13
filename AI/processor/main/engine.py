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
        --> Rank the responses of user query against the model
    	--> Process the query against the model and draft a prediction based on the rankings
    	<!-- --> Write the result to an output file. Also log it in the UI. Possibly also pickle it(##TODO) -->

***** We need to feed enough inputs to the machine in step-1 to ensure that the User query gets the best response and rank. *****

Note :: In-depth information is classified in the readme file.
https://github.com/arunchandramouli/fanofpython/blob/master/AI/processor/readme.txt

# ****************************************************************************************************************** #

'''

import os,sys,re
# Append the Path!
sys.path.append("..\utils")
import metas as theMetas


'''
    The Machine responsible for performing tasks listed in steps above
'''
class Core_Engine(object):

    '''
        Declare class-level variables
    '''

    getInputPattern, filteronPrediction = {},{}

    '''
        Send the file and input query for processing
    '''
    def loadFile(klass,fileName,ipQuery,targetfunctopush):

       if os.path.exists(fileName):
		          targetfunctopush.send((open(fileName,"r"),ipQuery))
       else:
            raise Exception('File path is invalid %s '%fileName)


    '''
        The Function that adds value to the container  - the training data to the machine
    '''
    @theMetas.pipeline
    def catMachineFeed(klass,targetfunctopush):

      while True:

        containerObject = yield
        fileObject,inputQuery = containerObject

        with fileObject as reader:
          for lines in (reader.readlines()):
            # Form a model - Add text against it's pattern
 			getIpLine = lines.split(",")[1].lower()
			theTable = {"Data" : getIpLine,"Pattern":re.compile(getIpLine)}

			klass.getInputPattern.__setitem__(getIpLine,theTable)

		# Send for further processing - Categorize training data and save for further processing     	
        targetfunctopush.send((klass.getInputPattern,inputQuery))

    '''
	    Categorize training data and save for further processing
    '''
    @theMetas.pipeline
    def createModel(klass,targetfunctopush):

      while True:

        modelObject,inputQuery = yield
        for k,v in modelObject.items():
		
			# Assign a default rating of 0
			v.update({"Rating":0})

        # Send for further processing - Categorize training data and save for further processing
        targetfunctopush.send((modelObject,inputQuery))

    '''
        Analyze and classify the new input
    '''
    @theMetas.pipeline
    def analyzeUserInput(klass,targetfunctopush):

	  while True:

		modelObject,inputQuery = yield
		# Split the input query and get the tokens
		getTokensIpQuery = inputQuery.split(' ')
		getPatternCompiled = [re.compile(text) for text in getTokensIpQuery]

        # Run the patterns against the model
		for allModelkeys,allModelVals in modelObject.items():
			scoreRating = 0

			for allPatterns in getPatternCompiled:								
				result = allPatterns.findall(allModelVals.__getitem__("Data"),re.IGNORECASE)

				if result :
					scoreRating += 1					
					allModelVals.__setitem__("Rating",scoreRating)

		targetfunctopush.send(modelObject)

    '''
        Summary of User data against the Machine Feed
    '''
    @theMetas.pipeline
    def summary(klass,targetfunctopush):

        while True:

            modelObject = yield
            for allModelkeys,allModelVals in modelObject.items():
                if  allModelVals.__getitem__("Rating") > 0:
					klass.filteronPrediction.__setitem__(allModelVals.__getitem__("Data"),allModelVals.__getitem__("Rating"))

            print klass.filteronPrediction
            targetfunctopush.send(klass.filteronPrediction)

    '''
        Calculate the Prediction
    '''

    @theMetas.pipeline
    def predictandRoute(klass):


        while True:

            prediction = yield

            '''
                From this given data, we can arrive at a solution that the user query somewhat relates to the data filtered
                and obtained at this stage , and this can be further taken and auto-complete be given in the UI
            '''

    '''
        Invoke the pipeline
    '''
    def execute(klass,fileName,ipQuery):
        getattr(klass,'loadFile').__call__(fileName,ipQuery,getattr(klass,
            'catMachineFeed').__call__(getattr(klass,'createModel').__call__(getattr(klass,
                'analyzeUserInput').__call__(getattr(klass,'summary').__call__(getattr(klass,'predictandRoute')())))))
