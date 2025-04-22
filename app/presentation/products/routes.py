from flask import Blueprint
from app.presentation.products.controller import ProductController
from app.infrastructure.datasource.mongo.categoryDatasourceImpl import CategoryDatasourceImp
from app.infrastructure.datasource.mongo.productDatasourceImp import ProductDatasourceImp
from app.infrastructure.repositories.categoryRepositoryImp import CategoryRepositoryImp
from app.infrastructure.repositories.productRepositoryImp import ProductRepositoryImp
from app.presentation.services.CategoryService import CategoryService
from app.presentation.services.productService import ProductService
from app.data.mongo.database import DatabaseConnection

class ProductRoutes:

    @staticmethod
    def routes() -> Blueprint:
        database: DatabaseConnection = DatabaseConnection()
        
        # datasources
        productDatasource = ProductDatasourceImp( database )
        categoryDatasource = CategoryDatasourceImp( database )
        
        # respositories
        productRepository = ProductRepositoryImp( productDatasource )
        categoryRepository = CategoryRepositoryImp( categoryDatasource )
        
        # services
        productService = ProductService( productRepository, categoryRepository)
        categoryService = CategoryService( categoryRepository)
        controller = ProductController( productService, categoryService )
        
        

        routes: Blueprint = Blueprint("products", __name__,url_prefix="/inventario/productos")
        routes.add_url_rule("/",  view_func=controller.index, methods=["GET"])
        routes.add_url_rule("/agregar", view_func=controller.add, methods=["GET"])
        routes.add_url_rule("/save", view_func=controller.save_product, methods=["POST"])
        routes.add_url_rule("/actualizar/<string:id>", view_func=controller.show, methods=["GET"])
        routes.add_url_rule("/update", view_func=controller.update, methods=["POST"])
        routes.add_url_rule("/eliminar/<string:id>", view_func=controller.delete, methods=["GET"])
        return routes;

