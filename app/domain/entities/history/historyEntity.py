from datetime import datetime

class HistoryEntity:
    
    def __init__(self, id: str, type: str, description: str, product: str, quantity: str, user: str, created_at: str ):
        self.id = id
        self.type = type
        self.description = description
        self.product = product
        self.quantity = quantity
        self.user = user
        self.created_at = created_at
        
    
    @staticmethod
    def from_object( object: dict ):
        id = str(object.get( "_id" )).strip() if object.get("_id") is not None else str(object.get( "id" )).strip()
        type = str( object.get( "type" )).strip()
        description = str( object.get( "description" )).strip()
        product = str( object.get( "product" )).strip()
        quantity = int( object.get( "quantity" ))
        user = str( object.get( "user" )).strip()
        created_at = str( object.get("created_at"))
                
        return HistoryEntity( id, type, description, product, quantity, user, created_at )
    
    @staticmethod
    def from_array( objects_array: list ) -> list :
        histories = []
        for object in objects_array:
            history = HistoryEntity.from_object( object )
            histories.append( history.to_object() )
            
        return histories
        
    
    def to_object( self ) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "product": self.product,
            "quantity": self.quantity,
            "user": self.user,
            "created_at": self.created_at,
        }