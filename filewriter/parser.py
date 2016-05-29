import config,time,os

import sys


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
def loadtheFile(ipfileName,targetfunctopush):

	if os.path.exists(ipfileName):		
		targetfunctopush.send(ipfileName)
	else : raise Exception(' File path is invalid %s '%ipfileName)	

adds = set()

'''
	The Function that adds value to the container
'''
@autogen
def addtoContainer(targetfunctopush):

	while True:
		fileName = yield					
		with open(fileName,'r') as reader:			
			for lines in (reader.readlines()):
				for data in lines.split(","):			
					adds.add(str(data).lower().strip())	
		targetfunctopush.send(adds)

'''
	The Function that writes to the o/p file
'''
@autogen
def writeToOpFile(opFileName):

	while True:
		containerData = yield					
		with open(opFileName,'w') as writer:
			for lines in sorted(containerData):				
				writer.write(lines.strip())
				writer.write('\n')
# Run the Code
if __name__ == "__main__":

	loadtheFile.__call__(ipfileName = sys.argv[1],
		targetfunctopush = addtoContainer.__call__(targetfunctopush = 
	 writeToOpFile.__call__(opFileName = sys.argv[2])))