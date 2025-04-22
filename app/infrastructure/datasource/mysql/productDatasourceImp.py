from app.data.mysql.database import DatabaseConnection
from app.domain.datasources.productDatasource import ProductDatasource

class ProductDatasourceImp( ProductDatasource ):
    _connection: DatabaseConnection
    
    def __init__(self, database: DatabaseConnection ):
        self._connection = database
        self._cursor = self._connection.get_cursor()
        
    def find(self):
        self._cursor.execute("SELECT * FROM products")
        return self._cursor.fetchall()
    
    def find_one(self, id):
        self._cursor.execute("SELECT * FROM products WHERE id=%s", (id, ))
        return self._cursor.fetchone()
    
    def find_by_sku(self, sku):
        self._cursor.execute("SELECT * FROM products WHERE sku=%s", ( sku, ))
        return self._cursor.fetchone()
    
    def create(self, productCreateDto):
        try:
            sql = "INSERT INTO products (name, sku, category, quantity, price, status, user, created_at, updated_at) "
            sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self._cursor.execute( sql, (
                productCreateDto.name, 
                productCreateDto.sku, 
                productCreateDto.category, 
                productCreateDto.quantity, 
                productCreateDto.price,
                productCreateDto.status,
                productCreateDto.user,
                productCreateDto.created_at,
                productCreateDto.updated_at
            ))
            self._connection.commit()
            return True
        except Exception as error:
            return False
        
    def update(self, id, productUpdateDto):
        try:
            sql = "UPDATE products SET name=%s, category=%s, quantity=%s, price=%s, status=%s, updated_at=%s "
            sql += "WHERE id=%s"
            
            self._cursor.execute( sql, (
                productUpdateDto.name,
                productUpdateDto.category,
                productUpdateDto.quantity,
                productUpdateDto.price,
                productUpdateDto.status,
                productUpdateDto.updated_at,
                id
            ))
            
            self._connection.commit()
            return self.find_one( id )
        except Exception as error:
            return False
            
    
    
    def delete(self, id):
        try:
            self._cursor.execute("DELETE FROM products WHERE id=%s", ( id, ))
            self._connection.commit()
            return True
        except Exception as error:
            return False
    
    def count_registers(self):
        try:
            self._cursor.execute("SELECT COUNT(*) as count FROM products")
            result = self._cursor.fetchone()
            return result.get("count")
        except Exception as error:
            return 0