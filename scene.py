from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView
from PyQt5.QtCore import Qt,QBasicTimer,QRectF,QSizeF
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.Qt import QPointF

from maploader import MapLoader


SCENE_X                 = 800
SCENE_Y                 = 600
WINDOW_WIDTH            = 800
WINDOW_HEIGHT           = 600
FRAME_TIME_MS           = 16
SQUARE_SIZE             = 32
PLAYER_SIZE             = 32
SECOND                  = 1000


class Scene(QGraphicsScene):

    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        
        mapname = "map1.txt"
        
        self.maploader = MapLoader()
        mapsize = self.maploader.load_map(self,mapname)
        SCENE_X = mapsize['xsize']
        SCENE_Y = mapsize['ysize']
        
        self.size = QSizeF(SCENE_X,SCENE_Y)
        
        self.addBackGround()
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        
        
        self.view.show()
        
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures\BlockGrass.png')))
    
    
        
    def addBackGround(self):
        
        gradient = QLinearGradient(SCENE_X/2,0,SCENE_X/2,SCENE_Y)
        gradient.setColorAt(0,QColor(0,100,200))
        gradient.setColorAt(1,QColor(200,200,200))
        
        self.setBackgroundBrush(QBrush(gradient))
    
    def addDerbiili(self,derbiili):
        
        self.player = derbiili
    
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.camera_control()
        self.game_update()
        self.update()

    def camera_control(self):
        #checks x camera movement
        pass

    def game_update(self):
        
        self.player.player_movement(self.keys_pressed)