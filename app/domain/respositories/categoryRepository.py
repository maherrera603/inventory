from abc import ABC, abstractmethod
from app.domain.dtos.categories.createDto import AddCategoryDTO
from app.domain.dtos.categories.updateDto import UpdateCategoryDTO
from app.domain.entities.category.categoryEntity import CategoryEntity

class CategoryRespository( ABC ):
    
    @abstractmethod
    def create( self, addCategoryDto: AddCategoryDTO ) -> bool : ...
    
    @abstractmethod
    def find( self ) -> list[ CategoryEntity ]: ...
    
    @abstractmethod
    def find_one( self, id: str ) -> dict[ CategoryEntity ]: ...
    
    @abstractmethod
    def find_category( self, category: str ) -> dict: ...
    
    @abstractmethod
    def update( self, id: str, updateDto: UpdateCategoryDTO ) -> dict: ...
    
    @abstractmethod
    def delete( self, id: str ) -> dict: ... 
    
    
    @abstractmethod
    def count_registers( self ) -> int: ...