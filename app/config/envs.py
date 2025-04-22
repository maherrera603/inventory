from os import getenv
from dotenv import load_dotenv

class Envs:
    
    @staticmethod
    def get_envs() -> dict:
        load_dotenv()
        return {
            "PORT": int( getenv("PORT").__str__()) if getenv("PORT") else 8000,
            "URL_CONNECTION": getenv( "URL_CONNECTION"),
            "WORD_SECRET_SESSION": getenv( "WORD_SECRET_SESSION" ),
            "DB_NAME": getenv("DB_NAME"),
            "HOST": getenv("HOST"),
            "USER": getenv("USER"),
            "PASSWORD": getenv("PASSWORD"),
        }    