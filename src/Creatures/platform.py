from .enemy import Enemy
from PyQt5.Qt import QPixmap, QPointF, QRectF, QPainterPath
from animation import Animation
from Creatures.flyingenemy import FlyingEnemy


class Platform(FlyingEnemy):
    
    def __init__(self,x,y, scene, collision = True, parent=None):
        speed = -0.6
        distance = 10
        size = {'height':32,'width':32,'offset':0,'weight':1.0}
        FlyingEnemy.__init__(self,scene,speed,distance,collision,size,parent=parent)
        self.animation = Animation(self,"Textures/Platform",1000)
        self.size = self.calculate_size()
        self.set_pos(x,y)
    
    def shape(self):
        
        rect = QRectF(0,0,32,32)
        path = QPainterPath()
        path.addRect(rect)
        path.moveTo(self.pos())
        
        return path
    
    def touch_effect(self, player, scene):
        
        pass
    
    def stand_on_effect(self, player, scene):
        
        player.setPos(player.x()+self.speed,player.y())