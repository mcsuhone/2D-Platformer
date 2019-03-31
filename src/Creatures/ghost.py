from .enemy import Enemy
from PyQt5.Qt import QPixmap
from animation import Animation
from physics import Physics


class Ghost(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/Ghost",25)
        self.set_pos(x,y+32)
        
    def set_physics(self):
        
        self.physics = Physics(height = 22, width = 23, offset = 6, weight = 1.0)