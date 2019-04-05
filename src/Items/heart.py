from PyQt5.Qt import QGraphicsPixmapItem, QPixmap
from .item import Item


class Heart(Item):
    
    def __init__(self, parent=None):
        
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Heart.png"))