from app.domain.datasources.userDatasource import UserDatasource
from app.data.mysql.database import DatabaseConnection


class UserDatasourceImp( UserDatasource ):
    _connection: DatabaseConnection
    _cursor: any
    def __init__(self, database: DatabaseConnection ):
        self._connection = database
        self._cursor = database.get_cursor()
        
        
        
    def find_one(self, id):
        return super().find_one(id)
    
    def find_user(self, email):
        self._cursor.execute("SELECT * FROM users WHERE email=%s", ( email, ))
        return self._cursor.fetchone()
        
       