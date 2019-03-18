from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Spikes(Block):
    
    def __init__(self,x,y,collision = True, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures\Spikes.png"))
        self.addPos(x,y)
        
    def stand_on_effect(self,player,scene):
        
        scene.death_screen()
        
        return True