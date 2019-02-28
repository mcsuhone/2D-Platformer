from PyQt5.QtGui import QPixmap,QPainterPath
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt


class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, scene, physics, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        self.speed = 3
        self.jump_height = 12.0
        self.vy = 0.0
        self.scene = scene
        self.physics = physics
        
    def game_update(self, keys_pressed):
        dx = 0
        
        if self.is_flying():
            self.vy = self.physics.gravity(self.vy)
            dy = self.vy
            
        elif not self.is_flying() and Qt.Key_Space in keys_pressed:
            self.vy = self.jump_height
            dy = self.vy
            
        else:
            dy = 0
            self.physics.reset_gravity()
        
        
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
     
        
        
        