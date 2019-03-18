from PyQt5.Qt import QGraphicsPixmapItem, QPointF

from physics import Physics

class Enemy(QGraphicsPixmapItem):
    
    def __init__(self, scene, speed = -1.0, distance = 1.0, collision = True, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.collision = collision
        
        self.speed = speed
        self.in_air = False
        self.vy = 0.0
        self.direction = -1
        self.distance = distance
        
        self.physics = Physics()
        self.scene = scene
    
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
        self.origin = QPointF(x*32,y*32)
        
    def stand_on_effect(self,player,scene):
        
        return False
    
    def touch_effect(self,player,scene):
        
        scene.death_screen()
    
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision
    
    def distance_from_origin(self):
        
        return abs(self.origin.x()-self.x())
    
    def flip(self,direction):
        #overwrite this.
        pass
    
    def move(self):
        dy = 0
        testfall = self.physics.check_collisions_y(self, self.scene, -1)
        if testfall is None:
            self.in_air = True
        
        if self.in_air:
            dv = self.physics.gravity()               #continue air movement
            dy = self.vy-dv
        
        if self.direction == -1:
            self.flip(self.direction)
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
                self.direction = 1
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
            self.flip(self.direction)
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
                
            self.setPos(self.x()+dx, self.y())
            
            
            
            
            
            
            
            