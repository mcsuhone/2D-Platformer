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
        
        #define menu and load map
        self.menu = menu
        self.maploader = MapLoader()
        self.mapsize = self.maploader.load_map(self,mapname)
        self.cakes = 0
        
        self.addBackGround()
        self.addScoreBoard()
        
        rect = QRectF(QPointF(0,0),QSizeF(self.mapsize['xsize'],self.mapsize['ysize']))
        self.setSceneRect(rect)
        
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
    
    
    def add_cake(self,cakes):
        
        self.cakes += cakes
    
    def death_screen(self):
        
        redscreen = QGraphicsRectItem(0,0,self.mapsize['xsize'],self.mapsize['ysize'])
        redbrush = QBrush(QColor(200,100,100))
        redscreen.setBrush(redbrush)
        redscreen.setOpacity(0.4)
        self.addItem(redscreen)
        
        self.timer.stop()
        
        pos = self.view.mapToScene(0,0)
        
        button1 = Button(300+pos.x()-80,200+pos.y(),160,32, "Back to map menu")
        button1.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button1.clicked.connect(self.death_event)
        self.addWidget(button1,Qt.Widget)
        
        button2 = Button(300+pos.x()-80,200+pos.y()+64,160,32, "Exit")
        button2.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button2.clicked.connect(self.view.close)
        self.addWidget(button2,Qt.Widget)
        
        deathtext = QGraphicsTextItem("Out of lives!")
        deathtext.setPos(2300+pos.x()-80,200+pos.y()-64)
        self.addItem(deathtext)
        
    def death_event(self):
        
        self.view.hide()
        self.menu.show()
        self.menu.display_map_menu()
        
    def addScoreBoard(self):
        
        str = "Cake collected: " + "{:}".format(self.cakes)
        self.scoreboard = QGraphicsTextItem(str)
        self.addItem(self.scoreboard)
        
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
        #self.update_items()
        self.update()
        
        #    x=False

    def camera_control(self):
        #checks x camera movement
        x = self.player.x()
        pos = QPointF(x,self.mapsize['ysize'])
        self.view.centerOn(pos)
        
    def game_update(self):
        
        self.player.player_movement(self.keys_pressed)
        self.update_GUI()
        
    def update_GUI(self):
        
        pos = self.view.mapToScene(0,0)
        self.scoreboard.setPos(pos)
        str = "Cake collected: " + "{:}".format(self.cakes)
        self.scoreboard.setPlainText(str)
        
    def update_items(self):
        
        itemlist = self.view.items()
        for item in itemlist:
            if type(item) == Items.cake.Cake:
                item.update_idle()
                