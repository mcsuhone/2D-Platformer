from PyQt5.Qt import QGraphicsPixmapItem, QPixmap
from .equipment import Equipment
from animation import Animation


class Crown(Equipment):
    
    def __init__(self,x,y, parent=None):
        
        Equipment.__init__(self,parent)
        self.animation = Animation(self, "Textures/Crown",500)
        self.set_pos(x,y)
        
    def set_pos(self,x,y):
        
        self.setPos(x*32+8,y*32+8)
        
    def update(self):
        
        player = self.get_player()
        
        if player.get_direction() == 'right':
            self.setPos(12,-3)
        else:
            self.setPos(4,-3)