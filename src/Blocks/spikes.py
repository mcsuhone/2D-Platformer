from PyQt5.QtGui import QPixmap
from Blocks.block import Block
from PyQt5.Qt import QPainterPath, QRectF

class Spikes(Block):
    
    def __init__(self,x,y,scene,collision = True, parent=None):
        texture = "Textures/Blocks/Spikes.png"
        Block.__init__(self,x,y,scene,collision=collision,parent=parent)
        self.ypos = y*32
        
    def stand_on_effect(self,player,scene):
        
        scene.back_to_checkpoint()
        
        return True
    
    def shape(self):
        
        rect = QRectF(0,7,32,25)
        path = QPainterPath()
        path.addRect(rect)
        path.moveTo(self.pos())
        
        return path
        
    def y(self):
        
        return self.ypos+7
        
        
        
        