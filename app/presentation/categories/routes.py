from flask import Blueprint
from app.presentation.categories.controller import CategoryController
from app.data.mongo.database import DatabaseConnection
from app.infrastructure.datasource.mongo.categoryDatasourceImpl import CategoryDatasourceImp
from app.infrastructure.repositories.categoryRepositoryImp import CategoryRepositoryImp
from app.presentation.services.CategoryService import CategoryService

class CategorieRouter:
    
    @staticmethod
    def routes() -> Blueprint:
        database = DatabaseConnection()
        
        # datasources
        categoryDatasource = CategoryDatasourceImp( database )
        
        # repositories
        categoryRepository = CategoryRepositoryImp( categoryDatasource )
        
        # services
        categoryService = CategoryService( categoryRepository )
        controller = CategoryController( categoryService )
        
        
        routes: Blueprint = Blueprint("categories", __name__, url_prefix="/inventario/categorias")
        routes.add_url_rule("/", view_func=controller.index, methods=["GET"])
        routes.add_url_rule("/agregar", view_func=controller.add, methods=["GET"])
        routes.add_url_rule("/save", view_func=controller.save_category, methods=["POST"])
        routes.add_url_rule("/actualizar/<string:id>", view_func=controller.show, methods=["GET"])
        routes.add_url_rule("/update", view_func=controller.update_category, methods=["POST"])
        routes.add_url_rule("/eliminar/<string:id>", view_func=controller.delete, methods=["GET"])
        return routes
        