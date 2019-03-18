from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics
import Blocks
from CONSTANTS import *
from PyQt5.Qt import QPointF

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, x, y, scene, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures/Derbiili/Derbiili.png"))
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        #values can be found in "CONSTANTS"
        self.speed = PLAYER_SPEED
        self.jump_height = JUMP_HEIGHT
        self.in_air = False
        self.a = ACCELERATION
        self.friction = FRICTION
        
        self.vx = 0.0
        self.vy = 0.0
        self.direction = -1
    
        self.scene = scene
        self.physics = Physics()
        
    def is_collidable(self):
        
        return self.collision
    
    def player_movement(self, keys_pressed):
        dx = 0
        dy = 0
        
        self.is_standing_on()
        
        if self.in_air:
            
            dv = self.physics.gravity()               #continue air movement
            dy = self.vy-dv
            
        elif Qt.Key_Space in keys_pressed:
            dy = self.jump()                          #iniate jump
            
        if Qt.Key_A in keys_pressed:
            self.direction = 1
            
            if self.vx > -self.speed:
                self.vx -= self.a
                dx += self.vx
            else:
                dx -= self.speed
            if self.x()+dx < 0:
                dx = 0   
        
        elif Qt.Key_D in keys_pressed:
            self.direction = -1
            
            if self.vx < self.speed:
                self.vx += self.a
                dx += self.vx
            else:
                dx += self.speed
            if self.x()+dx+32 > self.scene.getSceneX():
                dx = 0
        else:
            if self.vx == 0.0:
                pass
            elif self.vx > 0:
                if self.vx - self.friction < 0:
                    self.vx = 0
                    dx = 0
                else:
                    self.vx -= self.friction
                    dx = self.vx
            else:
                if self.vx + self.friction > 0:
                    self.vx = 0
                    dx = 0
                else:
                    self.vx += self.friction
                    dx = self.vx
        
            
        if dy <= 0:
            
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)

            if xdetect is None:
                pass

            else:
                dx = xdetect    
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
                
        elif dy > 0:
            
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            if xdetect is None:
                pass
            else:
                dx = xdetect    
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                
        #positive dy moves player up, negative moves down
        
        self.is_touching()
        self.update_texture()
        self.move(dx,dy)
        
        return dx,dy
        
    def is_standing_on(self):
        
        effect = False
        transform = QTransform()
        pos = self.pos()
        posdown1 = pos + QPointF(5.0,32.0)
        posdown2 = pos + QPointF(27.0,32.0)
        
        item1 = self.scene.itemAt(posdown1,transform)
        item2 = self.scene.itemAt(posdown2,transform)
        
        if item1 is None and item2 is None:
            self.in_air = True
            
        if item1 is not None:
            
            effect = item1.stand_on_effect(self,self.scene)
                
        if item2 is not None:
            
            effect = item2.stand_on_effect(self,self.scene)
                
        if item1 is not None or item2 is not None:
            pass
        
        if not effect:
            self.reset_friction()
        
    def is_touching(self):
        
        items = self.scene.collidingItems(self)
        
        for item in items:
            
            item.touch_effect(self,self.scene)
    
    def jump(self):
        self.vy = self.jump_height
        dy = self.vy
        self.in_air = True
        
        return dy
        
    def set_friction(self,df):
        
        self.friction = df
        self.a = df/2
        
    def reset_friction(self):
        
        self.friction = FRICTION
        self.a = ACCELERATION
        
    def move(self,dx,dy):

        self.setPos(self.x()+dx, self.y()-dy)
        
    def update_texture(self):
        
        if self.in_air:
            if self.direction == -1:
                self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliJumping.png"))
            else:
                self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliJumpingFlipped.png"))
        else:
            if self.direction == -1:
                self.setPixmap(QPixmap("Textures/Derbiili/Derbiili.png"))
            else:
                self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliFlipped.png"))
        
        
        