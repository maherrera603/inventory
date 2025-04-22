from abc import ABC, abstractmethod
from app.domain.entities.product.productEntity import ProductEntity
from app.domain.dtos.products.ProductCreateDTO import ProductCreateDTO
from app.domain.dtos.products.productUpdateDTO import ProductUpdateDTO


class ProductRepository( ABC ):
    
    @abstractmethod
    def find( self )-> list[ ProductEntity] : ...
    
    @abstractmethod
    def find_one( self, id: str ) -> dict[ ProductEntity ]: ...
    
    @abstractmethod
    def find_by_sku( self, sku: int) -> dict : ...
    
    @abstractmethod
    def create( self, productCreateDto: ProductCreateDTO ) -> dict : ...
    
    @abstractmethod
    def update( self, id: str, productUpdateDto: ProductUpdateDTO ) -> dict : ...
    
    @abstractmethod
    def delete( self, id: str) -> dict: ...
    
    @abstractmethod
    def count_registers( self ) -> int: ...