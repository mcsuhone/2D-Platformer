from PyQt5.Qt import pyqtSignal, QObject




class Signals(QObject):
    
    direction_changed = pyqtSignal()
    animation_changed = pyqtSignal()
    
    def __init__(self):
        QObject.__init__(self)