from .enemy import Enemy
from PyQt5.Qt import QPixmap, QPointF
from src.animation import Animation


class Bat(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.6
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/Bat",10)
        self.addPos(x,y)
    
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
        self.origin = QPointF(x*32,y*32)
    
    def distance_from_origin(self):
        
        return abs(self.origin.x()-self.x())
    
    def move(self):
        dx = 0
        dy = 0
        
        if self.direction == -1:
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            
            
            if self.distance_from_origin() > 32*self.distance:
                
                self.direction = 1
                self.speed = -self.speed
                dx = self.speed
                
            elif xdetect is None:
                pass 
            
            else:
                dx = xdetect
                self.direction = -self.direction
                self.speed = -self.speed
            
            if ydetect is None:
                pass
            
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
            
            self.animation.animate(self,self.direction)
            self.setPos(self.x()+dx, self.y()-dy)
            
        else:
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)

            if self.distance_from_origin() > 32*self.distance:
                self.direction = -1
                self.speed = -self.speed
                dx = self.speed
            
            elif xdetect is None:
                pass
            
            else:
                dx = xdetect
                self.direction = -1
                self.speed = -self.speed
                
            if ydetect is None:
                pass
            
            else:
                dy = ydetect
                self.vy = 0.0
                self.in_air = False
                self.physics.reset_gravity()
            
            self.animation.animate(self,self.direction)
            self.setPos(self.x()+dx, self.y())
            