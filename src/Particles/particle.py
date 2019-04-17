from PyQt5.Qt import QGraphicsRectItem, QTimer, QColor, QBrush
from physics import Physics
from CONSTANTS import *
import math

class Particle(QGraphicsRectItem):
    
    def __init__(self,scene,x,y,r,g,b,duration,direction,speed,parent=None):
        QGraphicsRectItem.__init__(self,parent)
        self.scene = scene
        
        self.timerbase = QTimer()
        self.timerbase.setInterval(10)
        self.timerbase.timeout.connect(self.update_particle)
        self.timerbase.start()
        
        self.timeout = QTimer()
        self.timeout.setSingleShot(True)
        self.timeout.setInterval(duration)
        self.timeout.timeout.connect(self.remove_particle)
        self.timeout.start()
        
        self.physics = Physics(5,5,0,1)
        self.in_air = False
        self.vy = 0
        self.vx = 0
        self.calculate_velocity(speed,direction)
        self.angle = direction
        self.friction = FRICTION
        self.setZValue(2)
        
        self.setRect(x,y,1,1)
        color = QColor(r,g,b)
        brush = QBrush(color)
        self.setBrush(brush)
        
    def X0(self):
        
        return self.x()
    
    def Y0(self):
        
        return self.y()
        
    def right_side(self):
        
        return 0
    
    def is_collidable(self):
        
        return False
        
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        pass
        
    def remove_particle(self):
        
        self.scene.removeItem(self)
        
    def calculate_velocity(self,speed,direction):
        
        direction = (direction*math.pi)/180
        
        self.vx = math.cos(direction)*speed
        self.vy = math.sin(direction)*speed
        
    def update_particle(self):
        
        dy = 0
        testfall = self.physics.check_collisions_y(self, self.scene, -1)
        if testfall is None:
            self.in_air = True
        
        if self.in_air:
            dv = self.physics.gravity()
            dy = self.vy-dv
            
        if self.vx >= 0:
            if self.in_air:
                dx = self.vx
                self.vx -= (self.friction)/3
            else:
                dx = self.vx
                self.vx -= self.friction
        else:
            if self.in_air:
                dx = self.vx
                self.vx += (self.friction)/3
            else:
                dx = self.vx
                self.vx += self.friction
        
        if dy <= 0:
            
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            if xdetect is None:
                pass
            
            else:
                dx = xdetect
                self.vx = 0.0  
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
                
        elif dy > 0:
            
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            if xdetect is None:
                pass
            else:
                dx = xdetect
                self.vx = 0.0
                
            if ydetect is None:
                pass
            else:
                dy = ydetect
                self.vy = 0.0
                self.physics.reset_gravity()
        
        self.setPos(self.x()+dx, self.y()-dy)
            
            