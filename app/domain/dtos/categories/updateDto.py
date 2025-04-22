from bson.objectid import ObjectId
from datetime import datetime

class UpdateCategoryDTO:
    
    def __init__(self, id: str, category: str, status: str ):
        self.id = id
        self.category = category
        self.status = status
        self.updated_at = datetime.now().isoformat()
    
    @staticmethod
    def update( object: dict ) -> list:
        id = object.get( "id" )
        category = object.get( "category" )
        status = object.get( "status" )
        
        
        
        if len( category ) < 3 : return [ "La categoria debe tener mas de 3 caracteres", None]
        
        if not status.lower() in  [ "active", "inactive"]: return [ "Seleccione el estado de la categoria", None ]
        return [ None, UpdateCategoryDTO( id, category, status ) ]
    
    def to_object( self ) -> dict:
        return {
            "id": self.id,
            "category": self.category,
            "status": self.status,
            "updated_at": self.updated_at
        }