from PyQt5.QtGui import QPixmap
from .item import Item
from animation import Animation

class Cake(Item):
    
    def __init__(self,x,y, collision = False, parent=None):
        
        Item.__init__(self,parent)
        self.addPos(x,y)
        self.collision = collision
        self.idle_state = 0.0
        self.animation = Animation(self,"Textures/Cake",40)
    
    def touch_effect(self,player,scene):
        
        scene.addCake(1)
        scene.removeItem(self)
        
    def update(self):
        self.animation.animate(self)
        