from PyQt5.QtGui import QPixmap
from Blocks.block import Block
from PyQt5.Qt import QPainterPath, QRectF

class Spikes(Block):
    
    def __init__(self,x,y,collision = True, parent=None):
        Block.__init__(self,collision,parent)
        self.setPixmap(QPixmap("Textures/Blocks/Spikes.png"))
        self.addPos(x,y)
        self.ypos = y*32
        
    def stand_on_effect(self,player,scene):
        
        scene.backToSavePoint()
        
        return True
    
    def shape(self):
        
        rect = QRectF(0,7,32,25)
        path = QPainterPath()
        path.addRect(rect)
        path.moveTo(self.pos())
        
        return path
        
    def y(self):
        
        return self.ypos+7
        
        
        
        