from PyQt5.Qt import pyqtSignal, QObject




class Pause(QObject):
    
    pause_end = pyqtSignal()
    
    def __init__(self):
        QObject.__init__(self)
        self.pause = False
        self.pausetime = 0
        self.pausetimer = 0
        
    def pause_state(self):
        
        return self.pause
        
    def begin(self,time):
        
        self.pause = True
        self.pausetime = time
        
    def calculate_pause(self):
        
        self.pausetimer += 1
        if self.pausetimer == self.pausetime:
            self.pause = False
            self.pausetimer = 0
            return True
        else:
            return False
        
    