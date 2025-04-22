from flask import redirect, render_template, url_for
from flask import request
from flask import session
from app.domain.dtos.products.ProductCreateDTO import ProductCreateDTO
from app.domain.dtos.products.productUpdateDTO import ProductUpdateDTO
from app.presentation.services.productService import ProductService
from app.presentation.services.CategoryService import CategoryService


class ProductController:
    _productService: ProductService
    _categorieService: CategoryService
    data: dict
    
    def __init__(self, productService: ProductService, categoryService: CategoryService ):
        self._productService = productService
        self._categorieService = categoryService
        self.data = { "user": {} }


    def index( self ):
        self.data["user"] = session["user"]
        self.data["products"] = self._productService.all_products()
        return render_template("/products/products.html", data=self.data )


    def add( self ):
        self.data["title_page"] = "Agregar"
        self.data["user"] = session["user"]
        self.data["product"] = {}
        self.data["categories"] = self._categorieService.all_categories()
        return render_template("/products/agregar.html", data=self.data)

    def save_product( self ):
        [ error, productCreateDto ] = ProductCreateDTO.create( request.get_json() )
        if error:
            return { "code": 400, "status": "Bad Request", "msg": error }

        productCreateDto.user = session["user"]["id"]
        resp = self._productService.create_product( productCreateDto )
        return resp

    def show( self, id ):
        self.data["title_page"] = "Actualizar"
        self.data["user"] = session["user"]
        product = self._productService.find_product( id )
        if "redirect" in product:
            return redirect( url_for( product.get("redirect") ) )
        
        self.data["categories"] = self._categorieService.all_categories()
        self.data["product"] = product
        return render_template("/products/agregar.html", data=self.data)
    
    def update( self ):
        [ error, productUpdateDto ] = ProductUpdateDTO.update( request.get_json() )
        if error:
            return { "code": 400, "status": "Bad Request", "msg": error }
        
        productUpdateDto.user = session["user"]["id"]
        resp = self._productService.update_product( productUpdateDto.id, productUpdateDto )
        if resp["code"] != 201:
            return resp
        
        return resp
    
    def delete( self, id ):
        self._productService.delete_product( id )
        return redirect( url_for( "index.products.index" ))
        


