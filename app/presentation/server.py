import os
from flask import Flask
from app.presentation.routes import AppRoutes
from app.config.envs import Envs
from app.presentation.middlewares.authMiddleware import AuthMiddleware


class Server:
    _app: Flask
    envs: dict = Envs.get_envs()
    
    
    def __init__(self) -> None:
        self._app = Flask( __name__ )
        self._app.template_folder=os.path.abspath("views")
        self._app.static_folder=os.path.abspath("assets")
        self._app.secret_key = self.envs.get("WORD_SECRET_SESSION")
        self._app.config["SESSION_TYPE"] = "filesystem"
        AuthMiddleware( self._app )

        
    def load_routes( self ):
        self._app.register_blueprint( AppRoutes.routes() )

    def start( self ) -> None:
        self.load_routes()
        self._app.run( host="127.0.0.1", port=self.envs.get("PORT"), debug=True )


