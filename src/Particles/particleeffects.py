from .particle import Particle
from PyQt5.Qt import QTimer



class ParticleEffects():
    
    def __init__(self,player,scene):
        
        self.timer = QTimer()
        self.timer.setInterval(150)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.player_run_particle)
        self.timer_running = False
        
        self.scene = scene
        self.player = player
    
    def player_run_init(self):
        
        if not self.timer_running:
            self.timer_running = True
            self.timer.start()
        
    def player_run_particle(self):
        
        self.timer_running = False
        x = self.player.x()
        y = self.player.y() + 30
        r = 255
        g = 0
        b = 0
        if self.player.get_direction() == 'right':
            particle = Particle(self.scene,x,y,r,g,b,4000,90,16.3)
            self.scene.addItem(particle)
        else:
            x += 32
            particle = Particle(self.scene,x,y,r,g,b,4000,90,16.3)
            self.scene.addItem(particle)
            
            
            
        