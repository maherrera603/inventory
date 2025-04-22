from datetime import datetime

class HistoryCreateDTO:
    
    def __init__(self, product: str, user: str, type: str, quantity: int, description: str):
        self.product = product
        self.user = user
        self.type = type
        self.quantity = quantity
        self.description = description
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        
    
    @staticmethod
    def from_object( object: dict ) -> list:
        product = str(object.get( "id" )).strip()
        user = str( object.get( "user" )).strip()
        type = str( object.get( "type" )).strip()
        quantity = int( object.get( "quantity" ))
        description = str( object.get( "description" )).strip()
        
        if len( product ) < 1: return [ "el id del producto es invalido", None ]
        
        if len( user ) < 1 : return [ "el iddel usuario es invalido", None ]
        
        if type is None: return [ "seleccione el tipo de movimiento que realizo", None ]
        
        if quantity < 1: return [ "ingrese la cantidad que aumento al producto", None ]
        
        if  len( description) < 10:  return [ "Ingrese una descripcion mas detallada del moviento", None]
        
        return [ None, HistoryCreateDTO( product, user, type, quantity, description ) ]
    
    def to_object( self ) -> dict:
        return {
            "product": self.product,
            "user": self.user,
            "type": self.type,
            "quantity": self.quantity,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }