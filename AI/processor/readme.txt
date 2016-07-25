										Learning based query handler

# ****************************************************************************************************************** #


AIM:

	Implementation of Machine learning algorithm to process some input from an User in a text format

	The Following Pattern follows a Structured Supervised approach with labelled data and it's instance knowledge based.


Purpose:

	Classifies the query from the User and assigns priority, routes to the respective team for handling


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
	   *** But we will limit our patterns and compile them only according to our requirement
	-> The data is then offered a rating and ran against the model
	-> The Query is labelled with a tag (possibly the road to the solution)
	-> Whenever a query is given, Machine refers to it's experience gained from training and suggets a solution

	<!-- -> If the machine is not aware of the solution, it tries to give an approx solution and also pickles it. --> ##TODO

	*** The machine actually learns from various set of inputs fed by the input file and applies an algorithm against the new data.

	Note :: Pickling means saving the data that was generated during an interpreter session to be used in the sessions. I have referenced pickling as an example,
	meanwhile several other strategies are possible, such as invoking other pipelines, interacting with DB and so on ...

Example:

	Let's take an example ;

		Query ::  Please upgrade my ram to 16GB
		machine :: Splits the query, collects keywords, analyzes it and runs it against the model that was obtained through
		initial training data, allocates priority and assigns to the respective team for handling.

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

					--> utils
						--> __init__.py
						--> metas.py       =====> Does Metaprogramming tasks to support machine

					--> input
						--> support.csv	=====> The Input file used for training


Sample Input Data:

Customer Name,Problem Statement,Technician,Category,Document Attached,Document Name,Issue Resolved
Sandra ,"I can't remember my password",Sam,CRITICAL,FALSE,,Yes
Susanne,My PC is too slow,Andrew,MEDIUM,FALSE,,Yes
Tim Peters,I can’t print anything!,Peters,LOW,FALSE,,Yes
Alex Regan,My mobile device isn’t syncing my emails?,Tom,MEDIUM,TRUE,ScreanCapture03402.jpg,Yes
Mike,Can I have second monitor?,Anna,LOW,FALSE,,Yes
Arun,Why is the internet/network so slow?,David,MEDIUM,FALSE,,Yes
.
.
.
...............

Steps:

  --> Read and store machine feeds (training data)
	--> Categorize training data and save for further processing
	--> Create a model from data and response (Knowledge feed to the machine)
	--> Get the User query and process it - say split and store it in a container
	--> Get the query(new input) and form a regular expression pattern
	--> Process the query against the model and draft a prediction
	--> Write the result to an output file. Also log it in the UI.


Built-in Modules used:

	sys,os,re

# ****************************************************************************************************************** #