import os
import types

'''
	Utils file for file processing and related
'''



'''
	A Function to read file and generate values 
'''


def read_yield_records(file_path,option_read_no_rows=None):

	'''
		Yield Records

		Params:

			file_path = Path where the file is stored!
			option_read_no_rows = Select Top n.o. rows to read from the file
	'''

	try:

		with open(file_path,'r') as newreader:

			'''
				Yield line by line , continue to next line
				in case of an exception
			'''

			if bool(option_read_no_rows) : 


				header_line = next(newreader)
				types_line = next(newreader)

				yield header_line

				yield types_line


			else:

				'''
					Ignore top 2 rows
				'''

				header_line = next(newreader)
				types_line = next(newreader)


				for line in newreader:

					yield line.strip()

	except Exception as F:

		raise Exception("Please ensure that the path to the specified file is valid! ")




'''
	Convert string to data-type object
'''

def convert_to_data_type(array_of_items_generator):

	'''
		array_of_items_generator -> Row1 & Row2 from the csv file

		For eg :: 

			string -> type<str>
			int -> type<int>
	'''

	data_type_array = []

	header_line = next(array_of_items_generator)
	types_line_array_of_items = next(array_of_items_generator)


	for items in types_line_array_of_items.split(","):

			if str(items).lower().lstrip().rstrip().startswith("int"): data_type_array.append(types.IntType)
			elif str(items).lower().lstrip().rstrip().startswith("float"): data_type_array.append(types.FloatType)
			elif str(items).lower().lstrip().rstrip().startswith("str"): data_type_array.append(types.StringType)
			

	return data_type_array,header_line.split(",")


'''
	Identify data types of row values
'''

def identify_data_types_rows(row_values):

	'''
		row_values -> Row from the file

		Check if the values are float / string / int
	'''

	for row_val in row_values:

		row_val = str(row_val).lstrip().rstrip()

		if bool(check_handle_exception_data_types_ver(row_val, int)): yield types.IntType,row_val

		elif bool(check_handle_exception_data_types_ver(row_val, long)): yield types.IntType,row_val

		elif bool(check_handle_exception_data_types_ver(row_val, float)): yield types.FloatType,row_val
		
		elif bool(check_handle_exception_data_types_ver(row_val, str)): yield types.StringType,row_val


'''
	Check data-types of cell values
'''

def check_handle_exception_data_types_ver(row_val,datatypes):


	try:

		return datatypes(row_val).__class__ == datatypes

	except Exception as E:
		
		return False