from bson.objectid import ObjectId
from pymongo import ReturnDocument
from app.domain.datasources.productDatasource import ProductDatasource
from app.data.mongo.database import DatabaseConnection
from app.domain.entities.product.productEntity import ProductEntity

class ProductDatasourceImp( ProductDatasource ):
    _connection: DatabaseConnection
    def __init__(self, database: DatabaseConnection ):
        self._connection = database.get_instance()
        
        
    def find(self):
        data = self._connection.products.find()
        return data 
    
    def find_one(self, id):
        try:
            if ObjectId.is_valid( ObjectId( id ) ) is False:
                return None

            return  self._connection.products.find_one({ "_id": ObjectId(id) })
        except:
            return { "code": 500, "status": "Internal Server", "redirect": "index.products.index" }
    
    def find_by_sku(self, sku):
        return self._connection.products.find_one({ "sku": sku })
    
    def create(self, productCreateDto):
        try:
            if ObjectId.is_valid( productCreateDto.category ) is False:
                return False
            
            productCreateDto.category = ObjectId( productCreateDto.category )
            productCreateDto.user = ObjectId( productCreateDto.user )
            
            result = self._connection.products.insert_one( productCreateDto.to_object() )
            
            return result.acknowledged  
        except Exception as error:
            return False
    
    def update(self, id, productUpdateDto):
        try:
            if ObjectId.is_valid( id ) is False: 
                return { "code": 400, "status":"Bad Request", "msg": "Id del producto invalido"}
            
            productUpdateDto.category = ObjectId( productUpdateDto.category)
            productUpdateDto.user = ObjectId( productUpdateDto.user )
            data_update = productUpdateDto.to_object()
            del data_update["id"]
            
            print( data_update )
            
            product = self._connection.products.find_one_and_update(
                { "_id": ObjectId( id )},
                {"$set": data_update },
                return_document=ReturnDocument.AFTER
            )

            return product
        except Exception as error:
            print( error )
            return { "code": 500, "status": "Interna Server", "msg": "Ha ocurrido un error" }
           
    def delete(self, id):
        try:
            if ObjectId.is_valid( id) is False:
                return False
            
            result = self._connection.products.delete_one({ "_id": ObjectId( id) })
            return result.deleted_count > 0
        except Exception as error:
            return False
        
    def count_registers(self):
        return self._connection.products.count_documents({})
        