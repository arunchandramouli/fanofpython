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

			utils.helpers.convert_to_data_type()


			'''
				Fetch all the records from the file
			'''

			get_each_record = utils.helpers.read_yield_records(file_path)		


			while True:				

				#yield get_each_record.next().split(",")

				yield get_top_record.next().split(",")

		except StopIteration as I:

			logging.info("All Records Processed")


	'''
	'''

	@classmethod
	def identify(instance,records):

		for record in records:

			if not len(record) == 25 : appLog.info(record)

			print record ,"\n\n"


'''
	Code Execution
'''		

if __name__ == "__main__":


	fetch_records = Processor.fetch_records_file(config.configuration.csv_automate)

	Processor.identify(fetch_records)


