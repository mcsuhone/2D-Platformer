from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockBox(Block):
    
    def __init__(self,x,y, scene, collision = True, parent=None):
        Block.__init__(self,scene,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/BlockBox.png"))
        self.addPos(x,y)