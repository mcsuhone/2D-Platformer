

class Physics():
    
    def __init__(self):
        self.g = 0.0
    
    
    def check_collision(self,player):
        
        list = player.collidingItems()
        
        
        if not list:
            return False
        else:
            return True
           
    def check_collision_direction(self,player,nearbyitems):
        #return a list of directions that object is colliding in
        
        directions = []
        
        for item in nearbyitems:
            if player.x() >= item.x():
                directions.append("left")
            if player.x() <= item.x():
                directions.append("right")
            if player.y() <= item.y():
                directions.append("down")
            if player.y() >= item.y():
                directions.append("up")
    
    def reset_gravity(self):
        self.g = 0.0
    
    def gravity(self,v):
        
        self.g -= 0.01
        
        v += self.g
        
        return v
        