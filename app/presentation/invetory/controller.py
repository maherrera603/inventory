from flask import render_template, session
from app.presentation.services.inventaryService import InventaryService

class InventoryController:
    _inventaryService: InventaryService

    def __init__(self, inventaryService: InventaryService ):
        self.data = { "user": {} }
        self._inventaryService = inventaryService   

    
    def index( self ):
        self.data["user"] = session["user"]
        self.data["count"] = self._inventaryService.get_registers()
        return render_template("/inventory/index.html", data=self.data );
