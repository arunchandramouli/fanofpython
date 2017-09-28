import os

'''
	Utils file for file processing and related
'''



'''
	A Function to read file and generate values 
'''


def read_yield_records(file_path):

	'''
		Yield Records

		Params:

			file_path = Path where the file is stored!
	'''

	try:

		with open(file_path,'r') as newreader:

			'''
				Yield line by line , continue to next line
				in case of an exception
			'''

			for line in newreader:

				yield line.strip()

	except Exception as F:

		raise Exception("Please ensure that the path to the specified file is valid! ")