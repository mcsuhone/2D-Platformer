from Creatures.enemy import Enemy
from PyQt5.Qt import QPainterPath, QRectF
from animation import Animation


class CaveBug(Enemy):
    
    def __init__(self,x,y, scene, parent=None):
        size = {'height':17,'width':25,'offset':4}
        speed = -0.4
        distance = 10
        Enemy.__init__(self,scene,speed,distance,collision=True,size=size,parent=parent)
        self.animation = Animation(self,"Textures/CaveBug",300)
        self.size = self.calculate_size()
        self.set_pos(x,y)
        
        self.shelled = False
        self.counter = 0
        
    def X0(self):
        
        return self.x() + 4
    
    def Y0(self):
        
        return self.y() + 15
    
    def right_side(self):
        
        return 7
        
    def shape(self):
        
        path = QPainterPath()
        rect = QRectF(4,15,25,17)
        path.addRect(rect)
        
        return path
        
    def stand_on_effect(self, player, scene):
        
        if not self.shelled:
            self.shelled = True
            player.jump(8)
        
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
            if self.counter >= 300:
                self.counter = 0
                self.shelled = False
                self.animation.set_animation('default')
                self.animation.refresh_animation()
        else:
            self.move()
    