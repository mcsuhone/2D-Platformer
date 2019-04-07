import os
from PyQt5.Qt import QPixmap


class Animation():
    
    ANIMATION_TYPES = ['default','anim1','anim2','animdeath','animattack']
    
    def __init__(self,object,folder,delay):
        
        self.defaultanim = {}
        self.current_frame = 0
        self.defaultanim['delay'] = delay
        self.timer = 0
        self.load_animations(folder)
        self.object = object
        self.object.setPixmap(self.defaultanim['frames'][0])
        
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
                self.anim1 = {'delay':1}
                
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
                
            elif file == 'anim2':
                self.anim2 = {'delay':1}
                
                anim2flippedframes = []
                anim2frames = []
                dir = folder + "/" + file
                
                for file in os.listdir(dir):
                    if 'Flipped' in file:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        anim2flippedframes.append(pixmap)
                    elif file.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        anim2frames.append(pixmap)
                        
                self.anim2['frames'] = anim1frames
                self.anim2['flippedframes'] = anim1flippedframes
                
            elif file == 'animdeath':
                self.animdeath = {'delay':1}
                
                animdeathflippedframes = []
                animdeathframes = []
                dir = folder + "/" + file
                
                for file in os.listdir(dir):
                    if 'Flipped' in file:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        animdeathflippedframes.append(pixmap)
                    elif file.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        animdeathframes.append(pixmap)
                        
                self.animdeath['frames'] = anim1frames
                self.animdeath['flippedframes'] = anim1flippedframes
                
            elif file == 'animattack':
                self.animattack = {'delay':1}
                
                animattackflippedframes = []
                animattackframes = []
                dir = folder + "/" + file
                
                for file in os.listdir(dir):
                    if 'Flipped' in file:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        animattackflippedframes.append(pixmap)
                    elif file.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + file
                        pixmap = QPixmap(str)
                        animattackframes.append(pixmap)
                        
                self.animattack['frames'] = anim1frames
                self.animattack['flippedframes'] = anim1flippedframes
                
            self.defaultanim['frames'] = frames
            self.defaultanim['flippedframes'] = flippedframes
            
    def get_animations(self):
            
        if self.current_animation == 'default':
            return self.defaultanim
        elif self.current_animation == 'anim1':
            return self.anim1
        elif self.current_animation == 'anim2':
            return self.anim2
        elif self.current_animation == 'animdeath':
            return self.animdeath
        elif self.current_animation == 'animattack':
            return self.animattack
        
    def next_frame(self,direction):
        
        self.current_frame += 1
        animations = self.get_animations()
        
        if direction is None:
            if len(animations['frames']) <= self.current_frame:
                self.current_frame = 0
            
            return animations['frames'][self.current_frame]
        
        else:
            if direction == 'right':
                if len(animations['frames']) <= self.current_frame:
                    self.current_frame = 0
                    
                return animations['frames'][self.current_frame]
            
            elif direction == 'left':
                if len(animations['flippedframes']) <= self.current_frame:
                    self.current_frame = 0
                    
                return animations['flippedframes'][self.current_frame]
    
    def animate(self,direction=None):
        animations = self.get_animations()
        
        self.timer += 1
        if self.timer >= animations['delay']:
            self.timer = 0
            self.object.setPixmap(self.next_frame(direction))
        
    def instantanimate(self,animation,direction=None):
        animations = self.get_animations()
        
        self.set_animation(animation)
        self.timer = 1000
        self.animate(direction)
        self.timer = animations['delay']
    