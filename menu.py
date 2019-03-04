from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView,QPushButton,QMainWindow, QAction, qApp
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.QtCore import Qt,QBasicTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette,QPixmap

from scene import Scene
from CONSTANTS import *


class Menu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        
        self.addMenuGraphics()
        self.initUI()
        
        
    def addMenuGraphics(self):
        
        self.palette = QPalette()
        pixmap = QPixmap('Textures/BlockGround.png')
        self.palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(self.palette)
    
    def initUI(self):               
        
        button_play = QPushButton('Play', self)
        button_play.move(WINDOW_WIDTH/2,200)
        button_play.clicked.connect(self.play)
        
        button_exit = QPushButton('Exit', self)
        button_exit.move(WINDOW_WIDTH/2,300)
        button_exit.clicked.connect(self.close)
        
        self.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.setWindowTitle('Derbiili: Adventures')    
        self.show()
        
        
    def play(self):
        
        self.close()
        scene = Scene()

        
        
        
        
        