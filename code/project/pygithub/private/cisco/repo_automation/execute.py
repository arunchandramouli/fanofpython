import github
import logging
import datetime

logging.basicConfig(level=logging.INFO)
pygit = logging.getLogger("PyGit")

class Reports(object):

	"""
		Initialization block
	"""
	def __init__(instance):

		instance.gh = github.Github(login_or_token = "f5c140ebf56bbe364485b1a8d7915c7714644df2",
			base_url='https://wwwin-github.cisco.com/api/v3')

		instance.user = instance.gh.get_user()


	"""
		Get all the repos
	"""
	def get_all_repos(instance):

		"""
			List all available repos
		"""

		instance.repos = instance.user.get_repos()

		return instance.repos
   	

   	"""
   		Filter and extract the required repository
   	"""
   	def filter_repo(instance,repo_name):
   		
   		"""
   		From the list of available repo , filter required repo
   		:param repo_name : Repository name - for eg :: cafy/cafyap
   		:return Repository name if valid , else False
   		"""
  	   	
  	   	try:

		 	for each_repo in instance.get_all_repos():

	   			if str(repo_name) == str(each_repo.name):

	   				# Return the Repository itself
	   				return each_repo

	   		# If not found return False
	   		return False

	   	except Exception as error :
	   		pygit.error(error)


	"""
		Access a repository and obtain pull requests information
	"""
	def get_all_pull_requests_from_repository(instance,repo_name):

   		"""
   		From the repo , obtain the pull requests
   		:param repo_name : Repository name - for eg :: cafy/cafyap
   		:return Repository name if valid , else False
   		"""

   		get_reqd_repo = instance.filter_repo(repo_name)

		for each_pull_request in get_reqd_repo.get_pulls():

			try:

				"""
				Form a string seperated by "," to write to a csv file
				and yield it
				"""

				# n.o. hours the PR is open
				open_for_hours = instance.calculate_time_diff(each_pull_request.created_at , datetime.datetime.now())

				# If there would be any reviewer assigned

				if bool(each_pull_request.assignee):

					reviewer_list = {}

					get_list_reviewers = instance.add_reviewers(each_pull_request.assignees,reviewer_list)

					to_input_csv = (str(each_pull_request.number )+"," +str(open_for_hours)+ "," + str(each_pull_request.state).upper() + "," + str(each_pull_request.commits)
						+","+str(each_pull_request.title).replace(",","") + "," +str(each_pull_request.user.name)
						+","+str(get_list_reviewers) +","+str(each_pull_request.created_at) + ","+"GREEN")

				else:

					to_input_csv = (str(each_pull_request.number )+"," +str(open_for_hours)+ "," + str(each_pull_request.state).upper() + "," + str(each_pull_request.commits)
						+","+str(each_pull_request.title).replace(",","") + "," +str(each_pull_request.user.name)
						+","+str("Not Assigned to any Reviewer yet") +","+str(each_pull_request.created_at) + ","+"RED")

				
				# yield for processing

				yield to_input_csv

			except Exception as error :

				pygit.error("Exception %s while processing pull request number %s and ID %s - raised by author - %s "%(error,
					each_pull_request.number,each_pull_request.id,each_pull_request.user.name))

				continue

	"""
		Write the final output to a csv file
	"""
	def write_csv_reports(instance,repo_name,
		file_name):
		"""
		Write final o/p to csv
		:param repo_name : Repository name to parse
		:param file_name : csv output file name		
		: required fields in the report;

		number | state | commits count | Title | url | user name | Assignees | Assignee | Details |  Created At | Updated At | ID
		"""

		# Reports

		pygit.info("Extract CSV Reports ")

		# Fetch the output
		fetch_output = instance.get_all_pull_requests_from_repository(repo_name)

		try:			
			
			"""
				Write to an output file
			"""

			with open(str(file_name),"w") as pywrite:

				#Write Headers
				pywrite.write("Number, Open for how many hours? , State , N.O. Commits, Title , Raised By , Reviewers , Created At ,Flag")
				pywrite.write("\n")

				while True:				

					get_data = fetch_output.next()
					pywrite.write(str(get_data))
					pywrite.write("\n")
						

		except StopIteration as prog_completion:

			pygit.info("Write to csv completed ")


	"""
		Add the list of reviewers and return
	"""
	@staticmethod
	def add_reviewers(list_of_reviewers,reviewer_container):
		"""
			Add all reviewers of a PR to a container
			:param list_of_reviewers - List obtained from PR
			:param reviewer_container - Container where Reviewer data is stored
		"""

		try:

			for each_reviewer in list_of_reviewers:
				
				try:
					
					reviewer_container.__setitem__(each_reviewer.name , each_reviewer.name)					
					
				except Exception as error:
					pygit.error(error)
					continue

			return " & ".join(reviewer_container.keys())

		except Exception as n_error:

			pygit.error(n_error)


	@staticmethod
	def calculate_time_diff(curr_time , created_at_time):
		"""
		Calculate the difference between past and current time in
		Days , Hours , Minutes , Seconds
		:param curr_time : obtained as datetime.datetime.now()
		:param created_at_time : taken from repository - shows as datetime.datetime.now()

		"""

		"""
			::TODO:: Add more clarity
		"""

		try:

			calculate_diff_hours = curr_time - created_at_time

			return str(calculate_diff_hours).replace("-","").replace(","," ")

		except Exception as error :
			pygit.error("Unable to calculate time difference ")
			return "None"


""" Execution block """
if __name__ == "__main__" :


	# First create a Github instance:
	
	get_reports = Reports()

	# Repository name
	set_repo_name = "cafyap"

	get_reports.write_csv_reports(set_repo_name,"%s.csv"%set_repo_name)
