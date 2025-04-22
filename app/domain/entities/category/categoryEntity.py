class CategoryEntity:

    def __init__(self, id: str, category: str, status: str ):
        self.id = id
        self.category = category
        self.status = status

    @staticmethod
    def from_object( object: dict ):
        id = str(object.get("_id")) if object.get("_id") is not None else str(object.get("id"))
        category = object["category"]
        status = object["status"]
        return CategoryEntity( id, category, status )


    @staticmethod
    def from_array( data: list ) -> list: 
        categories = []
        for category in data:
            category_class = CategoryEntity.from_object( category )
            categories.append( category_class.to_object() )
        return categories

    def to_object( self ):
        return {
            "id": self.id,
            "category": self.category,
            "status": self.status
        }
