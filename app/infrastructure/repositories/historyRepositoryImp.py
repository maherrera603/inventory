from app.domain.respositories.historyRepository import HistoryRepository
from app.domain.datasources.HistoryDatasource import HistoryDatasource

class HistoryRepositoryImp( HistoryRepository ):
    
    _datasource: HistoryDatasource
    
    def __init__(self, datasource: HistoryDatasource):
        self._datasource = datasource
        
    def find(self):
        return self._datasource.find()
    
    def find_one(self, id):
        return self._datasource.find_one( id )
    
    def create(self, historyCreateDto):
        return self._datasource.create( historyCreateDto )
    
    def count_registers(self):
        return self._datasource.count_registers()