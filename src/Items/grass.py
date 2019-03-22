from PyQt5.QtGui import QPixmap
from Items.item import Item

class Grass(Item):
    
    def __init__(self,x,y, collision = False, touchable = False, parent=None):
        
        Item.__init__(self,touchable,parent)
        self.setPixmap(QPixmap("Textures\Grass.png"))
        self.addPos(x,y)
        self.collision = collision
    