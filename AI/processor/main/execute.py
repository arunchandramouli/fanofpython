
import sys
import logging

# Append the Path!
sys.path.append("..\utils")
import metas
import engine

# Crate a logger and assign to engine and metas

core_engine_logger = logging.getLogger("Core Engine :: ")
logging.basicConfig(level=logging.INFO)

setattr(metas,"core_engine_logger",core_engine_logger)

# Set soem values to the engine
setattr(engine,"core_engine_logger",core_engine_logger)
setattr(engine,"theMetas",metas)

# Apply a decorator and convert all the methods as classmethods
engine.Core_Engine = metas.classdecorator(engine.Core_Engine)

#metas.applyToMultipleAttrs(engine.Core_Engine,['addtoContainer'],metas.pipeline)

def driver(ipfileName,userQuery):

	'''
		Invoke the engine driver and execute the code
	'''

	engine.Core_Engine.execute(ipfileName,userQuery)


# Execution block
if __name__ == "__main__":   

   driver(ipfileName = "..\\input\\support.csv", userQuery= "Having connectivity issue in uat")