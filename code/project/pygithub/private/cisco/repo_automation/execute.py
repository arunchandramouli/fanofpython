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

		# Create git hub repository instance
		instance.gh = github.Github(login_or_token = "f5c140ebf56bbe364485b1a8d7915c7714644df2",
			base_url='https://wwwin-github.cisco.com/api/v3')

		# Fetch the User details
		instance.user = instance.gh.get_user()

		#Setting as none
		instance.__class__.review_modified_state = {}

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

			if each_pull_request.number :


				try:

					"""
					Form a string seperated by "," to write to a csv file
					and yield it
					"""

					# Setting a class object					
					instance.__class__.pr_created_by = each_pull_request.user.name

					#Setting as none
					instance.__class__.review_modified_state = {}


					# n.o. hours the PR is open
					open_for_hours = instance.calculate_time_diff(each_pull_request.created_at , datetime.datetime.now())

					# 'get_review_comments', 'get_reviewer_requests', 'get_reviews'

					pygit.info("Processing Pull Request number %s "%str(each_pull_request.number))

					#import pdb;pdb.set_trace()

					get_list_reviewers = instance.get_reviewers_list(each_pull_request.get_reviews(),
						reviewers_list_container = {})


					get_list_reviewers_that_responded = instance.get_reviewers_list(each_pull_request.get_review_comments(),
						reviewers_list_container = {})

					get_list_get_reviewer_requests = instance.get_reviewer_requests_list(each_pull_request.get_reviewer_requests(),
						reviewers_list_container = {})

					final_reviewers = instance.parse_reviewers_list(str(get_list_reviewers) + " & "+str(get_list_get_reviewer_requests))

					get_reviewer_total_response = instance.get_total_response(each_pull_request)

					get_count_of_reviewers = instance.get_count_reviewers(final_reviewers)

					get_flag_state = instance.set_state_flag(get_count_of_reviewers,instance.__class__.review_modified_state)

					who_has_to_act_on_pr = instance.set_action_item_team_for_pr_closure(get_flag_state)

					# If there would be any reviewer assigned

					if bool(get_list_reviewers) or bool(get_list_get_reviewer_requests):

						to_input_csv = (str(each_pull_request.number )+","+str(each_pull_request.title).replace(",","")+"," +str(each_pull_request.user.name)+ "," + str(final_reviewers) + "," + str(get_reviewer_total_response)+","+str(open_for_hours)
							+","+str(instance.repo_name) + "," +str(each_pull_request.state)+","+str(each_pull_request.commits) + ","+str(get_flag_state)+","+str(who_has_to_act_on_pr))

					else:

						to_input_csv = (str(each_pull_request.number )+","+str(each_pull_request.title).replace(",","")+"," +str(each_pull_request.user.name)+ "," + str("Not assigned yet") + "," + str(get_reviewer_total_response)+","+str(open_for_hours)
							+","+str(instance.repo_name) + "," +str(each_pull_request.state)+","+str(each_pull_request.commits) + ","+str(get_flag_state)+","+str(who_has_to_act_on_pr))

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

		number , open for ? , state , no  commits , title , raised by , list of reviewers , review updated by , created at , flag
		"""

		# Reports

		pygit.info("Extract Reports from repository %s "%str(repo_name))

		instance.repo_name = repo_name

		# Fetch the output
		fetch_output = instance.get_all_pull_requests_from_repository(repo_name)

		try:			
			
			"""
				Write to an output file
			"""

			with open(str(file_name),"w") as pywrite:

				# Number , Title , Raised by , Reviewers,open for how many?,Repository,State,No Commits,Flag

				#Write Headers
				pywrite.write("Number , Title , Raised by , Reviewers,Total Reply from Reviewers , Open for how long - in days?,Repository,State,No Commits,Flag, Action Item On ?")
				pywrite.write("\n")

				while True:				

					get_data = fetch_output.next()
					pywrite.write(str(get_data))
					pywrite.write("\n")
						

		except StopIteration as prog_completion:

			pygit.info("Reports extaction completed for repository %s "%str(repo_name))	


	"""
		Get count of Reviewers
	"""
	@staticmethod
	def get_count_reviewers(final_reviewers,set_flag=None):
		"""
		 Get the number of reviewers , as marked by the PR Owner
		 :param final_reviewers : Reviewers - delimited by "&"
		 :param set_flag : If n.o. reviewers < 3 : Set Flag as RED
		"""

		try:
			
			count_of_reviewers = final_reviewers.split("&")

			return len(count_of_reviewers)

		except Exception as e:
			set_flag = "NA"

		return set_flag

	
	"""
		Verify flag mode
	"""
	@staticmethod
	def verify_flag_mode(state_change_list):
		"""
		Veify the state and return
		:param state_change_list : List of state changes made by Reviewers
		:return True or False		
		"""

		try:
			
			if not bool(state_change_list) : return False

			for each_state in state_change_list:

				if not str(each_state).lower().lstrip().rstrip() == 'approved':
					
					return False
		except Exception as error:
			return False
		
		return True


	"""
		Check the State of the Flag
	"""
	@classmethod
	def set_state_flag(instance,count_of_reviewers,state_change_list):
		"""
			Flag to be defined as RED , YELLOW , BLUE
			:param count_of_reviewers : Total n.o. Reviewers
			:param state_change_list : State as modified by the Reviewers
			:return RED or BLUE or YELLOW
		"""
		try:
			
			if bool(instance.verify_flag_mode(state_change_list.keys())):

				return "BLUE"
						
			if int(count_of_reviewers) < 3 : 

				return  "RED"

			return "YELLOW"
			
		except Exception as e:
			
			return "ERROR"
	
	"""
		Action item on teams for PR Closure
	"""
	@staticmethod
	def set_action_item_team_for_pr_closure(get_flag_state):
		"""
			Decide which team has to act on the PR at given point of time
			:param get_flag_state : RED or BLUE or YELLOW

				if state is BLUE => Team-Infra else => PR Owner
		"""

		try:

			return "Core Infra" if str(get_flag_state).lower()=="blue" else "PR Owner"
		except Exception as error:
			return "NA -Exception"

	"""
	Get Count of responses from the Reviewers
	"""

	@classmethod
	def get_total_response(instance,each_pull_request,reviewers_list_container={}):
		"""
			Get total response from Reviewers
			:param each_pull_request : Current Pull Request object
			:param reviewers_list_container - Container where Reviewer data is stored
		"""

		try:

			if not reviewers_list_container == {} : reviewers_list_container = {}

			get_total_response_pr_from_reviewers = 0

			for each_reviewer in each_pull_request.get_reviews():
				
				try:

					if not (str(each_reviewer.user.name.lower().lstrip().rstrip()) == str(instance.pr_created_by.lower().lstrip().rstrip())):

						instance.review_modified_state.__setitem__(each_reviewer.state,each_reviewer.state)

						get_total_response_pr_from_reviewers += 1
					
				except Exception as error:
					pygit.error(error)
					continue
			
			return get_total_response_pr_from_reviewers

		except Exception as n_error:

			pygit.error(n_error)
			return "NA"


	"""
		Get list of Reviewers to whom its requested
	"""

	@classmethod
	def get_reviewer_requests_list(instance,list_of_reviewers,reviewers_list_container):
		"""
			Add all reviewers of a PR to a container
			:param list_of_reviewers - List obtained from PR
			:param reviewers_list_container - Container where Reviewer data is stored
		"""

		try:

			if not reviewers_list_container == {} : reviewers_list_container = {}

			for each_reviewer in list_of_reviewers:
				
				try:

					if not (str(each_reviewer.login.lower().lstrip().rstrip()) == str(instance.pr_created_by.lower().lstrip().rstrip())):

						reviewers_list_container.__setitem__(each_reviewer.login , each_reviewer.login)					
					
				except Exception as error:
					pygit.error(error)
					continue
			
			return " & ".join(reviewers_list_container.keys())

		except Exception as n_error:

			pygit.error(n_error)
			return "NA"



	"""
		Get list of Reviewers
	"""

	@classmethod
	def get_reviewers_list(instance,list_of_reviewers,reviewers_list_container):
		"""
			Add all reviewers of a PR to a container
			:param list_of_reviewers - List obtained from PR
			:param reviewers_list_container - Container where Reviewer data is stored
		"""

		try:

			if not reviewers_list_container == {} : reviewers_list_container = {}

			for each_reviewer in list_of_reviewers:
				
				try:

					if not (str(each_reviewer.user.name.lower().lstrip().rstrip()) == str(instance.pr_created_by.lower().lstrip().rstrip())):

						reviewers_list_container.__setitem__(each_reviewer.user.name , each_reviewer.user.name)					
					
				except Exception as error:
					pygit.error(error)
					continue
			
			return " & ".join(reviewers_list_container.keys())

		except Exception as n_error:

			pygit.error(n_error)
			return "NA"

	"""
		Parse Reviewers list
	"""
	@staticmethod
	def parse_reviewers_list(list_of_reviewers):

		"""
		Parse the reviewers list to remove extra "&"
		:param list_of_reviewers : A String
		"""

		try:

			list_of_reviewers = list_of_reviewers.lstrip().lstrip("&").strip()
			list_of_reviewers = list_of_reviewers.rstrip().rstrip("&").strip()

			return list_of_reviewers

		except Exception as error :

			return list_of_reviewers
	"""
		Add the list of reviewers and return
	"""
	@staticmethod
	def get_assignees_list(list_of_assignees,assignees_container):
		"""
			Add all reviewers of a PR to a container
			:param list_of_reviewers - List obtained from PR
			:param reviewer_container - Container where Reviewer data is stored
		"""

		try:

			for each_assignee in list_of_assignees:
				
				try:
					
					assignees_container.__setitem__(each_assignee.name , each_assignee.name)					
					
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

			return str(calculate_diff_hours.days).replace("-","").replace(","," ")

		except Exception as error :
			pygit.error("Unable to calculate time difference ")
			return "None"


""" Execution block """
if __name__ == "__main__" :


	# First create a Github instance:
	
	get_reports = Reports()

	# Repository name
	set_repo_name = "cafyap"

	get_reports.write_csv_reports(set_repo_name,"reports.csv")
