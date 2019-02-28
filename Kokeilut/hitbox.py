'''
import scene


class HitBox():
    
    def __init__(self,type,x,y):
        
        self.hitboxes = []
        
        if type == "Block":
            self.hitbox = self.rectangle(x,y,scene.SQUARE_SIZE)
            self.set_center()
            self.hitboxes.append(self.hitbox)
        
        elif type == "Player":
            self.hitbox = self.rectangle(x,y,scene.PLAYER_SIZE)
        
        
        
    def rectangle(self,x,y,size):
        
        hitbox = {'type':'rectangle','x':x,'y':y,'size':size,'x2':x+size,'y2':y+size}
        
        return hitbox
        
    def ellipse(self,x,y):
        pass
        
    def set_center(self):
        
        if self.hitbox['type'] == 'rectangle':
            
            center = [self.hitbox['x']+(self.hitbox['size']/2), self.hitbox['y']+(self.hitbox['size']/2)]
            self.hitbox['center'] = center
            
        else:
            pass
        
    def move(self,dx,dy):
        
        self.hitbox['x'] += dx
        self.hitbox['y'] += dy
                
    def check_collision(self):
        
        for hitbox in self.hitboxes:
            if hitbox['x'] <= self.hitbox['x2'] <= hitbox['x']*2*hitbox['size'] and self.hitbox['y2'] == hitbox['y']:
                return True
            
            if hitbox['y'] <= self.hitbox['y2'] <= hitbox['y']*2*hitbox['size'] and self.hitbox['x2'] == hitbox['x']:
                return True
    
            if hitbox['x2']*2*hitbox['size'] <= self.hitbox['x'] <= hitbox['x2'] and self.hitbox['y'] == hitbox['y2']:
                return True
            
            if hitbox['y2']*2*hitbox['size'] <= self.hitbox['y'] <= hitbox['y2'] and self.hitbox['x'] == hitbox['x2']:
                return True
        
        return False
'''