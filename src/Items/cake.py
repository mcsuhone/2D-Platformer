from PyQt5.QtGui import QPixmap
from src.Items.item import Item
from src.animation import Animation

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
        
    def update_idle(self):
        self.animation.animate(self)
        
        '''
        if 0 <= self.idle_state < 1:
            self.setPos(self.x(), self.y()+0.05)
        if 1 <= self.idle_state <= 3:
            self.setPos(self.x(), self.y()-0.05)
        if 3 < self.idle_state <= 4:
            self.setPos(self.x(), self.y()+0.05)
            
        if self.idle_state >= 4:
            self.idle_state = 0.0
        else:
            self.idle_state += 0.05
        '''