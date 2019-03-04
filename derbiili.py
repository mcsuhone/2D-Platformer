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
        
        #position = self.physics.check_collision_direction(self,nearbyitems)
        
        if Qt.Key_Space in keys_pressed:
            
            self.jump = True
        
        if self.jump:
            self.counter += 1
        if self.counter >= 3:
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
        
        transform = QTransform()
        pos = self.pos()
        pos1 = pos + QPointF(0.0,31.0-dy)
        pos2 = pos + QPointF(31.0,31.0-dy)
        
        itemunder1 = self.scene.itemAt(pos1,transform)
        itemunder2 = self.scene.itemAt(pos2,transform)
        
        
        if itemunder1 != None:
            self.setPos(self.x()+dx, itemunder1.y()-32)
        elif itemunder2 != None:
            self.setPos(self.x()+dx, itemunder2.y()-32)
        else:
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
            if self.vy <= -self.jump_height:
                dy = -self.jump_height
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
            if self.vy <= -10:
                dy = -10
            else:
                dy = self.vy
        
        return dy
        
        
        
        