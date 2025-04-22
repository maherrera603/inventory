from abc import ABC, abstractmethod
from app.domain.entities.history.historyEntity import HistoryEntity
from app.domain.dtos.history.historyCreateDTO import HistoryCreateDTO

class HistoryDatasource:
    
    @abstractmethod
    def find( self ) -> list[ HistoryEntity ]: ...
    
    @abstractmethod
    def find_one( self, id: str) -> dict[HistoryEntity]: ...
    
    @abstractmethod
    def create( self, historyCreateDto: HistoryCreateDTO ): ...
    
    @abstractmethod
    def count_registers( self ) -> int: ...