from PyQt5.QtGui import QPixmap,QPainterPath
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt


class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, scene, physics, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        
        self.speed = 3
        self.jump_height = 12.0
        self.jump = False
        self.vy = 0.0
        self.counter = 0
        
        self.scene = scene
        self.physics = physics
        
    def game_update(self, keys_pressed):
        dx = 0
        
        if Qt.Key_Space in keys_pressed:
            self.jump = True
        if self.jump:
            self.counter += 1
        if self.counter >= 2:
            self.jump = False
            
        if self.physics.check_collision(self.scene,self) and self.jump:
            self.vy = self.jump_height
            dy = self.vy
            
        elif self.physics.check_collision(self.scene,self):
            self.counter = 0
            self.jump = False
            dy = 0
            self.physics.reset_gravity()
            
        else:
            self.vy = self.physics.gravity(self.vy)
            dy = self.vy
        
        
        
        if Qt.Key_A in keys_pressed:
            
            dx -= self.speed
               
        if Qt.Key_D in keys_pressed:
            
            dx += self.speed
        
        self.setPos(self.x()+dx, self.y()-dy)
    
    def is_flying(self):
        
        if self.physics.check_collision(self.scene,self):
            return False
        else:
            return True
     
        
        
        