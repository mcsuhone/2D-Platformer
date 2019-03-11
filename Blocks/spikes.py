from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Spikes(Block):
    
    def __init__(self,x,y,collision = True, obstacle = True, parent=None):
        Block.__init__(self,collision,obstacle,parent)
        self.setPixmap(QPixmap("Textures\Spikes.png"))
        self.addPos(x,y)
        
    def obstacle_effect(self,scene):
        
        scene.death_screen()
        print("Kuolit!")