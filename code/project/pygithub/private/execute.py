import github
import logging

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

		instance.repo_cafykit = "cafykit"
		instance.repo_cafyap = "cafyap"

	
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


			print each_pull_request.number , each_pull_request.state, each_pull_request.commits,each_pull_request.title
			print each_pull_request.url , each_pull_request.user.name , each_pull_request.assignees , each_pull_request.assignee
			print each_pull_request.body , each_pull_request.created_at , each_pull_request.updated_at,each_pull_request.id
			
			print "Reviews "

			for ech in each_pull_request.get_reviews():# , each_pull_request.get_review_comment , each_pull_request.get_review_comments()
				print ech , "\n"

			print "Review Comments "

			for each_pull_comment in each_pull_request.get_review_comments():
				print each_pull_comment,"\n"

			break


""" Execution block """
if __name__ == "__main__" :


	# First create a Github instance:
	
	get_reports = Reports()

	get_reports.get_all_pull_requests_from_repository(get_reports.repo_cafyap)
