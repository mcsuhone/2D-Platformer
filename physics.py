

class Physics():
    
    def __init__(self):
        self.g = 0.0
    
    def check_collision(self,scene,player):
        ground = scene.get_ground()
        
        if player.collidesWithItem(ground):
            return True
        else:
            return False
    
    def reset_gravity(self):
        self.g = 0.0
    
    def gravity(self,v):
        
        self.g -= 0.25
        v += self.g
        
        return v
        