from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockIce(Block):
    
    def __init__(self,x,y,collision = True, parent = None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures\BlockIce.png"))
        self.addPos(x,y)
        
    def stand_on_effect(self,player,scene):
        
        player.set_friction(0.01)
        
        return True