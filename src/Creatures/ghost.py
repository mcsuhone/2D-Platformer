from .enemy import Enemy
from animation import Animation
from physics import Physics
from Creatures.flyingenemy import FlyingEnemy

class Ghost(FlyingEnemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.15
        distance = 10
        FlyingEnemy.__init__(self,scene,speed,distance,parent=parent)
        self.animation = Animation(self,"Textures/Ghost",300)
        self.size = self.calculate_size()
        self.set_pos(x,y-1)
        
        self.setOpacity(0.2)

    def set_physics(self):
        
        self.physics = Physics(height = 44, width = 28, offset = 2, weight = 1.0)
        
    def update(self,scene,player):
        
        distance = self.distance_from_player(player)
        x = (1/distance)**2
        self.setOpacity(1500*x)
        
        self.player_direction(player)
        
        if self.direction in self.player_tracker and 'infront' in self.player_tracker and distance < 32*5:
            self.animation.set_animation('anim1')
            if self.direction == 'left':
                self.speed = -1.0
            else:
                self.speed = 1.0
        else:
            self.animation.set_animation('default')
            if self.direction == 'left':
                self.speed = -0.15
            else:
                self.speed = 0.15
        
        self.move()