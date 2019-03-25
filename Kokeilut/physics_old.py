from PyQt5.Qt import QTransform, QPointF

class Physics():
    
    def __init__(self):
        self.g = 0.0
    
    def check_collision_up(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(3.0, 9.0)
        pos2 = pos + QPointF(29.0, 9.0)
        
        item1 = scene.itemAt(pos1,transform)
        item2 = scene.itemAt(pos2,transform)
        
        if item1 is None and item2 is None:
            return False
        elif item1 is not None:
            if item1.is_collidable():
                return True
        elif item2 is not None:
            if item2.is_collidable():
                return True
        else:
            return False
    
    def check_collision_down(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(3.0,32.0)
        pos2 = pos + QPointF(29.0,32.0)
        
        item1 = scene.itemAt(pos1,transform)
        item2 = scene.itemAt(pos2,transform)
        
        if item1 is None and item2 is None:
            return False
        
        elif item1 is not None:
            if item1.is_collidable():
                return True
            
        elif item2 is not None:
            if item2.is_collidable():
                return True
            
        else:
            return False
        
    def check_collision_left(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(2.0,10.0)
        pos2 = pos + QPointF(2.0,31.0)
        
        item1 = scene.itemAt(pos1,transform)
        item2 = scene.itemAt(pos2,transform)
        
        if item1 is None and item2 is None:
            return False
        elif item1 is not None:
            if item1.is_collidable():
                return True
        elif item2 is not None:
            if item2.is_collidable():
                return True
        else:
            return False
           
    def check_collision_right(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(30.0,10.0)
        pos2 = pos + QPointF(30.0,31.0)
        
        item1 = scene.itemAt(pos1,transform)
        item2 = scene.itemAt(pos2,transform)
        
        if item1 is None and item2 is None:
            return False
        elif item1 is not None:
            if item1.is_collidable():
                return True
        elif item2 is not None:
            if item2.is_collidable():
                return True
        else:
            return False
        
    def reset_gravity(self):
        self.g = 0.0
        return 0
    
    def gravity(self,v):
        
        self.g -= 0.1
        
        v += self.g
        
        return v
        