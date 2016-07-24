
																										Learning based query handler

# ****************************************************************************************************************** #


AIM:

	Implementation of Machine learning algorithm to process some input from an User in a text format

	The Following Pattern follows a Structured Supervised approach with labelled data and it's instance knowledge based.


Strategy:

	-> Prepare Data (possibly from a CSV file or any form)
	-> Choose an Algorithm - We are gonna use Decision Trees and Instance based learning to route the query to correct team.
	-> Instances obtained through training data to serve as a model for the new queries
	-> We also do sentimental analysis of the query and assign it a rating
	-> We form a model with training data and it's output.
	-> Expose the new data to the model
	-> Validation
	-> Prediction (Output)


What's it and what it does?:

	The Machine a.k.a engine.py module file is the system that does the following operations;

	 -> Load the Machine with Inputs and form a Model
	 -> Execute the Pipeline
	 -> Compare new data against the model and form a prediction
	 -> Training instances from the model are searched for instance that most closely
	 		resembles new instance
	 -> Provide a Solution
	 -> Pickle it for further use *** ( Python pickling is used to save the user query as a pattern and the machine is trained from pickled data)
	 	  --> Similarly in this case, a DB could also be used to save the analysis.


How it Works?:

	-> The Machine undergoes training with random data that is pushed via the pipeline
	-> Form a model with known data and it's responses
	-> This model will be exposed to the new data
	-> The data is then analyzed semantically and tagged a value  (possibly the road to the solution)
	-> The Semantic analysis is based on the text, emotions and meaning composed, regular expressions are used to classify
	-> For eg: "Order placed for a new Pizza with extra cheese " --> Can be classified as New Order
	   *** But we will limit our patterns and compile them only according to our requirement
	-> The data is then pickled
	-> The Query is labelled with a tag (possibly the road to the solution)
	-> Whenever a query is given, Machine refers to it's experience gained from training and suggets a solution
	-> If the machine is not aware of the solution, it tries to give an approx solution and also pickles it.

	Note :: Pickling means saving the data that was generated during an interpreter session to be used in the sessions. I have referenced pickling as an example,
	meanwhile several other strategies are possible, such as invoking other pipelines, interacting with DB and so on ...


	Let's take an example ;

	  I get a query from an User that is processed in the pipeline and tagged an output, say in a dictionary format {"I love Python":"python.org"}
	  This is further pickled (saved in the system somewhere for further use). I can use this data for my analysis and output.

	  *** Meanwhile if the interpreter session would still be alive and multiple queries are passed sequentially, we can also do caching and save time and analysis.


Folder Structure in GIT:

	--> fanofpython

		--> AI

		    --> processor

		    	--> __init__.py    =====> Initialization File

		        --> readme

				--> main
				    --> __init__.py    =====> Initialization File
					--> engine.py      =====> Core Engine, the actual machine
					--> execute.py     =====> Call the Engine with User input as a string (fires the pipeline)

				--> prog
					--> __init__.py
					--> metas.py       =====> Does Metaprogramming tasks to support machine

				--> input
					--> training.csv	=====> The Input file used for training


Steps:

  --> Read and store machine feeds (training data)
	--> Categorize training data and save for further processing
	--> Create a model from data and response (Knowledge feed to the machine)
	--> Get the User query and process it - say split and store it in a container
	--> Get the query(new input) from the User and classify it (say True/False/Valid/Invalid/0/1 ... etc...)
	--> Process the query against the model and draft a prediction
	--> Write the result to an output file. Also log it in the UI.


Pseudocode:


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
						def storeNewInput() .....# We will split and store in a container

						'''
							Get the query(new input) from the User and classify it (say True/False/Valid/Invalid/0/1 ... etc...)
						'''
						def classifyNewInput() ..... # We will classify as valid/invalid based on some keyword

						'''
							Process the query against the model and draft a prediction
						'''
						def analyzeNewInput() ...... # We run it against the model, instance based approach to predict a match

						'''
							Write the result to an output file. Also log it in the UI.
						'''
						def result() ..... # Predicted output. Also I pickle the model for further analysis if any on extension

# ****************************************************************************************************************** #
