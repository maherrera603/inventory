from app.domain.respositories.productRepository import ProductRepository
from app.domain.respositories.categoryRepository import CategoryRespository
from app.domain.entities.product.productEntity import ProductEntity
from app.domain.dtos.products.ProductCreateDTO import ProductCreateDTO
from app.domain.dtos.products.productUpdateDTO import ProductUpdateDTO


class ProductService:
    _productRepository: ProductRepository
    _categoryRepository: CategoryRespository
    
    
    def __init__(self, productRepository: ProductRepository, categoryRepository: CategoryRespository ):
        self._productRepository = productRepository
        self._categoryRepository = categoryRepository
        
    def all_products( self ):
        products_db = self._productRepository.find()
        products =  ProductEntity.from_array( products_db )
        return products
    
    def find_product( self, id):
        try:
            data = self._productRepository.find_one( id )
            if data is None:
                return { "code": 404, "status": "Not Found", "redirect": "index.products.index" }

            product = ProductEntity.from_object( data )
            return product.to_object()
        except:
            return { "code": 500, "status": "Internal Server", "redirect": "index.products.index" }
    
    def create_product( self, productCreateDto: ProductCreateDTO ):
        try:

            exists = self._productRepository.find_by_sku(productCreateDto.sku )
            if exists:
                return {"code": 400, "status" : "Bad Request", "msg": "El producto con el sku ya existe"}
            
            resp = self._productRepository.create( productCreateDto )
            if resp is False:
                return { "code": 500, "status": "Interna Server", "msg": "Ha ocurrido un error" }
            
            return { "code" : 200, "status": "Created", "msg": "el producto ha sido creado"}            
            
        except Exception as error:
            return { "code": 500, "status": "Internal Server", "redirect": "index.products.index" }
        
    def update_product( self, id: str, productUpdateDto: ProductUpdateDTO ):
        try:
            product = self._productRepository.find_one( id )
            if product is None:
                return { "code": 404, "status": "Not Found", "msg": "El producto no existe"}
            
            product = self._productRepository.update( id, productUpdateDto)
            print( product )
            if product is None:
                return { "code": 500, "status": "Internal Server", "msg": "Ha ocurrido un error"}
            
            update_product = ProductEntity.from_object( product )
            
            return { 
                "code": 201, 
                "status":"created", 
                "msg": "Producto actualizado correctamente!!!", 
                "product": update_product.to_object() 
            }
        except:
            return { "code": 500, "status": "Internal Server", "msg": "Ha ocurrido un error"}
        
    def delete_product( self, id: str ):
        try:
            product = self._productRepository.find_one( id )
            if product is None:
                return { "code": 404, "status": "Not Found", "msg": "product no existe"}
            
            result = self._productRepository.delete(id)
            if result is False:
                return { "code": 500, "status": "Internal Server", "msg": "Ha ocurrido un error"}
                
            return { "code": 204, "status":"no content", "msg": "Producto eliminado correctamente!!!"}
        except: 
            return { "code": 500, "status": "Internal Server", "msg": "Ha ocurrido un error"}