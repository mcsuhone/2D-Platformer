from PyQt5.Qt import QPushButton

class Button(QPushButton):
    
    def __init__(self,x,y,W,H, text, parent=None):
        QPushButton.__init__(self,text,parent)
        self.setFixedSize(W,H)
        self.move(x-W/2,y-H/2)
       
        
        