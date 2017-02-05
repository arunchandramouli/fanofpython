'''
	This py file consists of commonly used functions that can be reused at various sources	
'''

'''
	Import all the required module to perform the operations
'''

import openpyxl
import lxml
import requests
import logging

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
			if bool(get_each_row_data): yield get_each_row_data

		except Exception as E:			
			#core_logger.critical("Exception found in row  %s "%current_row)
			core_logger.critical("Exception Message %s "%E)
			core_logger.info("Proceeding next row ...")
			continue


				



def run():

	for data in read_excel("input_files/mes.xlsx"):
		print data,'\n'


'''
	Run the Code
'''	

if __name__ == "__main__":


 	run()