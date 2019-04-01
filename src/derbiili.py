from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics
import Blocks
from CONSTANTS import *
from PyQt5.Qt import QPointF
from texture import Texture

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, x, y, scene, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.texture = Texture(self,"Textures/Derbiili/Derbiili.png")
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        #values can be found in "CONSTANTS"
        self.speed = PLAYER_SPEED
        self.jump_height = JUMP_HEIGHT
        self.in_air = False
        self.crouching = False
        self.a = ACCELERATION
        self.friction = FRICTION
        
        self.vx = 0.0
        self.vy = 0.0
        self.direction = 'right'
    
        self.scene = scene
        self.physics = Physics()
        
    def is_collidable(self):
        
        return self.collision
    
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        pass
    
    def player_movement(self, keys_pressed,keybindings):
        dx = 0
        dy = 0
        
        self.is_touching()
        if self.scene.is_stopped():
            return 0,0
        
        self.is_standing_on(dy)
        if self.scene.is_stopped():
            return 0,0
        
        if keybindings['crouch'] in keys_pressed:
            self.crouching = True
            self.speed = 2
        else:
            self.crouching = False
            self.speed = PLAYER_SPEED
        
        if self.in_air:
            
            dv = self.physics.gravity()               #continue air movement
            dy = self.vy-dv
            
        elif keybindings['jump'] in keys_pressed:
            dy = self.jump()                          #iniate jump
            
        if keybindings['left'] in keys_pressed:
            self.direction = 'left'
            
            if self.vx > 0:
                self.vx -= self.friction
                dx += self.vx
                
            elif self.vx > -self.speed:
                self.vx -= self.a
                dx += self.vx
            else:
                dx -= self.speed
                
            if self.x()+dx < 0:
                dx = 0   
        
        elif keybindings['right'] in keys_pressed:
            self.direction = 'right'
            
            if self.vx < 0:
                self.vx += self.friction
                dx += self.vx
            elif self.vx < self.speed:
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
                self.vx = 0.0  
                
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
                self.vx = 0.0   
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.physics.reset_gravity()
        
        self.update_texture()
        #positive dy moves player up, negative moves down
        self.move(dx,dy)
    
    def is_standing_on(self,dy):
        
        effect = False
        transform = QTransform()
        pos = self.pos()
        posdown1 = pos + QPointF(5.0,32.0)
        posdown2 = pos + QPointF(27.0,32.0)
        
        item1 = self.scene.itemAt(posdown1,transform)
        item2 = self.scene.itemAt(posdown2,transform)
        
        if item1 is None and item2 is None:
            self.in_air = True
            effect = True
            
        elif item1 is not None:
            
            effect = item1.stand_on_effect(self,self.scene)
                
        elif item2 is not None:
            
            effect = item2.stand_on_effect(self,self.scene)
                
        elif item1 is not None or item2 is not None:
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
        self.physics.reset_gravity()
        
        return dy
        
    def set_friction(self,df):
        
        self.friction = df
        self.a = df*2
        
    def reset_friction(self):
        
        self.friction = FRICTION
        self.a = ACCELERATION
        
    def move(self,dx,dy):
        
        self.setPos(self.x()+dx, self.y()-dy)
        
    def update_texture(self):
        if self.crouching:
            if self.direction == 'right':
                self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliCrouching.png"))
            else:
                self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliCrouchingFlipped.png"))
        else:
            if self.in_air:
                if self.direction == 'right':
                    self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliJumping.png"))
                else:
                    self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliJumpingFlipped.png"))
            else:
                if self.direction == 'right':
                    self.setPixmap(QPixmap("Textures/Derbiili/Derbiili.png"))
                else:
                    self.setPixmap(QPixmap("Textures/Derbiili/DerbiiliFlipped.png"))
        
        
        