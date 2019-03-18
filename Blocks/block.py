from PyQt5.QtWidgets import QGraphicsPixmapItem


class Block(QGraphicsPixmapItem):
    
    def __init__(self, collision = True, obstacle = False, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.collision = collision
        self.pickable = False
        self.obstacle = obstacle
        
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
        
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision
        
    def is_pickable(self):
        if self is None:
            return False
        else:
            return self.pickable
        
    def is_obstacle(self):
        if self is None:
            return False
        else:
            return self.obstacle
        
    def stand_on_effect(self,player):
        
        pass
        
    def obstacle_effect(self,player,scene):
        
        pass