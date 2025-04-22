from mysql import connector
from app.config.envs import Envs

class DatabaseConnection:
    _envs = Envs.get_envs()
    
    def __init__(self):
        try:
            self._connection = connector.connect(**{
                "host": self._envs.get("HOST"),
                "user": self._envs.get("USER"),
                "password": self._envs.get("PASSWORD"),
                "database": self._envs.get("DB_NAME")
            })
            self._cursor = self._connection.cursor( dictionary=True )
            
        except Exception as error:
            self._connection = None
            self._cursor = None
            print("Error al conectarse a la base de datos")
    
    def get_cursor( self ):
        return self._cursor
        
    def commit( self ):
        self._connection.commit()
        
    def close( self ):
        self._cursor.close()
        self._connection.close();