from PyQt5.QtGui import QPixmap
from Blocks.block import Block
from animation import Animation

class Lava(Block):
    
    def __init__(self,x,y, scene, collision = False, parent=None):
        Block.__init__(self,scene,collision,parent)
        self.animation = Animation(self,"Textures/Lava",200,lava=True)
        self.addPos(x,y)
        
    def touch_effect(self, player, scene):
        
        scene.back_to_checkpoint()