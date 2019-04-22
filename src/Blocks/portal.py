from PyQt5.QtGui import QPixmap
from Blocks.block import Block

class Portal(Block):
    
    def __init__(self,x,y, scene, collision = False, parent=None):
        texture = "Textures/Blocks/Portal.png"
        Block.__init__(self,x,y,scene,texture,collision=collision,parent=parent)
        self.setOpacity(0.6)
        
    def touch_effect(self,player,scene):
        
        scene.win_screen()