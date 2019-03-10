from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, scene, x, y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        self.speed = 3
        self.jump_height = 6.0
        self.in_air = False
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
            dx -= self.speed
            if self.x()+dx < 0:
                dx = 0
        
        if Qt.Key_D in keys_pressed:
            dx += self.speed
            if self.x()+dx+32 > self.scene.getSceneX():
                dx = 0
                
        if dy <= 0:
            
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
        #detects return None is player is not colliding with anything
        #else returns distance from block
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
            
        #detects return None is player is not colliding with anything
        #else returns distance from block
            if xdetect is None:
                pass
            else:
                dx = xdetect    
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                
        #positive dy moves player up, negative moves down
        self.move(dx,dy)
        
        self.pickup_items()
        self.obstacle_check()
        
    def obstacle_check(self):
        
        items = self.scene.collidingItems(self)
        
        for item in items:
            if item.is_obstacle():
                item.obstacle_effect()
        
    def pickup_items(self):
        
        items = self.scene.collidingItems(self)
        
        for item in items:
            if item.is_pickable():
                item.effect()
                self.scene.removeItem(item)
        
    def jump(self):
        self.vy = self.jump_height
        dy = self.vy
        self.in_air = True
        
        return dy
        
    def move(self,dx,dy):
        
        self.setPos(self.x()+dx, self.y()-dy)
        
        
        
        
        