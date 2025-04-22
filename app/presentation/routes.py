from flask import Blueprint
from app.presentation.auth.routes import AuthRoutes
from app.presentation.invetory.routes import InventoryRoute
from app.presentation.products.routes import ProductRoutes
from app.presentation.categories.routes import CategorieRouter
from app.presentation.history.routes import HistoryRoutes

class AppRoutes:

    @staticmethod
    def routes() -> Blueprint:
        bp = Blueprint( name='index', import_name=__name__, url_prefix="/")
        
        
        bp.register_blueprint( blueprint=AuthRoutes.routes() )
        bp.register_blueprint( blueprint=InventoryRoute.routes() )
        bp.register_blueprint( blueprint=ProductRoutes.routes() )
        bp.register_blueprint( blueprint=CategorieRouter.routes() )
        bp.register_blueprint( blueprint=HistoryRoutes.routes() )
        return bp
