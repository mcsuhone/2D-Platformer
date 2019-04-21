from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Portal(Block):
    
    def __init__(self,x,y, scene, collision = False, parent=None):
        Block.__init__(self,scene,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/Portal.png"))
        self.addPos(x,y)
        self.setOpacity(0.6)
        
    def touch_effect(self,player,scene):
        
        scene.win_screen()