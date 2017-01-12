
import multiprocessing
import os
import requests
 
########################################################################
class Files_Parallel_Process(object):

	#----------------------------------------------------------------------
	    def __init__(self, files):

	        """ Initialize class with list of files """
	        self.files = files
	        self.counter = 0

	#----------------------------------------------------------------------
	    def run(self):
	        """
	          Download the files and waits for the processes to finish
	        """
	        jobs = []
	        for url in self.files:
 	          process = multiprocessing.Process(target=self.worker, args=(url,))
	          jobs.append(process)
	          process.start()

	        for job in jobs:
	           job.join()

	#------------------------------------------------------------------------

	    '''
  		  Read an input file line by line
	    '''

	    def worker(self,inputfile):
	    	
				reader = open(inputfile)
				lines = reader.readlines()
				self.counter += len(lines)	       
				return self.counter


#----------------------------------------------------------------------
if __name__ == "__main__":

	files_to_automate= []

	for dir_name,folder_name,files_list in os.walk("../big"):

		for data in files_list:
			files_to_automate.append(os.path.join(dir_name,data))


	downloader = Files_Parallel_Process(files_to_automate)
	downloader.run()
	print downloader.counter