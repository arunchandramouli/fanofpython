import openpyxl
import re


_values_to_eliminate =['%Change','Thousand Metric']
'''
 S1 : Check for headers to be present in various rows in the file, if yes, split by the headers
 S2 : Check for Sub-Tables inside the main table eg : Sheet-T8 , oil1114.xlsx
'''

def read_excel(excelfull_path):


	sheet = openpyxl.load_workbook(excelfull_path)
	ws = sheet.get_sheet_by_name('T1')	
	
	'''
		S0: Load all the Sheet Values into a Container for Processing
	'''
	get_rows_val = eliminate_values_container(load_values_container(container = [] , iter_rows =ws.iter_rows()))


	header_value , mx_mn ,len_max , len_min =  determine_headers(get_rows_val)

	

	'''
		S1 : Headers are present in more than one location  - Refer Sheet T3 , File -> oil1114.xlsx

		OECD Americas: Imports of Crude Oil, NGL and Refinery Feedstocks 1							
							Thousand metric tons
		Imports from:	2012	2013	1Q2013	2Q2013	3Q2013	4Q2013	Jan2014 --> Header
		Australia	274	143	2	65	76	-	-
		Belgium	2017	2362	501	514	770	577	164
		Canada	127017	135706	34998	31743	33658	35307	12955		
		Denmark	7	62	56	6	-	-	-

		OECD Asia Oceania: Imports of Crude Oil, NGL and Refinery Feedstocks 1							
							Thousand metric tons
		Imports from:	2012	2013	1Q2013	2Q2013	3Q2013	4Q2013	Jan2014
		Australia	3097	3416	769	985	708	954	115
		Belgium	-	-	-	-	-	-	-
		Canada	-	-	-	-	-	-	-
		Denmark	-	-	-	-	-	-	-
		France	-	-	-	-	-	-	-

	'''

	
	get_list_headers_location = check_headers_in_file(header_value,get_rows_val)	

	'''
		S2 : Check for Sub-Tables - Refer Sheet T8 , File -> oil1114.xlsx

		The Sheet has only one header but the rows are split by keys representing values beneath
		and all the keys belong to the same table and header

											%Change	%Change
			2012	2013	1Q2013	2Q2013	3Q2013	4Q2013	Jan2014	Current	Year to **** --> Header **** 
									Month1	Date2
		OECD Americas **** --> Key **** 
		
		Liquefied Petroleum Gases	20978	20805	4185	7130	6587	2903	1319	16.5	16.5
		Naphtha	15530	16839	4026	4217	4395	4201	1466	1.2	1.2
		Total Gasoline3	431393	442597	105054	110542	112624	114377	37072	3.7	3.7
		
		
		OECD Asia Oceania **** --> Key **** 
		Liquefied Petroleum Gases	6967	7527	1817	1929	2048	1733	662	7.6	7.6
		Naphtha	38992	40102	10535	9174	10334	10059	3377	-7.5	-7.5
		Total Gasoline3	70715	70529	17432	16850	17951	18296	6056	-0.1	-0.1

	'''

	presence_of_sub_tables = check_presence_of_sub_tables(get_rows_val,len_max , len_min,header_value)


	'''
		Form the Final Table
	'''

	if len(get_list_headers_location) > 1:

		'''
			Step 1: Get the indexes of the headers in the table
		'''

		get_rows_val_split_headers_indexes = [i for i,x in enumerate(get_rows_val) if x == header_value]


		'''
			Step 2: Split the table into multiple based on the indexes
		'''

		for indexid,indexes in enumerate(get_rows_val_split_headers_indexes):

			try:
				print get_rows_val[indexes:get_rows_val_split_headers_indexes.__getitem__(indexid+1)]

			except IndexError:
				print False
				print get_rows_val[get_rows_val_split_headers_indexes[-1]:]


		'''
			Compute the Table
		'''


def check_presence_of_sub_tables(get_rows_val,len_max , len_min,header_value):
	'''
		Iterate through the table rows and check for sub-tables as described above
	'''
	
	# Check all indexes whose length is 1
	
	get_min_position = [position for position,value in enumerate(get_rows_val) if len(value) == len_min]

	# Filter the index whose next index has a length on max ==> len_max

	if get_min_position:

		'''
			Return the indexes of Sub-tables headers, the rows that have only 1 cell and next row contains max entries as
			figured out by len_max
		'''

		return [pos_index for pos_index in get_min_position if not pos_index+1 == len(get_rows_val) and len(get_rows_val.__getitem__(pos_index+1)) == len_max \
			and not get_rows_val.__getitem__(pos_index+1) == header_value]
	
		


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

def eliminate_values_container(get_rows_val,elims = []):

	if not elims is None: elims = []

	for data in get_rows_val:
		for values in _values_to_eliminate:
			if values.lower() in ''.join(data).lower():
				elims.append(data)
	
	for values in elims:
		get_rows_val.remove(values)


	return get_rows_val


def determine_headers(iter_rows_data):

	
	lenght_list = [len(items) for items in iter_rows_data]
	len_max , len_min = max(lenght_list),min(lenght_list)

	for items in iter_rows_data:

		if len(items) == len_max or len(items) == len_max - 1:		

			return items,len(items) == len_max,len_max , len_min 


read_excel("oil1114.xlsx")