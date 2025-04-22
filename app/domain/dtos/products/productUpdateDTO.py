from datetime import datetime

class ProductUpdateDTO:
    
    def __init__(self, id: str, name: str, category: str, quantity: int, price: float, status: str, user: str = None):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.status = status
        self.user = user
        self.updated_at = datetime.now().isoformat()
    
    @staticmethod
    def update( object: dict ):
        id = str( object.get( "id" ))
        name = str( object.get( "name" ) ).strip()
        sku = str( object.get("sku") ).strip()
        category = str(object.get( "category" ))
        quantity = str( object.get( "quantity") ).strip()
        price = str( object.get( "price") ).strip()
        status = str( object.get( "status" ) ).strip()


        if len( name) < 3: return [ "el nombre del producto debe tener mas de 3 caracteres", None ]

        if len( sku ) > 10 or len( sku) < 10: return [ "el sku debe contener 10 digitos", None ]

        if len(category) < 1 : return [ "Seleccione una categoria", None ]

        if int( quantity ) < 1 : return ["la cantidad del producto debe ser mayor a 1", None ]

        if float( price ) < 50: return [ "el precio debe ser mayor a 50", None ]

        if not status.lower() in [ "available", "exhausted" ]: return [ "Seleccione el estado del producto", None]

        return [ None, ProductUpdateDTO( id, name, category, int(quantity), float(price), status)]
    
    def to_object( self ):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "user": self.user,
            "status": self.status,
            "updated_at": self.updated_at
        }
        