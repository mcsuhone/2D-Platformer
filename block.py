from PyQt5.QtGui import QPixmap,QPainterPath
from PyQt5.QtWidgets import QGraphicsPixmapItem


class Block(QGraphicsPixmapItem):
    
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        
    def addPos(self,x,y):
        self.setPos(x,y)
    