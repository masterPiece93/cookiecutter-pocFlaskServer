import os
from environs import env

env.read_env()


class ServerStartupVariables:
    """
    variables related to server startup
    """

    PORT = env.int("PORT")
    HOST = "0.0.0.0"

class SecurityRelatedVariables:

    SECRET_KEY = os.urandom(24)

class Config(ServerStartupVariables):
    """
    main configuration variables
    """

    DEBUG = env.bool("DEBUG")
    
    
