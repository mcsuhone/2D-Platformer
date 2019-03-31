import os
from PyQt5.Qt import QPixmap


class Animation():
    
    def __init__(self,object,folder,delay):
        
        self.current_frame = 0
        self.delay = delay
        self.timer = 0
        self.load_animations(folder)
        object.setPixmap(self.frames[0])
        
        self.width = self.frames[0].width()
        self.height = self.frames[0].height()
        
    def get_width(self):
        
        return self.width/32
    
    def get_height(self):
        
        return self.height/32
        
    def load_animations(self,folder):
        self.frames = []
        self.flippedframes = []
        
        for file in os.listdir(folder):
            if file.endswith(".png"):
                if 'Flipped' in file:
                    str = folder + "/" + file
                    pixmap = QPixmap(str)
                    self.flippedframes.append(pixmap)
                else:
                    str = folder + "/" + file
                    pixmap = QPixmap(str)
                    self.frames.append(pixmap)
            elif file == 'anim1':
                self.anim1 = []
        
        
    def next_frame(self,direction):
        
        self.current_frame += 1
        if direction is None:
            if len(self.frames) <= self.current_frame:
                self.current_frame = 0
                    
            return self.frames[self.current_frame]
        
        else:
            if direction == 1:
                if len(self.frames) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.frames[self.current_frame]
            
            elif direction == -1:
                if len(self.frames) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.flippedframes[self.current_frame]
                
                
    def animate(self,object,direction=None):
        
        self.timer += 1
        if self.timer == self.delay:
            self.timer = 0
            object.setPixmap(self.next_frame(direction))
        
            
            
            
        
        
        
        
    