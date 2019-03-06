from PyQt5.QtWidgets import QGraphicsPixmapItem


class Item(QGraphicsPixmapItem):
    
    def __init__(self, collision = False, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision