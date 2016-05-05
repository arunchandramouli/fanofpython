import config,time,os

'''
	Use a Coroutine and push the file to the target!
'''
def autogen(func):
	def theGenerator(*args,**kargs):
		theResult = func(*args,**kargs)
		theResult.next()
		return theResult
	return theGenerator



'''
	Load the File, validate and push for further processing
'''
def loadtheFile(fileName,targetfunctopush):

	if os.path.exists(fileName):
		targetfunctopush.send(open(fileName,"w"))
	else : raise Exception(' File path is invalid %s '%fileName)	


'''
	The Function that writes o/p to the csv file
'''
@autogen
def writetoCSV():

	while True:
		fileName = yield
	
		fileName.write(str(getattr(config,"headersinCSVFile")))
		fileName.write('\n')
		fileName.write(str(("START",getattr(config,"startValueR2"),getattr(config,"startValueR3"),time.time(),time.time()))) # The initial value
		
		# Save start values in a variable
		row2StartValue = getattr(config,"startValueR2") 
		row3StartValue = getattr(config,"startValueR3")

		# Save start time in a variable
		row2StartTime = row3StartTime = time.time()
		

		# Iterate until all the entries are completed!

		for iters in range(getattr(config,"countOfEntries")+1):

			# Write the O/p to the CSV File
			fileName.write(str(("A"+str(iters),row2StartValue+getattr(config,"incrementFactorR2"),
				row3StartValue+getattr(config,"incrementFactorR3"),
				row2StartTime+getattr(config,"timeincrementFactorR2"),
				row3StartTime+getattr(config,"timeincrementFactorR3"))))

			# Keep incrementing for next record
			row2StartValue = row2StartValue+getattr(config,"incrementFactorR2")
			row3StartValue = row3StartValue+getattr(config,"incrementFactorR3")
			row2StartTime = row2StartTime+getattr(config,"timeincrementFactorR2")
			row3StartTime = row3StartTime+getattr(config,"timeincrementFactorR3")

			fileName.write('\n') # We need a line break :-)

		fileName.close() # Close the file as a good habit :-)


# Run the Code
if __name__ == "__main__":

	loadtheFile.__call__(fileName = config.csvFileLocation,targetfunctopush = writetoCSV.__call__())