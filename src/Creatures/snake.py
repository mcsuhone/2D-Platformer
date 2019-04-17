from .enemy import Enemy
from PyQt5.Qt import QPixmap
from animation import Animation


class Snake(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent=parent)
        self.animation = Animation(self,"Textures/Snake",300)
        self.size = self.calculate_size()
        self.set_pos(x,y)
    
    