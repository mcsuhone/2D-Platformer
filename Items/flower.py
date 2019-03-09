from PyQt5.QtGui import QPixmap
from Items.item import Item

class Flower(Item):
    
    def __init__(self,x,y, collision = False, pickable = False, parent=None):
        
        Item.__init__(self,pickable,parent)
        self.setPixmap(QPixmap("Textures\Flower.png"))
        self.addPos(x,y)
        self.collision = collision
    