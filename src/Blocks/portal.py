from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Portal(Block):
    
    def __init__(self,x,y,collision = False, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures\Portal.png"))
        self.addPos(x,y)
        
    def touch_effect(self,player,scene):
        
        scene.win_screen()