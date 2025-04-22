from bson.objectid import ObjectId
from app.domain.datasources.CategoryDatasource import CategoryDataSource
from app.data.mongo.database import DatabaseConnection
from app.domain.entities.category.categoryEntity import CategoryEntity

class CategoryDatasourceImp( CategoryDataSource ):
    _connection: DatabaseConnection
    
    def __init__(self, database: DatabaseConnection ):
        self._connection = database.get_instance()
        
    def find_one(self, id):
        if ObjectId.is_valid( id ) is False:
            return None
        
        data = self._connection.categories.find_one({ "_id": ObjectId( id) })
        return data
    
    def find(self):
        categories = self._connection.categories.find()
        return categories
        
    def find_category(self, category):
        category = self._connection.categories.find_one({ "category": category })
        return category
    
    def create(self, addCategoryDto) -> bool:
        try:
            addCategoryDto.user = ObjectId( addCategoryDto.user )
            data = self._connection.categories.insert_one( addCategoryDto.to_object() )
            return data.acknowledged;
        except Exception as error:
            return False     
    
    def update(self, id, updateDto) ->bool:
        try:
            category_update =  updateDto.to_object()
            del category_update["id"]
            
            result = self._connection.categories.update_one(
                {"_id": ObjectId( id ) },
                {"$set": category_update }
            )
            
            return result.modified_count > 0
        except Exception as error:
            return False
    
    def delete(self, id):
        try:
            result = self._connection.categories.delete_one({ "_id": ObjectId(id) })
            return result.deleted_count > 0
        except Exception as error:
            return False

    def count_registers(self):
        return self._connection.categories.count_documents({})