from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView
from PyQt5.QtCore import Qt,QBasicTimer,QRectF,QSizeF
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.Qt import QPointF, QTransform, QGraphicsTextItem, QFont, QLabel,\
    QGridLayout, QGraphicsRectItem

from maploader import MapLoader
from CONSTANTS import *

class Scene(QGraphicsScene):

    def __init__(self,menu,mapname, parent = None):
        
        QGraphicsScene.__init__(self, parent)
        
        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        
        
        self.menu = menu
        self.maploader = MapLoader()
        self.mapsize = self.maploader.load_map(self,mapname)
        
        rect = QRectF(QPointF(0,0),QSizeF(self.mapsize['xsize'],self.mapsize['ysize']))
        self.setSceneRect(rect)
        
        self.addBackGround()
        #self.addScoreBoard()
        
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WINDOW_WIDTH*1.5,WINDOW_HEIGHT*1.5)
        
        self.view.scale(2,2)
        
        x = self.player.x()
        pos = QPointF(x,self.mapsize['ysize'])
        self.view.centerOn(pos)
        
        self.view.show()
        
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures\BlockGrass.png')))
    
    def death_screen(self):
        
        redscreen = QGraphicsRectItem(0,0,self.mapsize['xsize'],self.mapsize['ysize'])
        redbrush = QBrush(QColor(200,100,100))
        redscreen.setBrush(redbrush)
        redscreen.setOpacity(0.4)
        self.addItem(redscreen)
        
        self.addText('Kuolit!!')
        
        self.timer.stop()
        
    
    def death_event(self):
        
        
        self.view.hide()
        self.menu.show()
        self.menu.display_map_menu()
        
    def addScoreBoard(self):
        
        self.layout = QGridLayout(self)
        title = QLabel("Hello World", self)
        self.layout.addWidget(title, 50, 50)
        
        self.setLayout(self.layout)
        
    def getSceneX(self):
        
        return self.mapsize['xsize']
    
    def addBackGround(self):
        
        gradient = QLinearGradient(self.mapsize['xsize']/2,0,self.mapsize['xsize']/2,self.mapsize['ysize'])
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
        pos = QPointF(x,self.mapsize['ysize'])
        self.view.centerOn(pos)
        
    def game_update(self):
        
        self.player.player_movement(self.keys_pressed)