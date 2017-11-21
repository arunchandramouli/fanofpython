
import logging
import html_reports_config


logging.basicConfig(level=logging.INFO)
pygit = logging.getLogger("PyGit")


# Class to create a HTML Report

class HtmlReports(object):

	"""
		Initialization block
	"""
	def __init__(instance,instance_of_file_reader_class,
								htm_output_file_name,file_write_mode):

		"""
		Initialize required attributes
		:param instance_of_file_reader_class : Instance of class File_Reader
		:param htm_output_file_name : Full path of output file
		:param file_write_mode : Write or Append mode
		"""

		# Create an instance of HTML Class
		instance.html_webpage = html_reports_config.Html_Reports_Config
		instance.instance_of_file_reader_class = instance_of_file_reader_class
		instance.htm_output_file_name = htm_output_file_name
		instance.file_write_mode = file_write_mode


	"""
		Create a Table
	"""
	def create_html_table(instance):

		"""
			Create a new html file
		"""

		get_all_records = instance.instance_of_file_reader_class.file_read_yield_records()


		try:
			
			while True:

				# Get each row and add as table row with cells
				cell_values = get_all_records.next()
				form_table_row = "<tr>"
				end_table_row = "</tr>"
				all_cell_vals = ""

				for indexing , each_cell_value in enumerate(cell_values.split(",")):

					if "&" in str(each_cell_value) : 

						each_cell_value = str(each_cell_value).replace("&",",")
					
					all_cell_vals += "<td class='status'> %s </td>"%str(each_cell_value)

				get_each_row = str(form_table_row) + str(all_cell_vals) + str(end_table_row)

				yield str(get_each_row)


		except StopIteration as error:

			pygit.info("Table Creation completed. ")

		except Exception as error :

			raise error



	"""
		Define the Start of the Table
	"""
	def define_start_table(instance):

		"""
			Define the Start of the table
		"""

		try:

			return instance.instance_of_file_reader_class.file_write_records(file_name =instance.htm_output_file_name, 
				file_write_mode = "w" , object_to_write = instance.html_webpage.start_html_report())

		except Exception as error :

			raise error



	"""
		Define the end of the Table
	"""
	def define_end_table(instance):

		"""
			Define the Start of the table
		"""

		try:

			return instance.instance_of_file_reader_class.file_write_records(file_name =instance.htm_output_file_name, 
				file_write_mode = instance.file_write_mode , object_to_write = instance.html_webpage.end_html_report())

		except Exception as error :

			raise error



	"""
		Write the table to an HTML File
	"""
	def write_output_file(instance):

		try:

			return instance.instance_of_file_reader_class.file_write_records(instance.htm_output_file_name ,
			instance.file_write_mode,
			instance.create_html_table())

		except Exception as error :

			raise error


	"""
		Publish the HTML Report
	"""
	def publish_html_report(instance):

		"""
			Publish the HTML Report - Invoke the execution
		"""

		try:
			
			# Step 1 :: Start of the HTML Web-Page

			instance.define_start_table()

			# Step 2 :: Write Rows to HTML Table

			instance.write_output_file()

			# Step 3 :: End of the HTML Web-Page

			instance.define_end_table()
		

		except Exception as error_publish_report:
		
			raise error_publish_report

		
# Class to read input file and pass the values

class File_Reader(object):

	"""
		Initialization block
	"""
	def __init__(instance,file_name):

		#Read the file and pass the records
		instance.file_name = file_name


	"""
		Open the file , read records and yield
	"""
	def file_read_yield_records(instance):

		"""
		Read the file and yield records
		:param file_name : Name of the input file
		:yield records from the file
		"""

		with open(instance.file_name,"r") as input_file_reader:

			# Skip first line

			input_file_reader.next()

			# Process for the remaining records in the file

			for each_line in input_file_reader:

				yield each_line


	"""
		Open the file , write to it
	"""
	def file_write_records(instance , file_name , file_write_mode , object_to_write):

		"""
			Write to Output file
			:param file_name : Full path of the output file
			:param file_write_mode : write or append mode , "w" or "a"
			:param object_to_write : Object to iter, fetch records and write , for eg : a Generator object
		"""

		try :

			with open(file_name,file_write_mode) as file_writer :

				for each_record in object_to_write:

					file_writer.write(each_record)
					file_writer.write("\n")

		except Exception as error :

			raise error

