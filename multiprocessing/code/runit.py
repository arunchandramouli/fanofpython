import os

import Queue
from threading import Thread

import datetime

########################################################################
class Files_Parallel_Process(Thread):

	#----------------------------------------------------------------------
	    def __init__(self, queue):

	        """ Initialize class with list of files """
	        Thread.__init__(self)
	        self.queue = queue
	        self.counter = 0

	#----------------------------------------------------------------------
	    def run(self):
	        """
	          Download the files and waits for the processes to finish
	        """

	        while True:
	        	# Get the Dir and File
	        	directory_name,file_name = self.queue.get()
	        	self.worker(directory_name,file_name)
	        	self.queue.task_done()

	#------------------------------------------------------------------------

	    '''
  		  Read an input file line by line
	    '''

	    def worker(self,directory_name,file_name):

				inputfile = os.path.join(directory_name,file_name)
				reader = open(inputfile)
				lines = reader.readlines()
				self.counter += len(lines)	
				print self.counter       
				return self.counter


#----------------------------------------------------------------------
if __name__ == "__main__":

	files_to_automate= []
	queue = Queue.Queue()
	ts = datetime.datetime.now()

	# Create 8 worker threads
	for x in range(8):
		worker = Files_Parallel_Process(queue)
		# Setting daemon to True will let the main thread exit even though the workers are blocking
		worker.daemon = True
		worker.start()

	for dir_name,folder_name,files_list in os.walk("../big"):

		for data in files_list:
			queue.put((dir_name,data))

	queue.join()
	ts2 = datetime.datetime.now()

	print('Took {}'.format(ts2 - ts))