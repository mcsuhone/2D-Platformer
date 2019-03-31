from Creatures.enemy import Enemy
from PyQt5.Qt import QPixmap
from animation import Animation


class CaveBug(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/CaveBug",15)
        self.set_pos(x,y)
    