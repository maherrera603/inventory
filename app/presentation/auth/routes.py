from flask import Blueprint
from app.presentation.auth.controller import AuthController
from app.data.mongo.database import DatabaseConnection
from app.infrastructure.datasource.mongo.userDatasourceImp import UserDatasourceImp
from app.infrastructure.repositories.userRepositoryImp import UserRepositoryImp
from app.presentation.services.AuthService import AuthService

class AuthRoutes:

    @staticmethod
    def routes() -> Blueprint: 
        database =  DatabaseConnection()
        
        # datasources
        userDatasource = UserDatasourceImp( database )
        
        # repositories
        userRepository = UserRepositoryImp( userDatasource )
        
        # services
        authService = AuthService( userRepository )
        controller = AuthController( authService )
        

        routes: Blueprint = Blueprint("auth", __name__, url_prefix="/")
        routes.add_url_rule("/", view_func=controller.index, methods = ["GET"] )
        routes.add_url_rule("/login",  view_func=controller.login, methods=[ "POST" ])
        routes.add_url_rule("/salir", view_func=controller.logout, methods=["GET"])
        return routes
