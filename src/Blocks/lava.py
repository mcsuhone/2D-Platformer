from PyQt5.QtGui import QPixmap
from Blocks.block import Block
from animation import Animation
from PyQt5.Qt import QPainterPath, QRectF

class Lava(Block):
    
    def __init__(self,x,y, scene, flow_direction = 'horizontal', collision = False, parent=None):
        Block.__init__(self,scene,collision,parent)
        self.flow_direction = flow_direction
        self.animation = Animation(self,"Textures/Lava",300,lava=True)
        self.addPos(x,y)
        
    def shape(self):
        
        rect = QRectF(0,1,32,31)
        path = QPainterPath()
        path.addRect(rect)
        path.moveTo(self.pos())
        
        return path
        
    def touch_effect(self, player, scene):
        
        scene.back_to_checkpoint()
        
    def stand_on_effect(self, player, scene):
        
        scene.back_to_checkpoint()