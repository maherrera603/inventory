from flask import Blueprint
from app.presentation.history.controller import HistoryController
from app.data.mongo.database import DatabaseConnection
from app.infrastructure.datasource.mongo.historyDatasourceImp import HistoryDatasourceImp
from app.infrastructure.repositories.historyRepositoryImp import HistoryRepositoryImp
from app.infrastructure.datasource.mongo.productDatasourceImp import ProductDatasourceImp
from app.infrastructure.repositories.productRepositoryImp import ProductRepositoryImp
from app.infrastructure.datasource.mongo.categoryDatasourceImpl import CategoryDatasourceImp
from app.infrastructure.repositories.categoryRepositoryImp import CategoryRepositoryImp
from app.presentation.services.historyService import HistoryService
from app.presentation.services.productService import ProductService
from app.presentation.services.CategoryService import CategoryService

class HistoryRoutes:
    
    @staticmethod
    def routes():
        
        database = DatabaseConnection()
        
        # datasources
        historyDatasource = HistoryDatasourceImp( database )
        productDatasource = ProductDatasourceImp( database )
        categoryDatasource = CategoryDatasourceImp( database )
        
        # repositories
        historyRepository = HistoryRepositoryImp( historyDatasource )
        productRepository = ProductRepositoryImp( productDatasource )
        categoryRepository = CategoryRepositoryImp( categoryDatasource )
        
        # services
        historyService = HistoryService( historyRepository, productRepository, categoryRepository )
        productService = ProductService( productRepository, categoryRepository )
        categoryService = CategoryService( categoryRepository )
        
        controller = HistoryController( historyService, productService, categoryService )
        
        routes: Blueprint = Blueprint("history", __name__, url_prefix="/inventario/historial")
        routes.add_url_rule("/", view_func=controller.index, methods=["GET"])
        routes.add_url_rule("/save", view_func=controller.save_history, methods=["POST"])
        routes.add_url_rule("/historia/<string:id>", view_func=controller.show, methods=["GET"])
        return routes