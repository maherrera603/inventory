from app.domain.datasources.userDatasource import UserDatasource
from app.data.mongo.database import DatabaseConnection


class UserDatasourceImp( UserDatasource ):
    _connection : DatabaseConnection
    
    def __init__(self, database: DatabaseConnection):
        self._connection = database.get_instance()
        
    def find_user(self, email) -> dict :
        return self._connection.user.find_one({ "email": email })

    
    def find_one(self, id):
        return super().find_one(id)