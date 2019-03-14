from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Portal(Block):
    
    def __init__(self,x,y,collision = False, obstacle = True, parent=None):
        Block.__init__(self,collision,obstacle,parent)
        self.setPixmap(QPixmap("Textures\Portal_empty.png"))
        self.addPos(x,y)
        
    def obstacle_effect(self,scene):
        
        scene.win_screen()