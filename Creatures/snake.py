from Creatures.enemy import Enemy
from PyQt5.Qt import QPixmap


class Snake(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.2
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.setPixmap(QPixmap("Textures\Snake2.png"))
        self.addPos(x,y)
    
    def flip(self,direction):
        
        if direction == -1:
            self.setPixmap(QPixmap("Textures/Snake2.png"))
        else:
            self.setPixmap(QPixmap("Textures/Snake2Flipped.png"))