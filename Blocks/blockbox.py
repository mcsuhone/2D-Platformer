from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockBox(Block):
    
    def __init__(self,x,y,collision = True, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures\BlockBox.png"))
        self.addPos(x,y)