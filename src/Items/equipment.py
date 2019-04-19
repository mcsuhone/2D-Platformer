from PyQt5.Qt import QGraphicsPixmapItem, QPixmap
from .item import Item


class Equipment(Item):
    
    def __init__(self, parent=None):
        Item.__init__(self,parent)
        self.equipped = False
        self.player = None
        
    def get_player(self):
        
        return self.player
        
    def is_collidable(self):
        
        if self is None:
            return False
        else:
            return self.collision
        
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        if not self.equipped:
            self.pick_up(player)
            
    def pick_up(self,player):
        
        self.equipped = True
        self.setParentItem(player)
        self.player = player
        self.player.add_equipment(self,'Crown')
        
        self.update()
        
    def update(self):
        
        pass