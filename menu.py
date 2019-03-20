from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView,QPushButton,QMainWindow, QAction, qApp
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QIcon,QPixmap
from PyQt5.QtCore import Qt,QBasicTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette,QPixmap

from button import Button
from scene import Scene
from CONSTANTS import *
from PyQt5.Qt import QLabel


class Menu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setup()
        
        self.show()
        
        self.import_maps()
        self.main_menu()
        self.map_menu()
        
        self.display_main_menu()
        
    def import_maps(self):
        
        self.maps = {1:'Maps/map1.txt',2:'Maps/map2.txt',3:None}
        
    def setup(self):
        
        self.setStyleSheet('''
                            background-image: url(Textures/Button1.png);
                            border: none;
                            ''')
        
        self.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.setWindowTitle('Derbiili: Adventures')
        icon = QPixmap('Textures/BlockGrass.png')
        self.setWindowIcon(QIcon(icon))
        
        self.palette = QPalette()
        gradient = QLinearGradient(WINDOW_WIDTH/2,0,WINDOW_WIDTH/2,WINDOW_HEIGHT)
        gradient.setColorAt(0,QColor(0,100,200))
        gradient.setColorAt(1,QColor(230,255,230))
        self.palette.setBrush(QPalette.Background, QBrush(gradient))
        self.setPalette(self.palette)
        
    def main_menu(self):
        
        self.main_menu_items = []
        
        title = QLabel(self)
        titlepix = QPixmap("Textures/Title.png")
        title.setPixmap(titlepix)
        title.setMask(titlepix.mask())
        title.move(WINDOW_WIDTH/2-300/2,WINDOW_HEIGHT/2-200)
        
        self.main_menu_items.append(title)
        
        button_play = Button(WINDOW_WIDTH/2-160/2,WINDOW_HEIGHT/2-64,160,32,'Map Selection', self)
        button_play.clicked.connect(self.display_map_menu)
        
        self.main_menu_items.append(button_play)
        
        button_exit = Button(WINDOW_WIDTH/2-160/2,WINDOW_HEIGHT/2-16,160,32,'Exit', self)
        button_exit.clicked.connect(self.close)
        
        self.styleSheet()
        self.main_menu_items.append(button_exit)
        
        
    def map_menu(self):
        
        self.map_menu_items = []
        
        button_map1 = Button(200,100,64,64,'Level 1', self)
        button_map1.clicked.connect(self.map1)
        button_map1.clicked.connect(self.play)
        button_map1.setStyleSheet('''
                                background-image: url(Textures/MapIcon1.png);
                                border: none;
                                ''')
        
        self.map_menu_items.append(button_map1)
        
        button_map2 = Button(300,100,64,64,'Level 2', self)
        button_map2.clicked.connect(self.map2)
        button_map2.clicked.connect(self.play)
        button_map2.setStyleSheet('''
                                color: rgb(255,255,255);
                                background-image: url(Textures/MapIcon2.png);
                                border: none;
                                ''')
        
        self.map_menu_items.append(button_map2)
        
        button_back = Button(0,500,160,32,'Back', self)
        button_back.clicked.connect(self.display_main_menu)
        
        self.map_menu_items.append(button_back)
        
    def display_map_menu(self):
        for item in self.main_menu_items:
            item.hide()
            
        for item in self.map_menu_items:
            item.show()
    
    def display_main_menu(self):
        for item in self.map_menu_items:
            item.hide()
        
        for item in self.main_menu_items:
            item.show()
        
    def map1(self):
        
        self.mapnumber = 1
        
    def map2(self):
        
        self.mapnumber = 2
        
    def play(self):
        
        self.close()
        scene = Scene(self,self.maps,self.mapnumber)

    def next_level(self,number):
        
        self.mapnumber = number+1
        
        if self.maps[self.mapnumber] is None:
            print("X")
            self.setup()
            self.show()
            self.display_main_menu()
        else:
            scene = Scene(self,self.maps,self.mapnumber)
        
        
        
        
        