from flask import Blueprint
from app.data.mongo.database import DatabaseConnection
from app.infrastructure.datasource.mongo.categoryDatasourceImpl import CategoryDatasourceImp
from app.infrastructure.datasource.mongo.productDatasourceImp import ProductDatasourceImp
from app.infrastructure.datasource.mongo.historyDatasourceImp import HistoryDatasourceImp
from app.infrastructure.repositories.categoryRepositoryImp import CategoryRepositoryImp
from app.infrastructure.repositories.productRepositoryImp import ProductRepositoryImp
from app.infrastructure.repositories.historyRepositoryImp import HistoryRepositoryImp
from app.presentation.services.inventaryService import InventaryService
from app.presentation.invetory.controller import InventoryController


class InventoryRoute:

    @staticmethod
    def routes() ->Blueprint:
        
        database = DatabaseConnection()
        
        # datasources
        categoryDatasource = CategoryDatasourceImp( database )
        productDatasource = ProductDatasourceImp( database )
        historyDatasource = HistoryDatasourceImp( database )     
        
        # repositories
        categoryRepository = CategoryRepositoryImp( categoryDatasource )
        productRepository = ProductRepositoryImp( productDatasource )
        historyRepository = HistoryRepositoryImp( historyDatasource )
        
        
        inventaryService = InventaryService( categoryRepository, productRepository, historyRepository )
        controller = InventoryController( inventaryService )
        
        routes : Blueprint = Blueprint("invetario", __name__, url_prefix="/inventario")
        routes.add_url_rule("/", view_func=controller.index, methods=["GET"])
        return routes;
        