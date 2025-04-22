from flask import redirect, render_template, request, url_for, session
from app.domain.dtos.auth.AuthLoginDTO import AuthLoginDTO
from app.presentation.services.AuthService import AuthService

class AuthController:
    __authService: AuthService
    
    
    def __init__(self, authService: AuthService ):
        self.__authService = authService
        
    
    def index( self ):
        return render_template("/auth/login.html")

    def login( self ):
        [ error, authLogiDto] = AuthLoginDTO.login( request.get_json() )
        if error:
            return { "code": 400, "status": "Bad Request", "msg": error }
        
        resp = self.__authService.login( authLogiDto )
        if resp.get("status") == "not found":
            return resp
        
        session["user"] = resp.get("user")
        return redirect( url_for( resp.get("url")))
    
    
    def logout( self ):
        del session["user"]
        return redirect( url_for("index.auth.index") )
