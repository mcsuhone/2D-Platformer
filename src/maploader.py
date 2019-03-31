from io import StringIO

from Blocks.blockgrass import BlockGrass
from Blocks.blockground import BlockGround
from Blocks.blockrock import BlockRock
from Blocks.spikes import Spikes
from derbiili import Derbiili
from Items.cake import Cake
from Items.grass import Grass
from Blocks.blockbox import BlockBox
from Blocks.portal import Portal
from Creatures.snake import Snake
from Creatures.bat import Bat
from Blocks.blockstonewall import BlockStoneWall
from Blocks.blockice import BlockIce
from Creatures.cavebug import CaveBug
from Creatures.ghost import Ghost

class MapLoader():
    
    def load_map(self,scene,maps,number):
        
        self.file = open(maps[number],"r")
        self.scene = scene
        
        self.map = False
        self.title = False
        
        self.map_info = {'xsize':0,'ysize':0,'currentlevel':number}
        
        self.current_line = ''
        
        while True:
            if self.current_line.startswith("#"):
                self.current_line = self.current_line.strip()
                self.current_line = self.current_line.lower()
            else:
                self.current_line = self.file.readline()
                if self.current_line == "":
                    break
                else:
                    self.current_line = self.current_line.strip()
                    self.current_line = self.current_line.lower()
                    
            if self.current_line == "":
                pass
            elif self.current_line == "#title":
                self.titlereader()
                self.title = True
                
            elif self.current_line == "#map":
                self.mapreader()
                self.map = True
                
            else:
                pass
            
        if self.map and self.title:
            return self.map_info
        else:
            print("Map information missing.")
                
    
    def titlereader(self):
        
        while True:
            self.current_line = self.file.readline()
            if self.current_line == "" or self.current_line.startswith("#"):
                break
            else:
                self.current_line = self.current_line.strip()
                self.current_line = self.current_line.lower()
                
                if self.current_line == "":
                    pass
                else:
                    info = self.current_line.split("=")
                    if len(info) != 2:
                        pass
                    else:
                        if info[0].strip() == "name":
                            self.map_info['name'] = info[1].strip()
                        elif info[0].strip() == "backgroundgradient":
                            gradients = info[1].split("-")
                            gradient1 = gradients[0].split(",")
                            gradient2 = gradients[1].split(",")
                            
                            gradient1 = list(map(int, gradient1))
                            gradient2 = list(map(int, gradient2))
                            
                            self.map_info['background'] = [gradient1,gradient2]
                        elif info[0].strip() == "backgroundpixmap":
                            self.map_info['backgroundpixmap'] = info[1].strip()
        
    def mapreader(self):
        
        y=0
        while True:
            self.current_line = self.file.readline()
            if self.current_line == "" or self.current_line.startswith("#"):
                break
            else:
                self.current_line = self.current_line.strip()
                
                if self.current_line == "":
                    pass
                else:
                    y+=1
                    row = self.current_line.split(":")
                    self.map_info['xsize'] = len(row)*32
                    x=0
                    for block in row:
                        if block == "0":
                            pass
                        elif block == "g":
                            block = BlockGrass(x,y)
                            self.scene.addItem(block)
                        elif block == "d":
                            block = BlockGround(x,y)
                            self.scene.addItem(block)
                        elif block == "s":
                            block = BlockRock(x,y)
                            self.scene.addItem(block)
                        elif block == "X":
                            derbiili = Derbiili(x,y,self.scene)
                            self.scene.addItem(derbiili)
                            self.scene.addDerbiili(derbiili)
                        elif block == "C":
                            item = Cake(x,y)
                            self.scene.addItem(item)
                        elif block == "G":
                            item = Grass(x,y)
                            self.scene.addItem(item)
                        elif block == "M":
                            block = Spikes(x,y)
                            self.scene.addItem(block)
                        elif block == "b":
                            block = BlockBox(x,y)
                            self.scene.addItem(block)
                        elif block == "P":
                            block = Portal(x,y)
                            self.scene.addItem(block)
                        elif block == "1":
                            enemy = Snake(x,y,self.scene)
                            self.scene.addItem(enemy)
                        elif block == "2":
                            enemy = Bat(x,y,self.scene)
                            self.scene.addItem(enemy)
                        elif block == "3":
                            enemy = CaveBug(x,y,self.scene)
                            self.scene.addItem(enemy)
                        elif block == "4":
                            enemy = Ghost(x,y,self.scene)
                            self.scene.addItem(enemy)
                        elif block == "O":
                            block = BlockStoneWall(x,y)
                            self.scene.addItem(block)
                        elif block == "I":
                            block = BlockIce(x,y)
                            self.scene.addItem(block)
                            
                            
                        x+=1
        self.map_info['ysize'] = y*32            
        