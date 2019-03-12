from PyQt5.QtGui import QPixmap
from Items.item import Item

class Cake(Item):
    
    def __init__(self,x,y, collision = False, pickable = True, parent=None):
        
        Item.__init__(self,pickable,parent)
        self.setPixmap(QPixmap("Textures\Cake.png"))
        self.addPos(x,y)
        self.collision = collision
        self.idle_state = 1
    
    def effect(self):
        print("Yummy cake!")
        
    def update_idle(self):
        if self.idle_state == 1:
            self.idle_state += 1
            self.setPos(self.x(), self.y()+1)
        elif self.idle_state == 2:
            self.idle_state = -1
            self.setPos(self.x(), self.y()-1)
        elif self.idle_state == -1:
            self.idle_state += -1
            self.setPos(self.x(), self.y()-1)    
        elif self.idle_state == -2:
            self.idle_state = 1
            self.setPos(self.x(), self.y()+1)
        