from app.domain.respositories.categoryRepository import CategoryRespository
from app.domain.datasources.CategoryDatasource import CategoryDataSource

class CategoryRepositoryImp( CategoryRespository ):
    _datasource: CategoryDataSource
    
    def __init__(self, dataSource: CategoryDataSource ):
        self._datasource  = dataSource
    
    def find(self):
        return self._datasource.find()
        
    def find_one(self, id):
        return self._datasource.find_one( id )
    
    def find_category(self, category):
        return self._datasource.find_category( category )
        
    def create(self, addCategoryDto):
        return self._datasource.create( addCategoryDto )
    
    def update(self, id, updateDto):
        return self._datasource.update( id, updateDto )
    
    def delete(self, id):
        return self._datasource.delete( id )
    
    def count_registers(self):
        return self._datasource.count_registers()
    
        
    