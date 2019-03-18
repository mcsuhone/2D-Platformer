from PyQt5.Qt import QTransform, QPointF

class Physics():
    
    def __init__(self):
        self.g = 0.0
        self.v = 0.0
    
    def check_collisions_x(self,player,scene,dx):
        if dx > 0:
            #tests right side collision
            transform = QTransform()
            pos = player.pos()
            posright1 = pos + QPointF(27.0+dx,9.0)
            posright2 = pos + QPointF(27.0+dx,31.0)
            
            item1 = scene.itemAt(posright1,transform)
            item2 = scene.itemAt(posright2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return item1.x()-player.x()-28
                    
            if item2 is not None:
                if item2.is_collidable():
                    return item2.x()-player.x()-28
                    
            if item1 is not None or item2 is not None:
                return None
            
        elif dx < 0:
            #tests left side collision
            transform = QTransform()
            pos = player.pos()
            posleft1 = pos + QPointF(5.0+dx,9.0)
            posleft2 = pos + QPointF(5.0+dx,31.0)
            
            item1 = scene.itemAt(posleft1,transform)
            item2 = scene.itemAt(posleft2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return -(player.x()-item1.x()-28)
                    
            if item2 is not None:
                if item2.is_collidable():
                    return -(player.x()-item2.x()-28)
                    
            if item1 is not None or item2 is not None:
                return None
            
        else:
            return 0
        
    def check_collisions_y(self,player,scene,dy):
        
        if dy < 0:
            #tests bottom of player collision
            transform = QTransform()
            pos = player.pos()
            posdown1 = pos + QPointF(5.0,31.0-dy)
            posdown2 = pos + QPointF(27.0,31.0-dy)
            
            item1 = scene.itemAt(posdown1,transform)
            item2 = scene.itemAt(posdown2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item2 is not None:
                if item2.is_collidable():
                    return -(item2.y()-player.y()-32)
                
            if item1 is not None:
                if item1.is_collidable():
                    return -(item1.y()-player.y()-32)
               
            if item1 is not None or item2 is not None:
                return None
            
        elif dy > 0:
            #test top of player collisions
            transform = QTransform()
            pos = player.pos()
            posup1 = pos + QPointF(5.0,9.0-dy)
            posup2 = pos + QPointF(27.0,9.0-dy)
            
            item1 = scene.itemAt(posup1,transform)
            item2 = scene.itemAt(posup2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return 0
                    
            if item2 is not None:
                if item2.is_collidable():
                    return 0
                    
            if item1 is not None or item2 is not None:
                return None
            
        else:
            return None
    
        
    def reset_gravity(self):
        self.g = 0.0
        self.v = 0.0
    
    def gravity(self):
        
        self.g += 0.01
        if self.v <= 32.0:
            self.v += self.g
        
        return self.v
        