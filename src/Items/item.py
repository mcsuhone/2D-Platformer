from PyQt5.QtWidgets import QGraphicsPixmapItem


class Item(QGraphicsPixmapItem):
    
    def __init__(self, collision = False, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.collision = collision
        self.GUIitem = False
        
    def set_pos(self,x,y):
        self.setPos(x*32,y*32)
        
    def set_GUIitem(self, value):
        
        self.GUIitem = value
        
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision
        
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        pass