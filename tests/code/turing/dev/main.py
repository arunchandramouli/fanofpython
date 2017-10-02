import sys

sys.path.insert(0,"\\Code\\holy\\python\\presentation\\fanofpython\\tests\\code\\turing\\")


import utils.helpers
import logging
import config.configuration
import traceback


'''
	Logger Attributes
'''

logging.basicConfig(level=logging.INFO)
appLog = logging.getLogger("Turing -")


'''
	Logging File Handlers
'''


'''
   For bad lines
'''

bad_logs = logging.FileHandler(config.configuration.log_file_handler)
appLog.addHandler(bad_logs)


'''
	Process the records
'''


class Processor(object):

	'''
		Obtain records from the file
	'''

	@classmethod
	def fetch_records_file(instance,file_path):

		'''
			Fetch the Records
		'''

		try:


			'''
				Fetch only top 2 records
			'''

			get_top_record = utils.helpers.read_yield_records(file_path,option_read_no_rows=True)

			types_object_line,header_line = utils.helpers.convert_to_data_type(get_top_record)

			
			yield types_object_line

			yield header_line
		

			'''
				Fetch all the records from the file
			'''

			get_each_record = utils.helpers.read_yield_records(file_path)		


			while True:				

				yield get_each_record.next().split(",")


		except StopIteration as I:

			logging.info("All Records Processed")


	'''
		Fetch the Records and data-types of each row value
	'''

	@classmethod
	def fetch_records_types_objects(instance,records):

		'''
			Get the types object and header line
		'''

		types_object_line = records.next()

		header_line = records.next()


		yield header_line

		yield types_object_line


		for record in records:

			'''
				If the Record length is not == 25 , write to bad logs
			'''

			if len(record) == 25 :


				'''
					Also verify if the row values reflect the data types specified in row-2
				'''

				try:

					load_record = utils.helpers.identify_data_types_rows(record)
					iter_types_object_line = iter(types_object_line)

					while True:
						
						get_data,row_val = load_record.next()

						get_data_iter_types_object_line = iter_types_object_line.next()
						
						'''
							If the row value doesn't match the data-type specified in Row - 2 , write to bad logs
						'''

						if not(get_data == get_data_iter_types_object_line) : 

							appLog.info("Field Value -- " + str(row_val) + "\n\n" + "Record -- " + ''.join(record) + "\n\n")					

				except StopIteration as T:

					yield record


			else :

				 appLog.info(" Record Length < 25 Rows " + ''.join(record))



	'''
		Form a mapping of column

		Take all values from each column and map into header
	'''

	@classmethod
	def map_header_columns_rows(instance , records):

		'''
			Create a Mapper - Header is the key, where as 
			values from row 2 -> End are values
		'''

		'''
			Get the types object and header line
		'''

		header_line = records.next()

		types_object_line = records.next()

		mark_container = {}


		'''
			Iterate and retrieve the records
		'''

		get_records = iter(records)


		try:

			while 1:
				
				for headers , types_obj , each_records in zip(header_line , types_object_line, get_records.next()):

					try:

						if not (headers,types_obj) in mark_container.keys():

							mark_container.__setitem__((headers,types_obj), [])

							mark_container[(headers,types_obj)].append(each_records)
							
						else:

							mark_container[(headers,types_obj)].append(each_records)

					except Exception as E:

						continue

		except StopIteration as e:
				
			yield mark_container


	'''
		Get output as per user input
	'''

	@classmethod
	def get_stats_input(instance,records,user_input):

		'''
			From the table generated in previous step ,
			analyze user input and get the result
		'''


		try:

			while True:

				get_records = records.next()

				for header , row_values in get_records.items():

					if str(user_input).strip() in header:

						get_header , get_data_type = header

						yield get_header , get_data_type , row_values

		except StopIteration:

			pass


	'''
		Analyze the column values against the user input and write to log
	'''
	@classmethod
	def analyze_stats_input(instance,records):

		'''
			As per the Readme , process for Str and int data-types
		'''

		get_header , get_data_type , row_values = records.next()


		get_result = utils.helpers.process_records_data_type(get_header , get_data_type , row_values)

		with open(config.configuration.fin_file_handler, 'a') as writer:


			writer.write(get_result + '\n\n') if bool(get_result) else writer.write("Exception %s \n\n "%traceback.extract_stack()+ '\n\n')



	'''
		Initiate the Process
	'''

	@classmethod
	def initiate(instance,user_input) :

		fetch_records = instance.fetch_records_file(config.configuration.csv_automate)

		fetch_records_obj = instance.fetch_records_types_objects(fetch_records)

		get_mapped_dict = instance.map_header_columns_rows(fetch_records_obj)

		get_stats_input_from_user = instance.get_stats_input(get_mapped_dict,user_input)

		instance.analyze_stats_input(get_stats_input_from_user)

		return 