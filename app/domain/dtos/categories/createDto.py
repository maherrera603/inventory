from datetime import datetime

class AddCategoryDTO:

    def __init__(self, category, status, user=None):
        self.category = category
        self.status = status
        self.user = user
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    @staticmethod
    def create( data: dict ):
        category = data.get( "category", None)
        status = data.get( "status", None )

        if len( category ) < 3 : return [ "La categoria debe tener mas de 3 caracteres", None]

        if not status.lower() in  [ "active", "inactive"]: return [ "Seleccione el estado de la categoria", None ]

        return [ None, AddCategoryDTO( category=category, status=status )]

    def to_object( self ):
        return {
            "category": self.category,
            "status": self.status,
            "user": self.user,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
