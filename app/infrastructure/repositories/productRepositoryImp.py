from app.domain.respositories.productRepository import ProductRepository
from app.domain.datasources.productDatasource import ProductDatasource

class ProductRepositoryImp( ProductRepository ):
    _datasource: ProductDatasource
    
    def __init__(self, datasource: ProductDatasource):
        self._datasource = datasource

    def find(self):
        return self._datasource.find()
    
    def find_one(self, id):
        return self._datasource.find_one( id )
    
    def find_by_sku(self, sku):
        return self._datasource.find_by_sku( sku )
    
    def create(self, productCreateDto):
        return self._datasource.create( productCreateDto )

    def update(self, id, productUpdateDto):
        return self._datasource.update( id, productUpdateDto )
    
    def delete(self, id):
        return self._datasource.delete( id )
    
    def count_registers(self):
        return self._datasource.count_registers()