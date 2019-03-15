from Enemies.enemy import Enemy
from PyQt5.Qt import QPixmap, QPointF


class Bat(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.5
        Enemy.__init__(self,scene,speed,parent)
        self.setPixmap(QPixmap("Textures\Bat.png"))
        self.addPos(x,y)
    
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
        self.origin = QPointF(x*32,y*32)
    
    def distance_from_origin(self,dx):
        
        return abs(self.origin.x()-self.x())
    
    def move(self):
        dy = 0
        
        
        if self.direction == -1:
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
                
            if xdetect is None:
                pass
            
            elif self.distance_from_origin > 32*5:
                self.direction = -self.direction
                self.speed = -self.speed
                
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
                
            self.setPos(self.x()+dx, self.y()-dy)
            
        else:
            dx = self.speed
            xdetect = self.physics.check_collisions_x(self,self.scene,dx)
            ydetect = self.physics.check_collisions_y(self,self.scene,dy)
                
            if xdetect is None:
                pass
            
            elif self.distance_from_origin > 32*5:
                self.direction = -self.direction
                self.speed = -self.speed
                
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
                
            self.setPos(self.x()+dx, self.y())
            