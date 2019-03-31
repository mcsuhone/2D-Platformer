from .enemy import Enemy
from animation import Animation
from physics import Physics


class Ghost(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/Ghost",25)
        self.set_pos(x,y-1)
        
    def set_physics(self):
        
        self.physics = Physics(height = 60, width = 19, offset = 8, weight = 1.0)
        print(self.physics.left_side,self.physics.right_side,self.physics.top_side,self.physics.bottom_side)