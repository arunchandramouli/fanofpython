import sys

sys.path.insert(0,"\\Code\\holy\\python\\presentation\\fanofpython\\tests\\code\\turing\\")

import utils.helpers
import logging

'''
	Logger Attributes
'''

logging.basicConfig(level=logging.INFO)
appLog = logging.getLogger("Turing -")


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

			getrecord = utils.helpers.read_yield_records(file_path)		

			while True:				

				yield getrecord.next().split(",")

		except StopIteration as I:

			logging.info("All Records Processed")


	@classmethod
	def identify(instance,records):

		for record in records:

			print record




'''
	Code Execution
'''		

if __name__ == "__main__":


	fetch_records = Processor.fetch_records_file("\\Code\\holy\\python\\presentation\\fanofpython\\tests\\code\\turing\\config\\orders.csv")

	Processor.identify(fetch_records)


