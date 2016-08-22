from __future__ import division


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
        Load the input file and query and send to the target
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
      		Read each line i.e. the training data and store it, push to the target
      '''

      while True:

        containerObject = yield
        fileObject,inputQuery = containerObject

        with fileObject as reader:
          for tablelineID,lines in enumerate(reader.readlines()):
            
            # Add text against it's pattern
            if lines.strip():

                getIpLine , getCat , getSystemName, getPlatformName = lines.split(",")[1].lower(),lines.split(",")[2].lower(),\
                                     lines.split(",")[3].lower() ,lines.split(",")[4].lower()

            	# :: TODO :: Don't add input line but it's pattern
                theTable = {"Data" : getIpLine,"Pattern":re.compile(getIpLine),"Rating":0,"Category":getCat,
                            "System":getSystemName,"Platform":getPlatformName}

                klass.getInputPattern.__setitem__(tablelineID,theTable)

		# Send for further processing - Categorize training data and save for further processing
        targetfunctopush.send((klass.getInputPattern,inputQuery))


    '''
        Analyze and classify the new input
    '''
    @theMetas.pipeline
    def analyzeUserInput(klass,targetfunctopush):

	  '''
	  		Compile and run the user input against the patterns, for every match increment the rating by 1
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
    		Ratings > 0 goto next level for processing    		
    	'''

        # :: TODO :: If rating <2, the user query will be added to the database and assigned a category

        while True:

            modelObject = yield
            
            targetfunctopush.send(filter(lambda d:d.__getitem__("Rating") > 0,modelObject.values()))


    '''
         Calculate the Prediction
    '''
    @theMetas.pipeline
    def predictandRoute(klass,targetfunctopush):

        '''
             From the filtered value, predict the nearest category
        '''

        while True:

            prediction = yield


            # If there more than category short-listed, we need to fiter the best solution possible!

            #print sorted(prediction,key = operator.itemgetter('Rating'))

            # Find the maximum rating!
            getfinState = max(prediction,key = operator.itemgetter('Rating'))

            # Check if there are other solutions with max rating and get the categories!

            getFinCat = [items.__getitem__("Category").__str__().strip() for items in  prediction if items.__getitem__("Rating") == getfinState.__getitem__("Rating")]

            getFinlist = [(items.__getitem__("Category").__str__().strip(),items.__getitem__("System").__str__().strip(),items.__getitem__("Platform").__str__().strip() )
                        for items in  prediction if items.__getitem__("Rating") == getfinState.__getitem__("Rating")]

            for lineid, items in  enumerate(prediction):

                if items.__getitem__("Rating") == getfinState.__getitem__("Rating"):

                    catDict = {"Category":items.__getitem__("Category").__str__().strip(),"System":items.__getitem__("System").__str__().strip(),
                                "Platform":items.__getitem__("Platform").__str__().strip()}

                    klass.filteronPrediction.__setitem__(lineid,catDict)


            targetfunctopush.send(klass.filteronPrediction)

    
    '''
        From the given list, filter categories
    '''
    @theMetas.pipeline
    def filterRelevantCats(klass,targetfunctopush):

        '''
            Determine the matching and most matching categories
        '''

        while  True:
            
            predicatedIp = yield

            for tableid,data in predicatedIp.items():

                core_engine_logger.info("Category matching relevantly for the given query :- %s "%data.__getitem__("Category"))


            core_engine_logger.info("\n\n")

            getMaxCat = max(predicatedIp.values(), key = lambda x:x.__getitem__("Category"))

            #From the list above determine the most occurring

            core_engine_logger.info("\n\n")
            core_engine_logger.info("Category that most matches the given query is :- %s" %getMaxCat.__getitem__("Category"))
            core_engine_logger.info("\n\n")

            targetfunctopush.send((predicatedIp.values(),getMaxCat))


    '''
        From the given category, determine the system and platform
    '''
    @theMetas.pipeline
    def analyzeFinalCats(klass):

        '''
            Filter all entries where the key == category that most matches the given query
        '''

        while True:
            
            listofSolutions,mostmatchingSolution = yield

            # Filter all entries where the key == category that most matches the given query
            getFilteredTable = filter(lambda x:x.__getitem__("Category") == mostmatchingSolution.__getitem__("Category"), listofSolutions)

            getNoEntries = len(getFilteredTable)
            #Form a tuple of Platform and the System!
            getTuple = [(data.__getitem__('Platform'),data.__getitem__('System')) for data in getFilteredTable]
            getCount = theMetas.find_occurrences(getTuple)

            for items,count in getCount.items():
                core_engine_logger.info("Probability of occurrence of %s is %s "%(items,(int(count)/int(getNoEntries))*100))
                


    '''
        Invoke the pipeline
    '''
    def execute(klass,fileName,ipQuery):

        '''
            Execute the functions in the pipeline
        '''

        getattr(klass,'loadFile').__call__(fileName,ipQuery,getattr(klass,
            'catMachineFeed').__call__(getattr(klass,'analyzeUserInput').__call__(getattr(klass,
                    'summary').__call__(getattr(klass,'predictandRoute').__call__(getattr(klass,
                                "filterRelevantCats").__call__(getattr(klass,'analyzeFinalCats')()))))))
