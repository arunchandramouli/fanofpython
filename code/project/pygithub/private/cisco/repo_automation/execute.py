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

		"""instance.g = github.Github(login_or_token="beingadexter@gmail.com", 
			password="************")"""

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

			"""print each_pull_request.number , each_pull_request.state, each_pull_request.commits,each_pull_request.title
			print each_pull_request.url , each_pull_request.user.name , each_pull_request.assignees , each_pull_request.assignee
			print each_pull_request.body , each_pull_request.created_at , each_pull_request.updated_at,each_pull_request.id
			print "Diff ",each_pull_request.created_at - datetime.datetime.now()"""
			
			try:

				"""
				Form a string seperated by "," to write to a csv file
				and yield it
				"""

				# If there would be any reviewer assigned

				if bool(each_pull_request.assignee):

					to_input_csv = (str(each_pull_request.number ) + "," + str(each_pull_request.state) + "," + str(each_pull_request.commits)
						+","+str(each_pull_request.title).replace(",","") + "," +str(each_pull_request.url) + "," +str(each_pull_request.user.name)
						+","+str(each_pull_request.assignee.name) +","+str(each_pull_request.created_at)
						+","+str(each_pull_request.updated_at) +"," +str(each_pull_request.id))

				else:

					to_input_csv = (str(each_pull_request.number ) + "," + str(each_pull_request.state) + "," + str(each_pull_request.commits)
						+","+str(each_pull_request.title).replace(",","") + "," +str(each_pull_request.url) + "," +str(each_pull_request.user.name)
						+","+str("Not Assigned to any Reviewer yet") +","+str(each_pull_request.created_at)
						+","+str(each_pull_request.updated_at) +"," +str(each_pull_request.id))


				print "DATA ==== ",each_pull_request.created_at , datetime.datetime(each_pull_request.created_at)
				# yield for processing

				yield to_input_csv

				break

			except Exception as error :

				pygit.error("Exception %s while processing pull request number %s and ID %s - raised by author - %s "%(error,
					each_pull_request.number,each_pull_request.id,each_pull_request.user.name))


			"""print "Reviews "

			for ech in each_pull_request.get_reviews():# , each_pull_request.get_review_comment , each_pull_request.get_review_comments()
				print ech , ech.state  , ech.user.name ,"\n\n"

			print "Review Comments "

			for each_pull_comment in each_pull_request.get_review_comments():
				print each_pull_comment,"\n" , dir(each_pull_comment),"\n\n"


			print "\n\n"
			"""


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

		# Fetch the output
		fetch_output = instance.get_all_pull_requests_from_repository(repo_name)

		try:			

			
			"""
				Write to an output file
			"""

			with open(str(file_name),"w") as pywrite:

				#Write Headers
				pywrite.write("Number , State , N.O. Commits, Title , URL , Raised By , Assignees , Created At , Updated At , ID")
				pywrite.write("\n")

				while True:				

					get_data = fetch_output.next()
					pywrite.write(str(get_data))
					pywrite.write("\n")
						

		except StopIteration as prog_completion:

			pygit.info("Write to csv completed ")


""" Execution block """
if __name__ == "__main__" :


	# First create a Github instance:
	
	get_reports = Reports()

	# Repository name
	set_repo_name = "cafyap"

	get_reports.write_csv_reports(set_repo_name,"%s.csv"%set_repo_name)
