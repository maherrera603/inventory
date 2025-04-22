from app.domain.entities.history.historyEntity import HistoryEntity
from app.domain.dtos.history.historyCreateDTO import HistoryCreateDTO
from app.domain.respositories.historyRepository import HistoryRepository
from app.domain.respositories.productRepository import ProductRepository
from app.domain.respositories.categoryRepository import CategoryRespository


class HistoryService:
    _historyRepository: HistoryRepository
    _productRepository: ProductRepository
    _categoryRepository: CategoryRespository
    
    def __init__(self, 
        historyRespository: HistoryRepository, 
        productRepository: ProductRepository,
        categoryRepository: CategoryRespository
    ):
        self._historyRepository = historyRespository
        self._productRepository = productRepository
        self._categoryRepository = categoryRepository
        
    def all_histories( self ):
        histories_db = self._historyRepository.find()
        histories = HistoryEntity.from_array( list( histories_db ))
        return histories
    
    def find_historie( self, id: str ):
        history_db = self._historyRepository.find_one( id )
        if history_db is None:
            return { "code": 404, "status": "Not Found", "msg": "la historia no existe"}
        
        history = HistoryEntity.from_object( history_db )
        return history.to_object()
    
    def create_history(self, historyCreateDto: HistoryCreateDTO ):
        try:
            resp = self._historyRepository.create( historyCreateDto )
            if resp is False:
                return { "code": 400, "status": "Bad Request", "msg": "Se ha generado un error"}
            
            return { "code": 201, "status": "Created", "msg": "el usuario"}
        except Exception as error:
            return { "code": 500, "status": "Internal Server", "msg": "se ha generado un error" }
        