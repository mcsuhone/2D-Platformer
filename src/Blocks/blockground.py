from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockGround(Block):
    
    def __init__(self,x,y, scene, collision = True, parent=None):
        Block.__init__(self,scene,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/BlockGround.png"))
        self.addPos(x,y)