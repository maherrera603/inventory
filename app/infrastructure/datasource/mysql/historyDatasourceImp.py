from app.domain.datasources.HistoryDatasource import HistoryDatasource
from app.data.mysql.database import DatabaseConnection

class HistoryDatasourceImp( HistoryDatasource ):
    _connection: DatabaseConnection
    
    
    def __init__(self, database: DatabaseConnection ):
        self._connection = database
        self._cursor = self._connection.get_cursor()
        
    def find(self):
        self._cursor.execute("SELECT * FROM histories")
        return self._cursor.fetchall()
    
    def find_one(self, id):
        self._cursor.execute( "SELECT * FROM histories WHERE id=%s", ( id, ))
        return self._cursor.fetchone()
    
    def create(self, historyCreateDto):
        try:
            sql = "INSERT INTO histories (type, description, product, quantity, user, created_at, updated_at)"
            sql += "VALUES ( %s, %s, %s, %s, %s, %s, %s )"
            self._cursor.execute( sql, (
                historyCreateDto.type,
                historyCreateDto.description,
                historyCreateDto.product,
                historyCreateDto.quantity,
                historyCreateDto.user,
                historyCreateDto.created_at,
                historyCreateDto.updated_at
            ))
            
            self._connection.commit()
            return True
        except Exception as error:
            return False
    
    def count_registers(self):
        try:
            self._cursor.execute("SELECT COUNT(*) as count FROM histories")
            result = self._cursor.fetchone()
            return result.get("count")
        except Exception as error:
            return 0