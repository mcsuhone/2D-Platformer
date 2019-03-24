from PyQt5.QtGui import QPixmap
from src.Blocks.block import Block

class BlockGrass(Block):
    
    def __init__(self,x,y,collision = True, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/BlockGrass.png"))
        self.addPos(x,y)
        