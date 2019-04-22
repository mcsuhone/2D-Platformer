from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class BlockIce(Block):
    
    def __init__(self,x,y, scene, collision = True, parent = None):
        texture = "Textures/Blocks/BlockIce.png"
        Block.__init__(self,x,y,scene,texture,collision=collision,parent=parent)
        self.setOpacity(0.8)
        
    def stand_on_effect(self,player,scene):
        
        player.set_friction(0.015)
        
        return True