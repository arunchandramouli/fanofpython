
# -*- coding: UTF-8 -*-

'''

	SECTION - IMPORTS

'''

from multiprocessing import Pool
import datetime
import requests
from threading import Thread
import os
import time
from random import random
import sys
import Queue
from lxml import html
import urllib2

sys.setrecursionlimit(10000)



'''
	
	Aim :: To multithread task of performing an operation on containers

	Here we take many containers as input and perform operation on each of its elements

	We peform this operation in parallel, say each process will hold a container


	*** In this example, we will hit several URLs and get their contents - imagine if we have
	to process several millions on a daily basis ***

'''



'''
	A Simple example of multithreading, this example will not be affected by GIL

	Say , We want to take multiple iterables and perform operations
'''



def openfile(file_name):


	with open(file_name,'r') as reader:

		return reader.readlines()



'''	
	Execute
'''

def execute(func):

	def mapper(*args,**kargs):


		start = time.time()

		result = func(*args,**kargs)

		end = time.time()

		print "Time Taken %s "%(end-start)

		return result

	return mapper



def return_list_of_files_in_dir(dir_name):

	file_to_process = []
	for maindir , sunfolder , files in os.walk(os.path.join(os.getcwd(),dir_name)):

		for each_file in files:

			get_file_name = os.path.join(maindir,each_file)

			file_to_process.append(get_file_name)

	return file_to_process




''' Execute it using Threads '''
@execute
def multitask(single=False):

	file_to_process = return_list_of_files_in_dir("files")

	
	if single:

		for get_file_name in file_to_process:

			openfile(get_file_name)


	for get_file_name in file_to_process:

			t = Thread(target = openfile,args = (get_file_name,))
			t.start()
			t.join()




if __name__ == "__main__" :


	print "Single Thread ... ",'\n\n'	
	multitask(True)

	print "Multi Thread ... ",'\n\n'
	multitask()

	''' Lets Use maps '''

	print "Maps ... ",'\n\n'
	start = time.time()
	map(openfile,return_list_of_files_in_dir("files"))

	print time.time() - start 
	print "\n\n\n\n"
