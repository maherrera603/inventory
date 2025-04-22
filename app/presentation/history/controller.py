from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session
from app.domain.dtos.history.historyCreateDTO import HistoryCreateDTO
from app.presentation.services.historyService import HistoryService
from app.presentation.services.productService import ProductService
from app.presentation.services.CategoryService import CategoryService


class HistoryController: 
    _data: dict
    _historyService: HistoryService
    _productService: ProductService
    _categoryService: CategoryService
   
    
    def __init__(
        self,
        historyService: HistoryService,
        productService: ProductService,
        categoryService: CategoryService
    ):
        self._data= {}
        self._historyService = historyService
        self._productService = productService
        self._categoryService = categoryService
        
    
    
    def index( self ):
        self._data["user"] = session["user"]
        self._data["histories"] = self._historyService.all_histories()
        return render_template("/history/histories.html", data=self._data)
        
    def save_history( self ):
        [ error, historyCreateDto ] = HistoryCreateDTO.from_object( request.get_json() )
        if error:
            return { "code": 400, "status": "Bad Request", "msg": error}
        
        resp = self._historyService.create_history( historyCreateDto )
        if resp["code"] != 201: 
            return resp
        
        return redirect( url_for( "index.products.index" ))
    
    def show( self, id: str ):
        self._data["user"] = session.get("user")
        
        history = self._historyService.find_historie( id )
        if "code" in history:
            return redirect( url_for("index.history.index"))
        
        product = self._productService.find_product( history.get("product") )
        if "code" in product:
            return redirect( url_for("index.history.index"))
        
        category = self._categoryService.find_categorie( product.get("category") )
        if "code" in category:
            return redirect( url_for("index.history.index"))
        
        self._data["history"] = history
        self._data["product"] = product
        self._data["category"] = category
        return render_template("/history/show.html", data=self._data )
        