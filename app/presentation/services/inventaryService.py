from app.domain.respositories.categoryRepository import CategoryRespository
from app.domain.respositories.productRepository  import ProductRepository
from app.domain.respositories.historyRepository  import HistoryRepository

class InventaryService:
    _categoryRepository: CategoryRespository
    _productRepository: ProductRepository
    _historyRepository: HistoryRepository
    
    def __init__(
        self, 
        categoryRepository: CategoryRespository,
        productRepository: ProductRepository,
        historyRepository: HistoryRepository
    ):
        self._categoryRepository = categoryRepository
        self._productRepository = productRepository
        self._historyRepository = historyRepository
        
    def get_registers(self) -> dict:
        return {
            "category_count": self._categoryRepository.count_registers(),
            "product_count": self._productRepository.count_registers(),
            "history_count": self._historyRepository.count_registers()
        }
    
    