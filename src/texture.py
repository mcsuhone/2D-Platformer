from PyQt5.Qt import QPixmap




class Texture():
    
    def __init__(self,object,texture):
        
        self.pixmap = QPixmap(texture)
        self.width = self.pixmap.width()
        self.height = self.pixmap.height()
        
        self.setPixmap(object)
        
    def get_width(self):
        
        return (self.width)/32
    
    def get_height(self):
        
        return (self.height)/32
        
    def setPixmap(self,object):
        #object needs to QGraphicsPixmapItem
        
        object.setPixmap(self.pixmap)

        
    