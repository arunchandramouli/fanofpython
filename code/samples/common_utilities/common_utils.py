'''
	This py file consists of commonly used functions that can be reused at various sources	
'''

'''
	Import all the required module to perform the operations
'''

import openpyxl
from lxml import etree
import requests
import logging
import json
from StringIO import StringIO
import csv

import PyPDF2


logging.basicConfig(level=logging.INFO)

core_logger= logging.getLogger("Common_Utils")


'''
	Read an excel file and store it's values
'''

def read_excel(excel_file_full_path, sheet_name = None):

	'''
		Parameters

			excel_file_full_path - Full path of the excel to read
			sheet_name - If specified, read only that sheet else read all sheets
	'''

	'''
		Load the workbook into memory
	'''
	fetch_workbook = openpyxl.load_workbook(excel_file_full_path)

	'''
		Get the Sheet names from the workbook
	'''
	get_sheet_names = fetch_workbook.get_sheet_names()

	'''	
		If the Sheet name is provided then act on that sheet alone
		else act on all the sheets in the excel file
	'''

	if bool(sheet_name): 

		for row_data in read_each_sheet(fetch_workbook,sheet_name):
			yield row_data

	else:

		'''
			Read each and every sheet in the excel file and yield values
		'''

		for each_sheet in get_sheet_names:
	
			for row_data in read_each_sheet(fetch_workbook,each_sheet):
	
				yield row_data

	

'''
	Read the sheet - row by row and yield the values
'''
def read_each_sheet(fetch_workbook,sheet_name):

	'''
		Parameters

			sheet_name - Name of the sheet to be read
	'''

	sheet_to_read = fetch_workbook.get_sheet_by_name(sheet_name.strip())

	'''
		Load each row value into a list
		This includes each cell value in a Row
	'''
	for current_row in sheet_to_read.iter_rows() :

		'''
			In case of an exception continue with the next row
		'''
		try:
			'''
				Join cell values by a "," and yield it, keep yielding such for all rows in the file
			'''
			get_each_row_data = ','.join([str(cell.value).encode("utf-8").strip() for cell in current_row if cell.value is not None])

			'''
				If the row is not None - [] , then yield the row for
				further processing ... 
			'''
			if bool(get_each_row_data): 

				yield get_each_row_data

		except Exception as E:			
			#core_logger.critical("Exception found in row  %s "%current_row)
			core_logger.critical("Exception Message %s "%E)
			core_logger.info("Proceeding next row ...")
			continue




'''

	Read a text-file line by line and yield values
'''

def read_txt_file(txt_file_full_path,as_container = False):

	'''
		Parameters
			txt_file_full_path - Full path of the text file
	'''

	with open(txt_file_full_path,'rb') as reader:		

		
		yield reader.readlines() if bool(as_container) else reader.read()


'''
	Read a Json file and yield values
'''

def read_json_file(json_file_full_path):


	'''
		Parameters
			json_file_full_path - Full path of the json file
	'''

	with open(json_file_full_path,"rb") as json_data:
		'''
			Let json load the data, such that it can be accessed in a dictionary format
		'''
		get_json_data = json.load(json_data)
		yield get_json_data


'''
	Read an XML file and yield the values
'''

def read_xml(xml_file_full_path):

	'''
		Parameters
			xml_file_full_path - Full Path of the XML File
	'''

	
	# Get the Data
	with open(xml_file_full_path,"rb") as reader:
		get_lines = reader.read()

	# Create an Iterator
	context = etree.iterparse(StringIO(get_lines))

	# Iterate and yield values
	for action, elem in context:

		if elem.text is not None:

			yield(elem.tag,elem.text.strip())

'''
	Read a CSV file and yield values
'''

def csv_read(full_path_csv_file):

	'''
		Parameters
			
			full_path_csv_file - Full Path of the CSV File
	'''
	csv_file = open(full_path_csv_file, 'rb')

	reader = csv.reader(csv_file)

	'''	
		Use a Generator to yield the values
	'''

	try:
		while True:

			get_record = reader.next()
		
			# Returns a LIST
			yield get_record

	except StopIteration as SOP:

		core_logger.info("All Records Processed!")


'''
	Read a PDF File Page by Page and yield values
'''

def read_pdf(full_path_pdf_file,page_num = None):

	'''
		Parameters

			full_path_pdf_file - Full Path of the PDF File
	'''

	# Create a PDF File Object
	pdfFileObj = open(full_path_pdf_file, 'rb')

	# Create a PDF File Reader
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	get_total_pages = pdfReader.numPages
	core_logger.info("Total n.o. pages %s "%get_total_pages)

	if page_num is not None:
		get_page_content = pdfReader.getPage(page_num)

		try:
			yield gets_page_content.extractText().encode("utf-8")
		except Exception as E:
			core_logger.critical("Exception %s on page %s "%(E,page_num))
			yield None

	else:

		for each_page in range(1,get_total_pages):
			try:
				core_logger.info("Processing Page %s "%each_page)

				get_page_content = pdfReader.getPage(each_page)
				yield  get_page_content.extractText().encode("utf-8")

			except Exception as E:
				core_logger.critical("Exception %s on page %s "%(E,each_page))
				continue


'''
	Run - Execute
'''
def run():

	# Read an Excel
	"""for data in read_excel("input_files/automate.xlsx",sheet_name="Table2"):
		print data,'\n'"""


	"""
	#Read a text file

	for lines in read_txt_file("input_files/dsa.txt"):
		print lines
	"""

	
	#Read a Json file
	
	'''
	for values in read_json_file("input_files/youtube.json"):
		print values
	'''

	# Read an XML File

	'''for elemtag,elemtext in read_xml("input_files/parts.xml"):
		print elemtag,elemtext.strip()'''

	# Read a CSV File
	'''for records in csv_read("input_files/tests.csv"):
		print records'''

	# Read a PDF File
	'''
	for records in read_pdf("input_files/MOMR.pdf",10):
		print records'''



'''
	Run the Code
'''	

if __name__ == "__main__":


 	run()