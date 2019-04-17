from PyQt5.Qt import pyqtSignal, QObject




class Signals(QObject):
    
    direction_changed = pyqtSignal()
    animation_changed = pyqtSignal()
    player_moved = pyqtSignal()
    
    def __init__(self):
        QObject.__init__(self)