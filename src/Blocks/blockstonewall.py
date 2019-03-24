from PyQt5.QtGui import QPixmap
from src.Blocks.block import Block

class BlockStoneWall(Block):
    
    def __init__(self,x,y,collision = False, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/BlockStoneWall.png"))
        self.addPos(x,y)