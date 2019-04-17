from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView
from PyQt5.QtCore import Qt,QBasicTimer,QRectF,QSizeF
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.Qt import *

import Items
import Blocks
from button import Button
from maploader import MapLoader
from CONSTANTS import *
import Creatures
from Items.heart import Heart
from Items.cake import Cake
from pause import Pause
from Items.flower import Flower
from Particles.particle import Particle

class Scene(QGraphicsScene):

    def __init__(self, menu, maps, mapnumber, options, parent = None):
        
        QGraphicsScene.__init__(self, parent)
        # hold the set of keys we're pressing
        self.keys_pressed = set()
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        #define menu and load map
        self.menu = menu
        self.maploader = MapLoader()
        self.map_info = self.maploader.load_map(self,maps,mapnumber)
        
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WINDOW_WIDTH*1.5,WINDOW_HEIGHT*1.5)
        
        self.view.scale(2,2)
        self.view.centerOn(self.player.pos())
        
        self.options = options
        self.keybindings = self.options['keybindings']
        self.stop = False
        self.addScoreBoard()
        self.health = 5
        self.addHealthBar()
        #self.addMenuButton()
        self.pause = Pause()
        
        self.connections()
        
        rect = QRectF(QPointF(0,0),QSizeF(self.map_info['xsize'],self.map_info['ysize']))
        self.setSceneRect(rect)
        
        self.addBackGround()
        
        #camera settings
        if self.player is None:
            print("Player is missing from map file.")
        else:
            self.camera_y = self.player.y()
            self.camera_x = self.player.x()
            self.camera_speed = 2
        
        self.list_items()
        
        self.view.show()
        
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures/Blocks/BlockGrass.png')))
        
    def connections(self):
        
        self.pause.pause_end.connect(self.respawn)
    
    def list_items(self):
        
        itemlist = self.view.items()
        
        self.idleitems = []
        self.enemies = []
        
        for item in itemlist:
            if type(item) == Items.cake.Cake:
                self.idleitems.append(item)
            elif type(item) == Blocks.checkpoint.Checkpoint:
                self.idleitems.append(item)
            elif type(item) == Creatures.snake.Snake:
                self.enemies.append(item)
            elif type(item) == Creatures.bat.Bat:
                self.enemies.append(item)
            elif type(item) == Creatures.cavebug.CaveBug:
                self.enemies.append(item)
            elif type(item) == Creatures.ghost.Ghost:
                self.enemies.append(item)
        
    def addBackGround(self):
        #gc stands for gradient color
        gradient = QLinearGradient(self.map_info['xsize']/2,0,self.map_info['xsize']/2,self.map_info['ysize'])
        if self.map_info['currentlevel'] == 1:
            
            gc1 = self.map_info['background'][0]
            gc2 = self.map_info['background'][1]
            gradient.setColorAt(0,QColor(gc1[0],gc1[1],gc1[2]))
            gradient.setColorAt(1,QColor(gc2[0],gc2[1],gc2[2]))
            self.setBackgroundBrush(QBrush(gradient))
            
            '''
            brush = QBrush()
            brush.setTexture(QPixmap("Textures/Background1.png"))
            self.view.setBackgroundBrush(brush)
            '''
            
        elif self.map_info['currentlevel'] == 2:
            
            gc1 = self.map_info['background'][0]
            gc2 = self.map_info['background'][1]
            gradient.setColorAt(0,QColor(gc1[0],gc1[1],gc1[2]))
            gradient.setColorAt(1,QColor(gc2[0],gc2[1],gc2[2]))
            self.setBackgroundBrush(QBrush(gradient))
        
        
    
    def addDerbiili(self,derbiili):
        
        self.checkpoint = derbiili.pos()
        self.player = derbiili
        self.player.setZValue(0)
        
    def addMenuButton(self):
        
        self.menu_button = Button(100,20,80,20,"Main menu",self.view)
        self.menu_button.clicked.connect(self.back_to_main_menu)
        self.menu_button.setStyleSheet('''
                                background-image: url(Textures/Button3.png);
                                border: none;
                                ''')
        
    def is_stopped(self):
        
        return self.stop
    
    def getSceneX(self):
        
        return self.map_info['xsize']
    
    def death_screen(self):
        
        redscreen = QGraphicsRectItem(0,0,self.map_info['xsize'],self.map_info['ysize'])
        redbrush = QBrush(QColor(200,100,100))
        redscreen.setBrush(redbrush)
        redscreen.setOpacity(0.4)
        self.addItem(redscreen)
        
        self.stop = True
        
        pos = self.view.mapToScene(0,0)
        
        button2 = Button(300+pos.x(),200+pos.y()+64,160,32, "Back to map menu")
        button2.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button2.clicked.connect(self.back_to_menu)
        self.addWidget(button2,Qt.Widget)
        
        button3 = Button(300+pos.x(),200+pos.y()+128,160,32, "Exit")
        button3.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button3.clicked.connect(self.view.close)
        self.addWidget(button3,Qt.Widget)
        
        deathtext = QGraphicsTextItem("Out of lives!")
        deathtext.setPos(300+pos.x()-80,200+pos.y()-64)
        self.addItem(deathtext)
       
    def win_screen(self):
        
        winscreen = QGraphicsRectItem(0,0,self.map_info['xsize'],self.map_info['ysize'])
        lightbrush = QBrush(QColor(200,220,200))
        winscreen.setBrush(lightbrush)
        winscreen.setOpacity(0.4)
        self.addItem(winscreen)
        
        self.stop = True
        
        pos = self.view.mapToScene(0,0)
        
        button1 = Button(300+pos.x(),200+pos.y(),160,32, "Next level!")
        button1.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button1.clicked.connect(self.next_level)
        self.addWidget(button1,Qt.Widget)
        
        button2 = Button(300+pos.x(),200+pos.y()+64,160,32, "Back to map menu")
        button2.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button2.clicked.connect(self.back_to_menu)
        self.addWidget(button2,Qt.Widget)
        
        button3 = Button(300+pos.x(),200+pos.y()+128,160,32, "Exit")
        button3.setStyleSheet('''
                                background-image: url(Textures/Button1.png);
                                border: none;
                                ''')
        button3.clicked.connect(self.view.close)
        self.addWidget(button3,Qt.Widget)
        
        wintext = QGraphicsTextItem("Level completed!")
        wintext.setPos(300+pos.x()-80,200+pos.y()-64)
        self.addItem(wintext)
        
    def back_to_main_menu(self):
        
        self.view.close()
        self.menu.show()
        self.menu.display_main_menu()
        
    def back_to_menu(self):
        
        self.view.close()
        self.menu.show()
        self.menu.display_map_menu()
        
    def next_level(self):
        
        self.view.close()
        self.menu.next_level(self.map_info['currentlevel'])
        
    def addScoreBoard(self):
        
        self.cakes = []
        
    def addCake(self,cakes):
        
        for i in range(cakes):
            cake = Cake(0,0)
            cake.animation.stop_animation()
            self.addItem(cake)
            self.cakes.append(cake)
        
        if len(self.cakes) >= 10:
            self.addHealth(1)
            for cake in self.cakes:
                self.removeItem(cake)
            self.cakes.clear()
        
    def addHealthBar(self):
        
        self.hearts = []
        
        for i in range(self.health):
            heart = Heart()
            self.addItem(heart)
            self.hearts.append(heart)
    
    def addHealth(self,amount):
        
        for i in range(amount):
            heart = Heart()
            self.addItem(heart)
            self.hearts.append(heart)
            self.health += 1
        
    def removeHealth(self,amount):
        
        for i in range(amount):
            self.removeItem(self.hearts[-1-i])
            self.hearts.pop(-1-i)
            self.health -= 1
        
    def set_checkpoint(self,pos):
        
        self.checkpoint = pos
        
    def back_to_checkpoint(self):
        
        self.pause.begin(120)
        self.player.animation.set_animation('animdeath')
        
    def respawn(self):
        
        self.removeHealth(1)
        if self.health == 0:
            self.death_screen()
        else:
            self.player.setPos(self.checkpoint)
            self.view.centerOn(self.player.pos())
    
    def keyPressEvent(self, event):
        
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        
        self.keys_pressed.remove(event.key())
    
    def keyEvents(self):
        
        if Qt.Key_Escape in self.keys_pressed:
            
            self.back_to_main_menu()
            
    #*********************************************************************************************************
    
    def timerEvent(self, event):
        
        self.keyEvents()
        
        if self.pause.pause_state():
            value = self.pause.calculate_pause()
            self.player.animation.set_animation('animdeath')
            if value:
                self.pause.pause_end.emit()
                self.player.animation.set_animation('default')
                
        else:
            self.camera_control()
            self.game_update()
            
            self.update()
            
        if self.stop:
                self.timer.stop()
                
    #*********************************************************************************************************

    def camera_control(self):
        
        x = self.player.x()
        y = self.player.y()
        for i in range(4):
            if self.camera_y+50 < y:
                self.camera_y += self.camera_speed
            elif self.camera_y-50 > y:
                self.camera_y -= self.camera_speed
            else:
                pass
            
            self.view.centerOn(x,self.camera_y)
        
    def game_update(self):
        
        self.update_items()
        self.update_GUI()
        self.update_enemies()
        self.player.player_movement(self.keys_pressed,self.keybindings)
        
        if self.player.y() > self.map_info['ysize']:
            self.back_to_checkpoint()
        
    def update_GUI(self):
        
        pos = self.view.mapToScene(0,0)
        
        pos0 = pos + QPointF(568,0)
        for i in range(len(self.hearts)):
            pos2 = pos0 - QPointF(32*i,0)
            self.hearts[i].setPos(pos2)
            
        for i in range(len(self.cakes)):
            pos3 = pos0 + QPointF(-128+12.8*i,32)
            self.cakes[i].setPos(pos3)
        
    def update_items(self):
        
        for item in self.idleitems:
            item.update()
                
    def update_enemies(self):
        
        for enemy in self.enemies:
            enemy.update(self,self.player)
        