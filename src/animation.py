import os
from PyQt5.Qt import QPixmap, QTimer
from signals import Signals

class Animation():
    
    ANIMATION_TYPES = ['default','anim1','anim2','animdeath','animattack']
    
    def __init__(self,object,folder,delay):
        
        self.timer = QTimer()
        self.timer.setInterval(delay)
        self.timer.timeout.connect(self.animate)
        self.timer.start()
        
        self.current_frame = 0
        self.object = object
        self.load_animations(folder)
        self.current_animation = 'default'
        self.signals = Signals()
        self.signals.animation_changed.connect(self.refresh_animation)
        
        self.object.setPixmap(self.defaultanim['frames'][0])
        
    def load_animations(self,folder):
        self.defaultanim = {}
        
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
                
                for tex in os.listdir(dir):
                    if 'Flipped' in tex:
                        str = dir + "/" + tex
                        pixmap1 = QPixmap(str)
                        anim1flippedframes.append(pixmap1)
                    elif tex.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + tex
                        pixmap2 = QPixmap(str)
                        anim1frames.append(pixmap2)
                        
                self.anim1['frames'] = anim1frames
                self.anim1['flippedframes'] = anim1flippedframes
                self.anim1['animation'] = 'anim1'
                
            elif file == 'anim2':
                self.anim2 = {'delay':1}
                
                anim2flippedframes = []
                anim2frames = []
                dir = folder + "/" + file
                
                for tex in os.listdir(dir):
                    if 'Flipped' in tex:
                        str = dir + "/" + tex
                        pixmap3 = QPixmap(str)
                        anim2flippedframes.append(pixmap3)
                    elif tex.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + tex
                        pixmap4 = QPixmap(str)
                        anim2frames.append(pixmap4)
                        
                self.anim2['frames'] = anim2frames
                self.anim2['flippedframes'] = anim2flippedframes
                self.anim2['animation'] = 'anim2'
                
            elif file == 'animdeath':
                self.animdeath = {'delay':1}
                
                animdeathflippedframes = []
                animdeathframes = []
                dir = folder + "/" + file
                
                for tex in os.listdir(dir):
                    if 'Flipped' in tex:
                        str = dir + "/" + tex
                        pixmap5 = QPixmap(str)
                        animdeathflippedframes.append(pixmap5)
                    elif tex.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + tex
                        pixmap6 = QPixmap(str)
                        animdeathframes.append(pixmap6)
                        
                self.animdeath['frames'] = animdeathframes
                self.animdeath['flippedframes'] = animdeathflippedframes
                self.animdeath['animation']= 'death'
                
            elif file == 'animattack':
                self.animattack = {'delay':1}
                
                animattackflippedframes = []
                animattackframes = []
                dir = folder + "/" + file
                
                for tex in os.listdir(dir):
                    if 'Flipped' in tex:
                        str = dir + "/" + tex
                        pixmap7 = QPixmap(str)
                        animattackflippedframes.append(pixmap7)
                    elif tex.endswith(".txt"):
                        pass
                    else:
                        str = dir + "/" + tex
                        pixmap8 = QPixmap(str)
                        animattackframes.append(pixmap8)
                        
                self.animattack['frames'] = animattackframes
                self.animattack['flippedframes'] = animattackflippedframes
                self.animattack['animation':'attack']
                
            self.defaultanim['frames'] = frames
            self.defaultanim['flippedframes'] = flippedframes
            self.defaultanim['animation'] = 'default'
            
    def start_animation(self):
        
        self.timer.start()
        
    def stop_animation(self):
        
        self.timer.stop()
    
    def animate(self):
        
        self.object.setPixmap(self.next_frame())
        
    def next_frame(self):
        self.current_frame += 1
        animations = self.get_animations()
        
        try:
            direction = self.object.get_direction()
        except:
            direction = None
        
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
        
    def refresh_animation(self):
        
        self.object.setPixmap(self.next_frame())
        
    def set_animation(self,animation):
        
        self.current_animation = animation
    
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

        
        