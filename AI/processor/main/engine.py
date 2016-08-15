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

import os,sys,re, operator
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

		'''
			From the command line args, read the csv path, open it and send it along with input query for further processing
			Raise an exception if the path is found to be invalid
		'''

		if os.path.exists(fileName):
		          targetfunctopush.send((open(fileName,"r"),ipQuery))
		else:
			raise Exception('File path is invalid %s '%fileName)


    
    '''
        The Function that adds value to the container  - the training data to the machine
    '''
    @theMetas.pipeline
    def catMachineFeed(klass,targetfunctopush):

      '''
      		Read each line i.e. the training data and 
      		store it in a dictionary for quicker processing
      '''

      while True:

        containerObject = yield
        fileObject,inputQuery = containerObject

        with fileObject as reader:
          for tablelineID,lines in enumerate(reader.readlines()):
            
            # Add text against it's pattern
 			getIpLine , getCat = lines.split(",")[1].lower(),lines.split(",")[2].lower()
 			
 			# :: TODO :: Don't add input line but it's pattern
			theTable = {"Data" : getIpLine,"Pattern":re.compile(getIpLine),"Rating":0,"Category":getCat}

			klass.getInputPattern.__setitem__(tablelineID,theTable)

		# Send for further processing - Categorize training data and save for further processing
        targetfunctopush.send((klass.getInputPattern,inputQuery))

	
    '''
        Analyze and classify the new input
    '''
    @theMetas.pipeline
    def analyzeUserInput(klass,targetfunctopush):

	  '''
	  		Compile and run the user input against the patterns
	  		for every match increment the rating by 1
	  '''	

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
        Filter the Rating
    '''
    @theMetas.pipeline
    def summary(klass,targetfunctopush):

    	'''
    		Ratings > 1 goto next level for processing

    		:: TODO :: If rating <2, the user query will be added to the database and assigned a category
    	'''

        while True:

            modelObject = yield
            
            targetfunctopush.send(filter(lambda d:d.__getitem__("Rating") > 1,modelObject.values()))


    '''
        Calculate the Prediction
    '''
    @theMetas.pipeline
    def predictandRoute(klass):

    	'''
    		From the filtered value, predict the nearest category
    	'''

        while True:

            prediction = yield

            #print sorted(prediction,key = operator.itemgetter('Rating'))

            getfinState = max(prediction,key = operator.itemgetter('Rating'))

            # Identify the Category 
            print getfinState.__getitem__("Category")

            '''
                From this given data, we can arrive at a solution that the user query somewhat relates to the data filtered
                and obtained at this stage , and this can be further taken and auto-complete be given in the UI
            '''

    '''
        Invoke the pipeline
    '''
    def execute(klass,fileName,ipQuery):
        getattr(klass,'loadFile').__call__(fileName,ipQuery,getattr(klass,
            'catMachineFeed').__call__(getattr(klass,'analyzeUserInput').__call__(getattr(klass,'summary').__call__(getattr(klass,'predictandRoute')()))))
