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

def convert_to_data_type(array_of_items):

	'''
		For eg :: 

			string -> type<str>
			int -> type<int>
	'''

	data_type_array= []

	for items in array_of_items:

		{
			str(items).lower().startswith("int"): data_type_array.append(types.IntType),
			str(items).lower().startswith("float"): data_type_array.append(types.FloatType),
			str(items).lower().startswith("str"): data_type_array.append(types.StringType)
		}

	return data_type_array


