
class Core_Engine:

				'''
					Read and store machine feeds (training data)
				'''
				def getMachineFeeds(): .....

				'''
					Categorize training data and save for further processing
				'''
				def catMachineFeed(): .....

				'''
					Create a model from data and response (Knowledge feed to the machine)
				'''
				def createModel(): ..... # This is the model that serves as a guide for new inputs

				'''
					Get the User query and process it - say split and store it in a container
				'''
				def storeNewInput(): .....# We will split and store in a container

				'''
					Get the query(new input) from the User and classify it (say True/False/Valid/Invalid/0/1 ... etc...)
				'''
				def classifyNewInput(): ..... # We will classify as valid/invalid based on some keyword

				'''
					Process the query against the model and draft a prediction
				'''
				def analyzeNewInput(): ...... # We run it against the model, instance based approach to predict a match

				'''
					Write the result to an output file. Also log it in the UI.
				'''
				def result(): ..... # Predicted output. Also I pickle the model for further analysis if any on extension