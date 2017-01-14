import openpyxl
import re


'''
 S1 : Check for headers to be present in various rows in the file, if yes, split by the headers
 S2 : Check for Sub-Tables inside the main table eg : Sheet-T8 , oil1114.xlsx
'''

def read_excel(excelfull_path):


	sheet = openpyxl.load_workbook(excelfull_path)
	ws = sheet.get_sheet_by_name('T6')	
	
	get_rows_val = load_values_container(container = [] , iter_rows =ws.iter_rows())		
	header_value , mx_mn ,len_max , len_min =  determine_headers(get_rows_val)

	'''
		S1 : Headers are present in more than one location
	'''
	if bool(mx_mn):
		check_headers_in_file(header_value,get_rows_val)

	'''
		S2 : Check for Sub-Tables
	'''


def check_headers_in_file(headerinfo,get_rows_val,row_id_info = []):

	if not row_id_info == None: row_id_info = []

	for row_id,row_data in enumerate(get_rows_val):
		if headerinfo == row_data:
			row_id_info.append(row_id)
	return row_id_info

def load_values_container(container,iter_rows):


	'''
		Get all sheet values into a Container
	'''
	if container is not None:
		container = []

	for row in iter_rows:
		filter_container = []

		row_data = [cell.value for cell in row if cell.value is not None]
		if row_data  != []: 	
			
			new_cell_val = ''
			for each_cell in row_data:				
				try:
					new_cell_val += str(each_cell).strip()+","
					
				except UnicodeEncodeError:
					new_cell_val += re.sub('[^A-Za-z0-9\.]+', '-', each_cell).strip()+','					
			
			
			container.append(new_cell_val.split(",")[0:-1])			
			

	return container


def determine_headers(iter_rows_data):

	
	lenght_list = [len(items) for items in iter_rows_data]
	len_max , len_min = max(lenght_list),min(lenght_list)

	for items in iter_rows_data:

		if len(items) == len_max or len(items) == len_max - 1:		

			return items,len(items) == len_max,len_max , len_min 


read_excel("oil1114.xlsx")