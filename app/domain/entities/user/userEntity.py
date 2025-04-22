class UserEntity:
    
    def __init__(self, id, name, lastname, idnumber, phone, email, password, role ):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.idnumber = idnumber
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role
    
    @staticmethod
    def from_object( object: dict ):
        id = str(object.get( "_id" )) if object.get("_id") is not None else object.get("id")
        name = object.get("name")
        lastname = object.get( "lastname" )
        idnumber = object.get( "idnumber" )
        phone = object.get( "phone" )
        email = object.get( "email" )
        password = object.get( "password")
        role = object.get( "role" )
        return UserEntity( id, name, lastname, idnumber, phone, email, password, role )
    
    def to_object( self ):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "idnumber": self.idnumber,
            "phone": self.phone,
            "email": self.email,
            "role": self.role
        }
        
        