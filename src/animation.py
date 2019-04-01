import os
from PyQt5.Qt import QPixmap


class Animation():
    
    def __init__(self,object,folder,delay):
        
        self.defaultanim = {}
        self.current_frame = 0
        self.defaultanim['delay'] = delay
        self.timer = 0
        self.load_animations(folder)
        object.setPixmap(self.defaultanim['frames'][0])
        
        self.current_animation = 'default'
        
    def set_animation(self,animation):
        
        self.current_animation = animation
        
    def load_animations(self,folder):
        frames = []
        flippedframes = []
        
        for file in os.listdir(folder):
            if file.endswith(".png"):
                if 'Flipped' in file:
                    str = folder + "/" + file
                    pixmap = QPixmap(str)
                    flippedframes.append(pixmap)
                else:
                    str = folder + "/" + file
                    pixmap = QPixmap(str)
                    frames.append(pixmap)
                    
            elif file == 'anim1':
                self.anim1 = {'delay':15}
                
                anim1flippedframes = []
                anim1frames = []
                dir = folder + "/" + file
                
                for file in os.listdir(dir):
                    if 'Flipped' in file:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        anim1flippedframes.append(pixmap)
                    elif file.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        anim1frames.append(pixmap)
                        
                self.anim1['frames'] = anim1frames
                self.anim1['flippedframes'] = anim1flippedframes
                        
            self.defaultanim['frames'] = frames
            self.defaultanim['flippedframes'] = flippedframes
            
    def next_frame(self,direction):
        
        self.current_frame += 1
        if direction is None:
            if len(self.defaultanim['frames']) <= self.current_frame:
                self.current_frame = 0
                    
            return self.defaultanim['frames'][self.current_frame]
        
        else:
            if direction == 'right':
                if len(self.defaultanim['frames']) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.defaultanim['frames'][self.current_frame]
            
            elif direction == 'left':
                if len(self.defaultanim['flippedframes']) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.defaultanim['flippedframes'][self.current_frame]
              
    def animate_anim1(self,direction):
        
        self.current_frame += 1
        if direction is None:
            if len(self.anim1['frames']) <= self.current_frame:
                self.current_frame = 0
                    
            return self.anim1['frames'][self.current_frame]
        
        else:
            if direction == 'right':
                if len(self.anim1['frames']) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.anim1['frames'][self.current_frame]
            
            elif direction == 'left':
                if len(self.anim1['flippedframes']) <= self.current_frame:
                    self.current_frame = 0
                    
                return self.anim1['flippedframes'][self.current_frame]
    
    def animate(self,object,direction=None):
        self.timer += 1
        if self.current_animation == 'default':
            if self.timer >= self.defaultanim['delay']:
                self.timer = 0
                object.setPixmap(self.next_frame(direction))
        elif self.current_animation == 'anim1':
            if self.timer >= self.anim1['delay']:
                self.timer = 0
                object.setPixmap(self.animate_anim1(direction))
        
    