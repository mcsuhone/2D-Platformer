from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockIce(Block):
    
    def __init__(self,x,y, scene, collision = True, parent = None):
        Block.__init__(self,scene,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/BlockIce.png"))
        self.setOpacity(0.8)
        self.addPos(x,y)
        
    def stand_on_effect(self,player,scene):
        
        player.set_friction(0.015)
        
        return True