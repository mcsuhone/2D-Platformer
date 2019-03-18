from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView
from PyQt5.QtCore import Qt,QBasicTimer,QRectF,QSizeF
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.Qt import QPointF, QTransform, QGraphicsTextItem, QFont, QLabel,\
    QGridLayout, QGraphicsRectItem, QPushButton

import Items
from button import Button
from maploader import MapLoader
from CONSTANTS import *
import Creatures

class Scene(QGraphicsScene):

    def __init__(self, menu, mapname, parent = None):
        
        QGraphicsScene.__init__(self, parent)
        
        # hold the set of keys we're pressing
        self.keys_pressed = set()

        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        
        #define menu and load map
        self.menu = menu
        self.maploader = MapLoader()
        self.map_info = self.maploader.load_map(self,mapname)
        self.cakes = 0
        self.stop = False
        self.addBackGround()
        self.addScoreBoard()
        print(self.map_info)
        
        rect = QRectF(QPointF(0,0),QSizeF(self.map_info['xsize'],self.map_info['ysize']))
        self.setSceneRect(rect)
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WINDOW_WIDTH*1.5,WINDOW_HEIGHT*1.5)
        
        self.view.scale(2,2)
        
        #camera settings
        if self.player is None:
            print("Player is missing from map file.")
        else:
            self.camera_y = self.player.y()
            self.camera_x = self.player.x()
            self.camera_speed = 4
        
        self.list_items()
        
        self.view.show()
        
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures\BlockGrass.png')))
    
    def list_items(self):
        
        itemlist = self.view.items()
        
        self.idleitems = []
        self.enemies = []
        
        for item in itemlist:
            if type(item) == Items.cake.Cake:
                self.idleitems.append(item)
            elif type(item) == Creatures.snake.Snake:
                self.enemies.append(item)
            elif type(item) == Creatures.bat.Bat:
                self.enemies.append(item)
    
    def add_cake(self,cakes):
        
        self.cakes += cakes
        
    def is_stopped(self):
        
        return self.stop
    
    def death_screen(self):
        
        redscreen = QGraphicsRectItem(0,0,self.map_info['xsize'],self.map_info['ysize'])
        redbrush = QBrush(QColor(200,100,100))
        redscreen.setBrush(redbrush)
        redscreen.setOpacity(0.4)
        self.addItem(redscreen)
        
        self.stop = True
        
        pos = self.view.mapToScene(0,0)
        
        button2 = Button(300+pos.x()-80,200+pos.y()+64,160,32, "Back to map menu")
        button2.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button2.clicked.connect(self.back_to_menu)
        self.addWidget(button2,Qt.Widget)
        
        button3 = Button(300+pos.x()-80,200+pos.y()+128,160,32, "Exit")
        button3.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button3.clicked.connect(self.view.close)
        self.addWidget(button3,Qt.Widget)
        
        deathtext = QGraphicsTextItem("Out of lives!")
        deathtext.setPos(2300+pos.x()-80,200+pos.y()-64)
        self.addItem(deathtext)
       
    def win_screen(self):
        
        winscreen = QGraphicsRectItem(0,0,self.map_info['xsize'],self.map_info['ysize'])
        lightbrush = QBrush(QColor(200,220,200))
        winscreen.setBrush(lightbrush)
        winscreen.setOpacity(0.4)
        self.addItem(winscreen)
        
        self.stop = True
        
        pos = self.view.mapToScene(0,0)
        
        button1 = Button(300+pos.x()-80,200+pos.y(),160,32, "Next level!")
        button1.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button1.clicked.connect(self.next_level)
        self.addWidget(button1,Qt.Widget)
        
        button2 = Button(300+pos.x()-80,200+pos.y()+64,160,32, "Back to map menu")
        button2.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button2.clicked.connect(self.back_to_menu)
        self.addWidget(button2,Qt.Widget)
        
        button3 = Button(300+pos.x()-80,200+pos.y()+128,160,32, "Exit")
        button3.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button3.clicked.connect(self.view.close)
        self.addWidget(button3,Qt.Widget)
        
        wintext = QGraphicsTextItem("Level completed!")
        wintext.setPos(2300+pos.x()-80,200+pos.y()-64)
        self.addItem(wintext)
        
    def back_to_menu(self):
        
        self.view.close()
        self.menu.show()
        self.menu.display_map_menu()
        
    def next_level(self):
        
        self.view.close()
        self.menu.show()
        self.menu.display_map_menu()
        
    def addScoreBoard(self):
        
        str = "Cake collected: " + "{:}".format(self.cakes)
        self.scoreboard = QGraphicsTextItem(str)
        self.addItem(self.scoreboard)
        
    def getSceneX(self):
        
        return self.map_info['xsize']
    
    def addBackGround(self):
        #gc stands for gradient color
        gc1 = self.map_info['background'][0]
        gc2 = self.map_info['background'][1]
        
        gradient = QLinearGradient(self.map_info['xsize']/2,0,self.map_info['xsize']/2,self.map_info['ysize'])
        gradient.setColorAt(0,QColor(gc1[0],gc1[1],gc1[2]))
        gradient.setColorAt(1,QColor(gc2[0],gc2[1],gc2[2]))
        
        self.setBackgroundBrush(QBrush(gradient))
    
    def addDerbiili(self,derbiili):
        
        self.save_point = derbiili.pos()
        self.player = derbiili
        self.player.setZValue(0)
    
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())
    
    def timerEvent(self, event):
        
        self.camera_control()
        self.update_items()
        self.game_update()
        
        self.update()
        
        if self.stop:
            self.timer.stop()

    def camera_control(self):
        
        x = self.player.x()
        y = self.player.y()
        
        if self.camera_y+50 < y:
            self.camera_y += self.camera_speed
        elif self.camera_y-50 > y:
            self.camera_y -= self.camera_speed
        else:
            pass
        
        self.view.centerOn(x,self.camera_y)
        
    def game_update(self):
        
        self.update_GUI()
        self.update_enemies()
        self.player.player_movement(self.keys_pressed)
        
        if self.player.y() > self.map_info['ysize']:
            self.death_screen()
        
    def update_GUI(self):
        
        pos = self.view.mapToScene(0,0)
        self.scoreboard.setPos(pos)
        str = "Cake collected: " + "{:}".format(self.cakes)
        self.scoreboard.setPlainText(str)
        
    def update_items(self):
        
        for item in self.idleitems:
            item.update_idle()
                
    def update_enemies(self):
        
        for enemy in self.enemies:
            enemy.move()
        