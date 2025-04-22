from app.domain.respositories.categoryRepository import CategoryRespository
from app.domain.entities.category.categoryEntity import CategoryEntity
from app.domain.dtos.categories.createDto import AddCategoryDTO
from app.domain.dtos.categories.updateDto import UpdateCategoryDTO

class CategoryService:
    _categoryRepository: CategoryRespository
    
    def __init__(self, categoryRepository: CategoryRespository):
        self._categoryRepository = categoryRepository
        
    def all_categories( self ):
        categoriesList= self._categoryRepository.find()
        categories = CategoryEntity.from_array( list( categoriesList ) )
        return categories
    
    def find_categorie(self, id ):
        data = self._categoryRepository.find_one( id )
        if data is None:
            return { "code": 404, "status": "not found", "redirect": "index.categories.index" }
        
        category = CategoryEntity.from_object( data )
        return category.to_object()
    
    def create_category( self, addCategoryDto:AddCategoryDTO ):
        try:
            exists_category = self._categoryRepository.find_category( addCategoryDto.category )
            if exists_category:
                return { "code": 400, "status": "bad request", "msg": "la categoria ya existe"}
            
            result = self._categoryRepository.create( addCategoryDto )
            if result is False:
                return { "code": 500, "status": "internal server", "msg": "se ha generado un error !!"}
            
            return { "code": 201, "status": "created", "msg": "categoria ha sido creada !!"}
        except:
            return { "code": 500, "status": "internal server", "msg": "se ha generado un error !!"}
    
    def update_category(self, id: str, updateDto: UpdateCategoryDTO):
        try:
            category = self._categoryRepository.find_one( id )
            if category is None:
                return { "code": 404, "status": "Not Found", "msg": "la categoria no existe" }
            
            # TODO: validar que la categoria no exista
            result = self._categoryRepository.update( id, updateDto )
            
            if result is False:
                return { "code": 500, "status": "Internal Server", "msg": "Se ha producido un error" }
            
            return { "code": 201, "status": "Created" }
        except Exception as error:
            return { "code": 500, "status": "Internal Server", "msg": "Se ha producido un error" }

    def delete_category( self, id: str ):
        try:
            category = self._categoryRepository.find_one( id )
            if category is None:
                return { "code": 404, "status": "Not Found", "redirect": "index.categories.index"}
            
            delete = self._categoryRepository.delete( id )
            if delete is False:
                return { "code": 500, "status": "Internal Server Error", "redirect": "index.categories.index", "msg": "se ha generado un error"}
            
            return { "code": 204, "status": "Not Content", "msg": "categoria eliminada"}
        except:
            return { "code": 500, "status": "Internal Server Error", "redirect": "index.categories.index", "msg": "se ha generado un error"}
          
        
        