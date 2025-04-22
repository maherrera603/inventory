from bson.objectid import ObjectId

class ProductEntity:

    def __init__( self, id: str, name: str, sku: str, category: str, quantity: int, price: float, status: str, user: str ):
        self.id = id
        self.name = name
        self.sku = sku
        self.category = category
        self.quantity = quantity
        self.price = price
        self.status = status
        self.user = user

    @staticmethod
    def from_object( data: dict ):
        id = str( data.get("_id")) if data.get("_id") is not None else data.get("id")
        name = data.get("name")
        sku = data.get("sku")
        category =  str(data.get("category"))
        quantity = data.get("quantity")
        price = data.get("price")
        status = data.get("status")
        user = str(data.get("user"))
        
        return ProductEntity( id, name, sku, category, quantity, price, status, user )

    @staticmethod
    def from_array( data: list) -> list:
        products = []
        for product in data:
            product_dict = ProductEntity.from_object( product )
            products.append( product_dict.to_object() )
        return products

    def to_object( self ):
        return {
            "id": self.id,
            "name": self.name,
            "sku": self.sku,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status,
            "user": self.user
        }
