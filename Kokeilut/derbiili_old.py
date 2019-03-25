from PyQt5.QtGui import QPixmap,QPainterPath
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics
from PyQt5.Qt import QTransform, QPointF

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, scene, x, y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        self.speed = 4
        self.jump_height = 10.0
        self.jump = False
        self.fall = False
        self.vy = 0.0
        self.counter = 0
        #Height = 22
        #Widght = 26
        
        self.scene = scene
        self.physics = Physics()
        
    def is_collidable(self):
        
        return self.collision
    
    def player_movement(self, keys_pressed):
        
        #(self.x()-32.0),(self.y()-38.0),(self.x()+64.0),(self.y()+54.0)
        dx = 0
        
        #position = self.physics_old.check_collision_direction(self,nearbyitems)
        
        if Qt.Key_Space in keys_pressed:
            
            self.jump = True
        
        if self.jump:
            self.counter += 1
        if self.counter >= 5:
            self.jump = False    
        
        if not self.fall:
            dy = self.Jumping()
        else:
            dy = self.Falling()
            
        
        if not self.physics.check_collision_left(self,self.scene):
            if Qt.Key_A in keys_pressed:
                dx -= self.speed
                if self.x()+dx < 0:
                    dx = 0
        
        if not self.physics.check_collision_right(self,self.scene):
            if Qt.Key_D in keys_pressed:
                dx += self.speed
                if self.x()+dx+32 > self.scene.getSceneX():
                    dx = 0
        
        self.try_to_move(dx,dy)
        
        
    
    def try_to_move(self,dx,dy):
        
        transform = QTransform()
        pos = self.pos()
        pos1 = pos + QPointF(3.0,31.0-dy)
        pos2 = pos + QPointF(29.0,31.0-dy)
        
        item1 = self.scene.itemAt(pos1,transform)
        item2 = self.scene.itemAt(pos2,transform)
        print(item1,item2)
        if item1 is None and item2 is None:
            pass
            
        if item1 is not None:
            if item1.is_collidable():
                dy = item1.y()-self.y()-32
                
        if item2 is not None:
            if item2.is_collidable():
                dy = item2.y()-self.y()-32
                
        if item1 is not None or item2 is not None:
            pass
        
        pos3 = pos + QPointF(3.0,25.0-dx)
        pos4 = pos + QPointF(29.0,25.0+dx)
        
        item3 = self.scene.itemAt(pos3,transform)
        item4 = self.scene.itemAt(pos4,transform)
        
        if item3 is None and item4 is None:
            pass
            
        if item3 is not None:
            if item3.is_collidable():
                dx = self.x()-item3.x()-32
                
        if item4 is not None:
            if item4.is_collidable():
                dx = item4.x()-self.x()-32
                
        if item3 is not None or item4 is not None:
            pass
        
        print(dx,dy)
        self.setPos(self.x()+dx, self.y()-dy)
        
    def Falling(self):
        
        if self.physics.check_collision_down(self,self.scene) and self.jump:
            
            self.vy = self.jump_height
            dy = self.vy
            
        elif self.physics.check_collision_down(self,self.scene):
            
            self.counter = 0
            self.jump = False
            self.fall = False
            dy = 0
            
            self.vy = self.physics.reset_gravity()
            
        else:
            
            self.vy = self.physics.gravity(self.vy)
            if self.vy <= -self.jump_height*2:
                dy = -self.jump_height*2
            else:
                dy = self.vy
        
        return dy
    
    def Jumping(self):
        
        if self.physics.check_collision_down(self,self.scene) and self.jump:
            self.vy = self.jump_height
            dy = self.vy
            
        elif self.physics.check_collision_up(self, self.scene):
            self.vy = self.physics.reset_gravity()
            dy = self.vy
            self.fall = True
            
        elif self.physics.check_collision_down(self,self.scene):
            self.counter = 0
            self.jump = False
            dy = 0
            
            self.vy = self.physics.reset_gravity()
            
        else:
            self.vy = self.physics.gravity(self.vy)
            if self.vy <= -self.jump_height*2:
                dy = -self.jump_height*2
            else:
                dy = self.vy
        
        return dy
        
        
        
        