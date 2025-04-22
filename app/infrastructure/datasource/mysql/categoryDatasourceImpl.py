from app.domain.datasources.CategoryDatasource import CategoryDataSource
from app.data.mysql.database import DatabaseConnection

class CategoryDatasourceImp( CategoryDataSource ):
    _connection: DatabaseConnection
    _cursor: any
    
    def __init__(self, database: DatabaseConnection):
        self._connection = database
        self._cursor = self._connection.get_cursor()
        
    def find(self) -> list :
        self._cursor.execute( "SELECT * FROM categories" )
        return self._cursor.fetchall()
        
    def find_one(self, id):
        self._cursor.execute( "SELECT * FROM categories WHERE id=%s", ( id, ))
        return self._cursor.fetchone()
    
    def find_category(self, category):
        self._cursor.execute( "SELECT * FROM categories WHERE category=%s", ( category, ))
        return self._cursor.fetchone()
    
    def create(self, addCategoryDto):
        try:
            self._cursor.execute(
                "INSERT INTO categories ( category, status, user, created_at, updated_at) VALUES(%s, %s, %s, %s, %s )",
                ( addCategoryDto.category, addCategoryDto.status, addCategoryDto.user, addCategoryDto.created_at, addCategoryDto.updated_at )
            )
            self._connection.commit()
            return True
        except:
            self._connection.rollback()
            return False
    
    def update(self, id, updateDto):
        try:
            self._cursor.execute(
                "UPDATE categories SET category=%s, status=%s, updated_at=%s WHERE id=%s",
                (updateDto.category, updateDto.status, updateDto.updated_at, id )
            )
            self._connection.commit()
            return True
        except Exception as error:
            return False
    
    def delete(self, id):
        try:
            self._cursor.execute("DELETE FROM categories WHERE id=%s", (id, ))
            self._connection.commit()
            return True
        except Exception as error:
            return False
        
    def count_registers(self):
        try:
            self._cursor.execute("SELECT COUNT(*) as count FROM categories")
            result = self._cursor.fetchone()
            return result.get("count")
        except Exception as error:
            return 0
            