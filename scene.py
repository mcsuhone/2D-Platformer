from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView
from PyQt5.QtCore import Qt,QBasicTimer,QRectF,QSizeF
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.Qt import QPointF, QTransform

from maploader import MapLoader
from CONSTANTS import *

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
        self.SCENE_X = mapsize['xsize']
        self.SCENE_Y = mapsize['ysize']
        
        
        self.size = QSizeF(self.SCENE_X,self.SCENE_Y)
        rect = QRectF(QPointF(0,0),self.size)
        self.setSceneRect(rect)
        
        self.addBackGround()
        
        
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        
        x = self.player.x()
        pos = QPointF(x,self.SCENE_Y)
        self.view.centerOn(pos)
        
        self.view.show()
        
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures\BlockGrass.png')))
    
    def getSceneX(self):
        
        return self.SCENE_X
    
    def addBackGround(self):
        
        gradient = QLinearGradient(self.SCENE_X/2,0,self.SCENE_X/2,self.SCENE_Y)
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
        #x = False
        #if Qt.Key_Up in self.keys_pressed:
        #    x = True
        #if x:
        self.camera_control()
        self.game_update()
        self.update()
        #    x=False

    def camera_control(self):
        #checks x camera movement
        x = self.player.x()
        pos = QPointF(x,self.SCENE_Y)
        self.view.centerOn(pos)
        
    def game_update(self):
        
        self.player.player_movement(self.keys_pressed)