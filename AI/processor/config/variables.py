'''
    This module serves as a config space for all variables used for calculation
'''



config_variables = {"variables":{"jobName":0,"problem":1,"resolution":2,"system":3,
                                "issueplatform":4,"applicationPlatform":5,
                                "category":6,"reportedBy":7}}

# the list of variables to be used for analysis
itemsToConsider = ['Resolution','System','Platform','JobName','AppPlatform','Category','ReportedBy']

# final list for probability calculation - this will be displayd to the user
_finitemsToConsider = ['JobName','System','Platform','AppPlatform','Category','ReportedBy']
#_finitemsToConsider = ['System','Platform']