##################################################
# overrides for the webapp deployment

DEBUG = True
PORT = 5027
SSL = False
THREADED = True

############################################
# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://gateway:9200"
ELASTIC_SEARCH_INDEX = "jper"
ELASTIC_SEARCH_VERSION = "1.5.2"

# Classes from which to retrieve ES mappings to be used in this application
# (note that if ELASTIC_SEARCH_DEFAULT_MAPPINGS is sufficient, you don't need to
# add anything here
ELASTIC_SEARCH_MAPPINGS = [
    # "service.dao.MyDAO"
]

# initialise the index with example documents from each of the types
# this will initialise each type and auto-create the relevant mappings where
# example data is provided
ELASTIC_SEARCH_EXAMPLE_DOCS = [
    # "service.dao.MyDAO"
]

############################################
# important overrides for account module

ACCOUNT_ENABLE = False
SECRET_KEY = "super-secret-key"

#############################################
# important overrides for storage module

STORE_IMPL = "octopus.modules.store.store.StoreLocal"
STORE_TMP_IMPL = "octopus.modules.store.store.TempStore"

from octopus.lib import paths
STORE_LOCAL_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "live")
STORE_TMP_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "tmp")


#############################################
# Re-try/back-off settings

# from the http layer

# specific to this app

# Minimum amount to leave between attempts to deposit, in the event that there was a semi-permanent error
# default to 1 hour
LONG_CYCLE_RETRY_DELAY = 3600

# Maximum number of times to try and deposit before giving up and turning off repository sword submission
# for a given account
LONG_CYCLE_RETRY_LIMIT = 24


###############################################
## Other app-specific settings

# The date from which the first request against the JPER API will be made when listing a repository's
# notifications
DEFAULT_SINCE_DATE = "1970-01-01T00:00:00Z"

# how many seconds in between each run of the script
RUN_THROTTLE = 2

# whether to store sword response data (receipt, etc).  Recommend only to store during testing operation
STORE_RESPONSE_DATA = False