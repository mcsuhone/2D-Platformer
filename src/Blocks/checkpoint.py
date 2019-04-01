from PyQt5.QtGui import QPixmap
from Blocks.block import Block
from animation import Animation

class Checkpoint(Block):
    
    def __init__(self,x,y,collision = False, parent=None):
        Block.__init__(self,collision,parent)
        self.animation = Animation(self,"Textures/Checkpoint",8)
        self.addPos(x,y)
        self.setOpacity(0.8)
        self.setZValue(1)
        
    def touch_effect(self,player,scene):
        
        scene.set_checkpoint(self.pos())
        
    def update(self):
        
        self.animation.animate(self)