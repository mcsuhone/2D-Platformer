from Creatures.enemy import Enemy
from PyQt5.Qt import QPixmap
from animation import Animation


class CaveBug(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,parent)
        self.animation = Animation(self,"Textures/CaveBug",15)
        self.size = self.calculate_size()
        self.set_pos(x,y)
        
        self.shelled = False
        self.counter = 0
        
    def stand_on_effect(self, player, scene):
        
        self.shelled = True
        player.jump()
        
    def touch_effect(self, player, scene):
        
        player.is_standing_on(5)
        
        if self.shelled:
            pass
        else:
            scene.back_to_checkpoint()
            
        
    def update(self,scene,player):
        
        if self.shelled:
            self.counter += 1
            self.animation.set_animation('anim1')
            self.animation.animate(self,self.direction)
            if self.counter >= 300:
                self.counter = 0
                self.shelled = False
        else:
            self.animation.set_animation('default')
            self.move()
    