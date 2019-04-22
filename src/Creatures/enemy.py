from PyQt5.Qt import QGraphicsPixmapItem, QPointF, QPainterPath

from physics import Physics
import math
from CONSTANTS import *
from signals import Signals

class Enemy(QGraphicsPixmapItem):
    
    def __init__(self, scene, speed = -1.0, distance = 1.0, collision = False, size = {'height':22,'width':23,'offset':4}, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        
        self.size = size
        self.speed = speed
        self.in_air = False
        self.vy = 0.0
        self.direction = 'left'
        self.distance = distance
        self.player_tracker = set()
        
        self.collision = collision
        self.setZValue(-1)
        self.set_physics()
        self.scene = scene
        self.signals = Signals()
        self.signals.direction_changed.connect(self.direction_changed_update)
        
        scene.addItem(self)
        
    def X0(self):
        
        return self.x()
        
    def Y0(self):
        
        return self.y()
    
    def right_side(self):
        
        return 0
    
    def get_direction(self):
        
        return self.direction

    def calculate_size(self):
        
        size = {'width':0,'height':0}
        pixmap = self.pixmap()
        
        size['width'] = pixmap.width()
        size['height'] = pixmap.height()
        
        return size
    
    def set_physics(self):
        
        self.physics = Physics(self.size['height'],self.size['width'],self.size['offset'])
    
    def set_pos(self,x,y):
        
        self.setPos(x*32,y*32)
        self.origin = QPointF(x*32,y*32)
        
    def stand_on_effect(self,player,scene):
        
        return False
    
    def touch_effect(self,player,scene):
        
        scene.back_to_checkpoint()
    
    def is_collidable(self):
        
        return self.collision
        
    def update(self,scene,player):
        
        self.move()
    
    def flip(self,direction):
        #overwrite this.
        pass
    
    def distance_from_origin(self):
        
        return abs(self.origin.x()-self.x())
    
    def player_direction(self,player):
        
        if player.x() < self.x():
            self.player_tracker.add('left')
        elif 'left' in self.player_tracker:
            self.player_tracker.remove('left')
        
        if player.x() > self.x():
            self.player_tracker.add('right')
        elif 'right' in self.player_tracker:
            self.player_tracker.remove('right')
        
        if self.y()+self.size['height'] > player.y() > self.y()-30:
            self.player_tracker.add('infront')
        elif 'infront' in self.player_tracker:
            self.player_tracker.remove('infront')
        
        if player.y() < self.y()-32:
            self.player_tracker.add('above')
        elif 'above' in self.player_tracker:
            self.player_tracker.remove('above')
            
        if player.y() > self.y()+self.size['height']:
            self.player_tracker.add('below')
        elif 'below' in self.player_tracker:
            self.player_tracker.remove('below')
        
    def distance_from_player(self,player):
        
        xdistance = abs(self.x()-player.x())
        ydistance = abs(self.y()-player.y())
        
        distance = math.sqrt(xdistance**2+ydistance**2)
        
        return distance
    
    def change_direction(self):
        
        if self.direction == 'left':
            self.direction = 'right'
            self.speed = -self.speed
        else:
            self.direction = 'left'
            self.speed = -self.speed
            
        self.signals.direction_changed.emit()
        
    def direction_changed_update(self):
        
        self.animation.refresh_animation()
        
    def move(self):
        dy = 0
        testfall = self.physics.check_collisions_y(self, self.scene, -1)
        if testfall is None:
            self.in_air = True
        
        if self.in_air:
            dv = self.physics.gravity()
            dy = self.vy-dv
        
            
        if self.direction == 'left':
            
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            if self.physics.check_edge(self,self.scene):
                self.change_direction()
                dx = self.speed
            
            elif xdetect is None:
                pass
            
            else:
                dx = xdetect
                self.change_direction()
            
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
            
            self.setPos(self.x()+dx, self.y()-dy)
            
        else:
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            if self.physics.check_edge(self,self.scene):
                self.change_direction()
                dx = self.speed
                
            elif xdetect is None:
                pass
            
            else:
                dx = xdetect
                self.change_direction()
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
            
            self.setPos(self.x()+dx, self.y())
            
            