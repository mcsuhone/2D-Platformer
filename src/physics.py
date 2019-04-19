from PyQt5.Qt import QTransform, QPointF, QGraphicsRectItem
from CONSTANTS import *
import Creatures

class Physics():
    
    def __init__(self, height = 22, width = 23, offset = 4, weight = 1.0):
        self.g = 0.0
        self.v = 0.0
        
        self.w,self.h = self.calculate_size(width, height)
        
        self.right_side = width + offset + 1
        self.left_side = offset
        self.top_side = self.calculate_top(height)
        self.bottom_side = self.calculate_bottom(height)
        
        self.weight = weight
        
    def calculate_size(self,width,height):
        
        w = width//32 + 1
        h = height//32 + 1
        
        return w,h
        
    def calculate_top(self,height):
        
        a = (height//32 + 1)*32
        
        return a - height - 1
        
    def calculate_bottom(self,height):
        
        a = (height//32 + 1)*32
        
        return a - 1
        
    def check_collisions_x(self,player,scene,dx):
        if dx > 0:
            #tests right side collision
            transform = QTransform()
            pos = player.pos()
            posright1 = pos + QPointF(self.right_side+dx,self.top_side)
            posright2 = pos + QPointF(self.right_side+dx,self.bottom_side)
            
            item1 = scene.itemAt(posright1,transform)
            item2 = scene.itemAt(posright2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return item1.X0()-player.x()-self.right_side
                    
            if item2 is not None:
                if item2.is_collidable():
                    return item2.X0()-player.x()-self.right_side
                    
            if item1 is not None or item2 is not None:
                return None
            
        elif dx < 0:
            #tests left side collision
            transform = QTransform()
            pos = player.pos()
            posleft1 = pos + QPointF(self.left_side+dx,self.top_side)
            posleft2 = pos + QPointF(self.left_side+dx,self.bottom_side)
            
            item1 = scene.itemAt(posleft1,transform)
            item2 = scene.itemAt(posleft2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return -(player.x()-item1.X0()-self.right_side+item1.right_side())
                    
            if item2 is not None:
                if item2.is_collidable():
                    return -(player.x()-item2.X0()-self.right_side+item2.right_side())
                    
            if item1 is not None or item2 is not None:
                return None
            
        else:
            return 0
        
    def check_collisions_y(self,player,scene,dy):
        
        if dy < 0:
            #tests bottom of player collision
            transform = QTransform()
            pos = player.pos()
            posdown1 = pos + QPointF(self.left_side,self.bottom_side-dy)
            posdown2 = pos + QPointF(self.right_side-1,self.bottom_side-dy)
            
            item1 = scene.itemAt(posdown1,transform)
            item2 = scene.itemAt(posdown2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item2 is not None:
                if item2.is_collidable():
                    return -(item2.Y0()-player.y()-32*self.h)
                
            if item1 is not None:
                if item1.is_collidable():
                    return -(item1.Y0()-player.y()-32*self.h)
               
            if item1 is not None or item2 is not None:
                return None
            
        elif dy > 0:
            #test top of player collisions
            transform = QTransform()
            pos = player.pos()
            posup1 = pos + QPointF(self.left_side,self.top_side-dy)
            posup2 = pos + QPointF(self.right_side-1,self.top_side-dy)
            
            item1 = scene.itemAt(posup1,transform)
            item2 = scene.itemAt(posup2,transform)
            
            if item1 is None and item2 is None:
                return None
                
            if item1 is not None:
                if item1.is_collidable():
                    return -(item1.Y0()-player.y()+(self.h*32-self.top_side))
                    
            if item2 is not None:
                if item2.is_collidable():
                    return -(item2.Y0()-player.y()+(self.h*32-self.top_side))
                    
            if item1 is not None or item2 is not None:
                return None
            
        else:
            return None
    
    def check_edge(self,enemy,scene):
        
        transform = QTransform()
        pos = enemy.pos()
        posdown1 = pos + QPointF(self.left_side,self.bottom_side+2)
        posdown2 = pos + QPointF(self.right_side,self.bottom_side+2)
        
        item1 = scene.itemAt(posdown1,transform)
        item2 = scene.itemAt(posdown2,transform)
        
        if item1 is None or item2 is None:
            return True
        else:
            return False
        
    def reset_gravity(self):
        self.g = 0.0
        self.v = 0.0
    
    def gravity(self):
        
        self.g += GRAVITY
        if self.v <= MAX_FALL_VELOCITY:
            self.v += self.g*self.weight
        
        return self.v
        