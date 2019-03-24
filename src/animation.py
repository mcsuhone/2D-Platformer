import os
from PyQt5.Qt import QPixmap




class Animation():
    
    def __init__(self,object,folder,delay):
        
        self.current_frame = 0
        self.delay = delay
        self.timer = 0
        self.load_animation_frames(folder)
        object.setPixmap(self.frames[0])
        
    def load_animation_frames(self,folder):
        self.frames = []
        
        for file in os.listdir(folder):
            if file.endswith(".png"):
                str = folder + "/" + file
                pixmap = QPixmap(str)
                self.frames.append(pixmap)
    
    def next_frame(self):
        
        self.current_frame += 1
        if len(self.frames) <= self.current_frame:
            self.current_frame = 0
        
        return self.frames[self.current_frame]
    
    def animate(self,object):
        
        self.timer += 1
        if self.timer == self.delay:
            self.timer = 0
            object.setPixmap(self.next_frame())
        
        
        
        
    