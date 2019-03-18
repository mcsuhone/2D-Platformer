from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockIce(Block):
    
    def __init__(self,x,y,collision = True, obstacle = True, parent = None):
        Block.__init__(self,collision,obstacle,parent)
        self.setPixmap(QPixmap("Textures\BlockIce.png"))
        self.addPos(x,y)
        
    def obstacle_effect(self,player,scene):
        
        player.set_friction(0.01)