from app.domain.respositories.userRepository import UserRepository
from app.domain.dtos.auth.AuthLoginDTO import AuthLoginDTO
from app.domain.entities.user.userEntity import UserEntity
from app.config.bcryptAdapter import BcryptAdapter

class AuthService:
    _userRepository: UserRepository
    
    def __init__(self, userRepository: UserRepository ):
        self._userRepository = userRepository
        
    def login( self, authLoginDto: AuthLoginDTO ):
        user = self._userRepository.find_user( authLoginDto.email )
        if not user:
            return { "code": 404, "status": "not found", "msg": "Correo y/o contraseña invalidas"}
        
        userEntity = UserEntity.from_object( user )
        validPwd = BcryptAdapter.verify_password( authLoginDto.password, userEntity.password )
        if validPwd is False:
            return { "code": 404, "status": "not found", "msg": "Correo y/o contraseña invalidas"}
        
        return { 
            "code": 200, 
            "status": "OK", 
            "msg": "Bienvenido",
            "user": userEntity.to_object(), 
            "url": "index.invetario.index"
        }
        