from bson.objectid import ObjectId
from datetime import datetime

class ProductCreateDTO:

    def __init__(self, name: str, sku: int, category: str, quantity: int, price: float, status: str, user: ObjectId = None):
        self.name = name
        self.sku = sku
        self.category = category
        self.quantity = quantity
        self.price = price
        self.status = status
        self.user = user
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()


    @staticmethod
    def create( data: dict ):
        name = str( data.get( "name" ) ).strip()
        sku = str( data.get("sku") ).strip()
        category = str(data.get( "category" )).strip()
        quantity = str( data.get( "quantity") ).strip()
        price = str( data.get( "price") ).strip()
        status = str( data.get( "status" ) ).strip()


        if len( name) < 3: return [ "el nombre del producto debe tener mas de 3 caracteres", None ]

        if len( sku ) > 10 or len( sku) < 10: return [ "el sku debe contener 10 digitos", None ]

        if len(category) < 1  : return [ "Seleccione una categoria", None ]

        if int( quantity ) < 1 : return ["la cantidad del producto debe ser mayor a 1", None ]

        if float( price ) < 50: return [ "el precio debe ser mayor a 50", None ]

        if not status.lower() in [ "available", "exhausted" ]: return [ "Seleccione el estado del producto", None]

        return [ None, ProductCreateDTO( name, int(sku), category, int(quantity), float(price), status)]

    def to_object( self ):
        return {
            "name": self.name,
            "sku": self.sku,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status,
            "user": self.user,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
