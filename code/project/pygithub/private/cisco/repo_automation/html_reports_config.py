
# Supporting Class to create a HTML Report

class Html_Reports_Config(object):

	"""
		Start of the HTML Report
	"""
	@staticmethod
	def start_html_report():

		set_start_html_page = [ """
						<!DOCTYPE html>
							<html>
								<head>
									<title>Automation GIT - Pull Requests  Status</title>
								</head>

							<body>
								
								<br><br>
									<div> <center>  <b> Pull Requests - Contributors and Status </b> </center> </div>
								<br><br>

								<table border="7" cellpadding="12" , cellspacing="4"> 

									<tr ><td ><b> PR Number </b></td><td> <b> Title </b></td><td><b>  Raised by </b> </td>
									<td> <b> Reviewers </b> </td><td><b> Total Reply from Reviewers  </b> </td>
									<td> <b> Open for - days? </b> </td>
									<td> <b> Repository </b> </td>
									<td> <b> State </b> </td>
									<td> <b> No Commits </b> </td>
									<td> <b> Flag </b> </td>
									<td> <b> Action Item On ? </b>  </td></tr>

		""" ]

		return set_start_html_page

	"""
		End of Report
	"""
	@staticmethod
	def end_html_report():

		set_end_html_page = [ """

						</table>
					</body>
				</html>
		""" ]

		return set_end_html_page