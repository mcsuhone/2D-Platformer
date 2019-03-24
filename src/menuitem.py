from PyQt5.Qt import QLabel, QPixmap




class MenuItem(QLabel):
    
    def __init__(self,x,y,texture,parent = None):
        QLabel.__init__(self,parent)
        
        pix = QPixmap(texture)
        self.setPixmap(pix)
        self.setMask(pix.mask())
        width = pix.width()
        height = pix.height()
        self.move(x-width/2,y-height/2)