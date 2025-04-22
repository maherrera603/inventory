from app.domain.respositories.userRepository import UserRepository
from app.infrastructure.datasource.mongo.userDatasourceImp import UserDatasource

class UserRepositoryImp( UserRepository ):
    _datasource: UserDatasource
    def  __init__(self, datasource: UserDatasource ):
        self._datasource = datasource
        
    def find_one(self, id):
        return super().find_one(id)
    
    def find_user(self, email):
        return self._datasource.find_user( email )