from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, x, y, scene, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        self.speed = 4
        self.jump_height = 6.0
        self.in_air = False
        self.a = 0.5
        self.friction = 0.5
        
        self.vx = 0.0
        self.vy = 0.0
        
        self.scene = scene
        self.physics = Physics()
        
    def is_collidable(self):
        
        return self.collision
    
    def player_movement(self, keys_pressed):
        dx = 0
        dy = 0
        
        testfall = self.physics.check_collisions_y(self, self.scene, -1)
        if testfall is None:
            self.in_air = True
        
        if self.in_air:
            dv = self.physics.gravity()               #continue air movement
            dy = self.vy-dv
            
        elif Qt.Key_Space in keys_pressed:
            dy = self.jump()                          #iniate jump
            
        if Qt.Key_A in keys_pressed:
            if self.vx > -self.speed:
                self.vx -= self.a
                dx += self.vx
            else:
                dx -= self.speed
            if self.x()+dx < 0:
                dx = 0   
        
        elif Qt.Key_D in keys_pressed:
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
        
        self.pickup_items()
        self.obstacle_check()
        
        self.move(dx,dy)
        
    def obstacle_check(self):
        
        items = self.scene.collidingItems(self)
        
        for item in items:
            if item.is_obstacle():
                item.obstacle_effect(self.scene)
                
        
        
    def pickup_items(self):
        
        items = self.scene.collidingItems(self)
        
        for item in items:
            if item.is_pickable():
                item.effect(self.scene)
                self.scene.removeItem(item)
        
    def jump(self):
        self.vy = self.jump_height
        dy = self.vy
        self.in_air = True
        
        return dy
        
    def move(self,dx,dy):

        self.setPos(self.x()+dx, self.y()-dy)
        
        
        
        
        