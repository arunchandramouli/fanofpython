import sys

sys.path.insert(0,"\\Code\\holy\\python\\presentation\\fanofpython\\tests\\code\\turing\\")


import utils.helpers
import logging
import config.configuration



'''
	Logger Attributes
'''

logging.basicConfig(level=logging.INFO)
appLog = logging.getLogger("Turing -")


'''
	Logging File Handlers
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
	'''

	@classmethod
	def identify(instance,records):

		'''
			Get the types object and header line
		'''

		types_object_line = records.next()

		header_line = records.next()


		for record in records:

			'''
				If the Record length is not == 2, write to bad logs
			'''

			if not len(record) == 25 : appLog.info(record)


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

				continue
'''
	Code Execution
'''		

if __name__ == "__main__":


	fetch_records = Processor.fetch_records_file(config.configuration.csv_automate)

	Processor.identify(fetch_records)


