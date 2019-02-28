from PyQt5.QtWidgets import QGraphicsPixmapItem,QGraphicsScene,QGraphicsView,QGraphicsItemGroup
from PyQt5.QtCore import Qt,QBasicTimer,QTimer
from PyQt5.QtGui import QBrush,QColor,QLinearGradient,QPainterPath,QIcon,QPixmap

from derbiili import Derbiili
from blockground import BlockGround
from blockgrass import BlockGrass
from blockrock import BlockRock
from physics import Physics

SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 600
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
        
        
        self.physics = Physics()
        
        
        self.addBackGround()
        self.ground = self.addGround()
        
        self.rock = BlockRock(384,600)
        self.addItem(self.rock)
        
        
        self.addDerbiili()

        
        
        
        
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.view.setWindowTitle("Derbiili: Adventures")
        self.view.setWindowIcon(QIcon(QPixmap('Textures\Derbiili.png')))
        
    def get_ground(self):
        return self.ground
    
        
    def get_ground_shape(self):
        ground = self.get_ground()
        
        path = QPainterPath()
        path.addRect(ground.boundingRect())
        
        return path
        
    def addBackGround(self):
        
        gradient = QLinearGradient(SCREEN_WIDTH/2,0,SCREEN_WIDTH/2,SCREEN_HEIGHT)
        gradient.setColorAt(0,QColor(0,100,200))
        gradient.setColorAt(1,QColor(200,200,200))
        
        self.setBackgroundBrush(QBrush(gradient))
    
    def addDerbiili(self):
        
        self.player = Derbiili(self,self.physics)
        self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2,
                           384)
        
        self.addItem(self.player)
    
    def addGround(self):
        itemgroup = QGraphicsItemGroup()
        
        for x in range(0,800,SQUARE_SIZE):
            for y in range(0,600,SQUARE_SIZE):
                if y > 416:
                    
                    self.blockground = BlockGround(x,y)
                    itemgroup.addToGroup(self.blockground)
                    
                elif y > 384:
                    
                    self.blockgrass = BlockGrass(x,y)
                    itemgroup.addToGroup(self.blockgrass)
                
        self.addItem(itemgroup)
        
        return itemgroup
        
    
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        
        self.game_update()
        
        self.update()

    def game_update(self):
        
        self.player.game_update(self.keys_pressed)