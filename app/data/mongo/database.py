from pymongo import MongoClient
from app.config.envs import Envs

class DatabaseConnection:
    
    __instance = None
    __envs: dict = Envs.get_envs()
    
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super( DatabaseConnection, cls ).__new__( cls )
            cls.__instance.client = MongoClient( cls.__envs.get("URL_CONNECTION") )
            cls.__instance.db = cls.__instance.client[ cls.__envs.get("DB_NAME") ]
        return cls.__instance

    
    def get_instance( self ):
        return self.db