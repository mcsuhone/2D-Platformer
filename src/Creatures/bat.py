from .enemy import Enemy
from PyQt5.Qt import QPixmap, QPointF
from animation import Animation
from Creatures.flyingenemy import FlyingEnemy


class Bat(FlyingEnemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.6
        distance = 10
        FlyingEnemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/Bat",10)
        self.size = self.calculate_size()
        self.set_pos(x,y)
    