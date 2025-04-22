from flask import Flask
from flask import session, request
from flask import redirect, url_for

class AuthMiddleware:
    
    def __init__(self, app: Flask):
        app.before_request( self.check_session )
        self.public_paths = ['/', "/login" ]
        self.private_paths = [ "/inventario" ]
        self.public_prefix_paths = [ "/static/"]
        # app.after_request( self.not_authenticated )

    def check_session( self ):
        path = request.path
        is_authenticated = 'user' in session

        # Siempre permitir recursos estáticos
        if any(path.startswith(prefix) for prefix in self.public_prefix_paths):
            return

        # Si el usuario está autenticado e intenta acceder a ruta pública → redirigir a inventario
        if is_authenticated and path in self.public_paths:
            return redirect( url_for("index.invetario.index"))

        # Si la ruta es privada y no está autenticado → redirigir al login
        if any(path.startswith(prefix) for prefix in self.private_paths):
            if not is_authenticated:
                return redirect(url_for("index.auth.index"))

        # Si no está autenticado y quiere acceder a una pública exacta → permitir
        if not is_authenticated and path in self.public_paths:
            return

        # Para todo lo demás: permitir
        return
        
        
        
     
