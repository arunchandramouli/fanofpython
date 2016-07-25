import engine

import sys
import logging

# Append the Path!
sys.path.append("..\utils")
import metas

# Set access to engine and metas module

core_engine_logger = logging.getLogger("Core Engine :: ")

setattr(engine,"core_engine_logger",core_engine_logger)
setattr(engine,"theMetas",metas)
setattr(metas,"core_engine_logger",core_engine_logger)
engine.Core_Engine = metas.classdecorator(engine.Core_Engine)

#metas.applyToMultipleAttrs(engine.Core_Engine,['addtoContainer'],metas.pipeline)

def driver(ipfileName,userQuery):

    engine.Core_Engine.execute(ipfileName,userQuery)

# Execution block
if __name__ == "__main__":

    driver(ipfileName = "..\\input\\support.csv", userQuery= "Set up Visual Studio latest version")
