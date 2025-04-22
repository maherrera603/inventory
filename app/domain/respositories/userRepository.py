from abc import ABC, abstractmethod



class UserRepository( ABC):
    
    @abstractmethod
    def find_one( self, id: str ) -> dict: ...
    
    @abstractmethod
    def find_user( self, email: str  ) -> dict: ...
    
    