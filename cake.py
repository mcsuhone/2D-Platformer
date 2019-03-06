from PyQt5.QtGui import QPixmap
from item import Item

class Cake(Item):
    
    def __init__(self,x,y, collision = False, parent=None):
        
        Item.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Cake.png"))
        self.addPos(x,y)
        self.collision = collision
        