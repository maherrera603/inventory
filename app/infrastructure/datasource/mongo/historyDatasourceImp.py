from bson.objectid import ObjectId
from app.data.mongo.database import DatabaseConnection
from app.domain.datasources.HistoryDatasource import HistoryDatasource
from app.domain.entities.history.historyEntity import HistoryEntity

class HistoryDatasourceImp( HistoryDatasource ):
    
    _connection: DatabaseConnection
    
    def __init__(self, database: DatabaseConnection):
        self._connection = database.get_instance()
    
    def find(self):
        histories = self._connection.histories.find()
        return histories
    
    def find_one(self, id):
        history = self._connection.histories.find_one({ "_id": ObjectId( id )})
        return history
    
    def create(self, historyCreateDto):
        try:
            if ObjectId.is_valid( historyCreateDto.product ) is False:
                return False
            
            if ObjectId.is_valid( historyCreateDto.user ) is False:
                return  False
            
            historyCreateDto.product = ObjectId( historyCreateDto.product )
            historyCreateDto.user = ObjectId( historyCreateDto.user )
            self._connection.histories.insert_one( historyCreateDto.to_object() )
            return True
        except Exception as error:
            return False
    
    def count_registers(self):
        return self._connection.histories.count_documents({})
    
    