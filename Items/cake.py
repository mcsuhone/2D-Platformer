from PyQt5.QtGui import QPixmap
from Items.item import Item

class Cake(Item):
    
    def __init__(self,x,y, collision = False, pickable = True, parent=None):
        
        Item.__init__(self,pickable,parent)
        self.setPixmap(QPixmap("Textures\Cake.png"))
        self.addPos(x,y)
        self.collision = collision
    
    def effect(self):
        print("Yummy cake!")