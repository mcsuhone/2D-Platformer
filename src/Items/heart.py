from PyQt5.Qt import QGraphicsPixmapItem, QPixmap



class Heart(QGraphicsPixmapItem):
    
    def __init__(self, parent=None):
        
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Heart.png"))