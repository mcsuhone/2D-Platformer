from Enemies.enemy import Enemy
from PyQt5.Qt import QPixmap


class Snake(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.5
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.setPixmap(QPixmap("Textures\Snake2.png"))
        self.addPos(x,y)
    
    