from PyQt5.Qt import QGraphicsPixmapItem, QPixmap
from .item import Item


class Heart(Item):
    
    def __init__(self, parent=None):
        
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Heart.png"))
        self.collision = False
        
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision
        
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        pass