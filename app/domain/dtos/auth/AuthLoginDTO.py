import re

class AuthLoginDTO:
    
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
    
    
    @staticmethod
    def login( data: dict ):
        email = str( data.get( "email" )).strip()
        password = str( data.get( "password" )).strip()
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        if re.match( pattern, email) is None:  return [ "formato de email incorrecto", None ]
        
        if len( password ) < 8 or len( password ) > 12: return [ "la contraseña debe contener 8 a 12 caracteres", None]
        
        return [ None, AuthLoginDTO( email, password )]