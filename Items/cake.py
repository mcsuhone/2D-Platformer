from PyQt5.QtGui import QPixmap
from Items.item import Item

class Cake(Item):
    
    def __init__(self,x,y, collision = False, pickable = True, parent=None):
        
        Item.__init__(self,pickable,parent)
        self.setPixmap(QPixmap("Textures\Cake.png"))
        self.addPos(x,y)
        self.collision = collision
        self.idle_state = 0.0
    
    def effect(self,scene):
        
        scene.add_cake(1)
        
    def update_idle(self):
        
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
        