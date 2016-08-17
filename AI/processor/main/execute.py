
import sys
import logging

# Append the Path!
sys.path.append("..\utils")
import metas


# Set access to engine and metas module

core_engine_logger = logging.getLogger("Core Engine :: ")
logging.basicConfig(level=logging.INFO)
setattr(metas,"core_engine_logger",core_engine_logger)

import engine

setattr(engine,"core_engine_logger",core_engine_logger)
setattr(engine,"theMetas",metas)

engine.Core_Engine = metas.classdecorator(engine.Core_Engine)

#metas.applyToMultipleAttrs(engine.Core_Engine,['addtoContainer'],metas.pipeline)

def driver(ipfileName,userQuery):

    engine.Core_Engine.execute(ipfileName,userQuery)

# Execution block
if __name__ == "__main__":   

   driver(ipfileName = "..\\input\\support.csv", userQuery= "Having connectivity issue in uat")


'''

THIS IS REGARDING PROJECT "P0501728 ELENDING AUDIT DATA ARCHIVAL WE ARE HAVING CONNECTIVITY ISSUE IN UAT. 
PLEASE FIND THE LOGS FOR ERRORS:  HERE IS THE JIRA FOR DETAIL REFERENCE MPS00002-1025 IN CASE REQUIRED  

'''