from .enemy import Enemy
from PyQt5.Qt import QPixmap, QPointF
from animation import Animation


class FlyingEnemy(Enemy):
    
    def __init__(self, scene, speed, distance, parent=None):
        Enemy.__init__(self,scene,speed,distance,parent)
        
    def move(self):
        dx = 0
        dy = 0
        
        if self.direction == 'left':
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
            
            
            
            if self.distance_from_origin() > 32*self.distance:
                
                self.direction = 'right'
                self.speed = -self.speed
                dx = self.speed
                
            elif xdetect is None:
                pass 
            
            else:
                dx = xdetect
                self.direction = 'right'
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
                self.direction = 'left'
                self.speed = -self.speed
                dx = self.speed
            
            elif xdetect is None:
                pass
            
            else:
                dx = xdetect
                self.direction = 'left'
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
            