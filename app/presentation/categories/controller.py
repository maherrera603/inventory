from  flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for


from app.domain.dtos.categories.createDto import AddCategoryDTO
from app.domain.dtos.categories.updateDto import UpdateCategoryDTO
from app.presentation.services.CategoryService import CategoryService


class CategoryController:
    _categoryService: CategoryService
    
    def __init__(self, categoryService: CategoryService ):
        self._categoryService = categoryService
        self.data = { "user": {} }
        
    
    def index( self ):
        self.data["user"] = session["user"]
        self.data["categories"] = self._categoryService.all_categories()
        return render_template("/categories/categories.html", data=self.data)
    
    def add( self ):
        self.data["user"] = session["user"]
        self.data["category"] = {}
        self.data["action_title"] = "Agregar"
        return render_template("/categories/add.html", data=self.data)
    
    def save_category( self ):
        [ error, addCategoryDto ] = AddCategoryDTO.create( request.get_json() )
        if error:
            return { "code": 400, "status": "Bad Request", "msg": error}
        
        addCategoryDto.user = session["user"]["id"]
        
        resp = self._categoryService.create_category( addCategoryDto )
        return resp
    
    def show( self, id ):
        self.data["user"] = session["user"]
        self.data["action_title"] = "Actualizar"
        category = self._categoryService.find_categorie( id )
        if "redirect" in category:
            return redirect( url_for( category["redirect"] ))
        
        self.data["category"] = category
        return render_template("/categories/add.html", data=self.data )
    
    def update_category( self ):
        [ error, updateCategoryDto] = UpdateCategoryDTO.update( request.get_json() )
        if error:
            return { "code": 400, "status": "bad request", "msg": error }
        
        resp = self._categoryService.update_category( updateCategoryDto.id, updateCategoryDto )
        if resp.get("code") != 201:
            return resp
        
        return redirect( url_for( "index.categories.index" ))
    
    def delete( self, id ):
        resp = self._categoryService.delete_category( id )
        if resp["code"] != 204:
            return redirect( url_for( resp["redirect"] ))
        
        return redirect( url_for( "index.categories.index"))