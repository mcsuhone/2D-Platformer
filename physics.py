from PyQt5.Qt import QTransform, QPointF

class Physics():
    
    def __init__(self):
        self.g = 0.0
    
    def check_collision_up(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(0.0, 0.0)
        pos2 = pos + QPointF(31.0, 0.0)
        
        itemunder1 = scene.itemAt(pos1,transform)
        itemunder2 = scene.itemAt(pos2,transform)
        
        if itemunder1 != None or itemunder2 != None:
            return True
        else:
            return False
    
    def check_collision_down(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(0.0,32.0)
        pos2 = pos + QPointF(31.0,32.0)
        
        itemunder1 = scene.itemAt(pos1,transform)
        itemunder2 = scene.itemAt(pos2,transform)
        
        if itemunder1 != None or itemunder2 != None:
            return True
        else:
            return False
    
    def check_collision_left(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(-2.0,4.0)
        pos2 = pos + QPointF(-2.0,29.0)
        
        itemunder1 = scene.itemAt(pos1,transform)
        itemunder2 = scene.itemAt(pos2,transform)
        
        if itemunder1 != None or itemunder2 != None:
            return True
        else:
            return False
           
    def check_collision_right(self,player,scene):
        
        transform = QTransform()
        pos = player.pos()
        pos1 = pos + QPointF(32.0,4.0)
        pos2 = pos + QPointF(32.0,29.0)
        
        itemunder1 = scene.itemAt(pos1,transform)
        itemunder2 = scene.itemAt(pos2,transform)
        
        if itemunder1 != None or itemunder2 != None:
            return True
        else:
            return False
        
    def reset_gravity(self):
        self.g = 0.0
        return 0
    
    def gravity(self,v):
        
        self.g -= 0.05
        
        v += self.g
        
        return v
        