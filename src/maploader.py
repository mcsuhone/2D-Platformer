from io import StringIO

from src.Blocks.blockgrass import BlockGrass
from src.Blocks.blockground import BlockGround
from src.Blocks.blockrock import BlockRock
from src.Blocks.spikes import Spikes
from src.derbiili import Derbiili
from src.Items.cake import Cake
from src.Items.grass import Grass
from src.Blocks.blockbox import BlockBox
from src.Blocks.portal import Portal
from src.Creatures.snake import Snake
from src.Creatures.bat import Bat
from src.Blocks.blockstonewall import BlockStoneWall
from src.Blocks.blockice import BlockIce

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
                        elif block == "O":
                            block = BlockStoneWall(x,y)
                            self.scene.addItem(block)
                        elif block == "I":
                            block = BlockIce(x,y)
                            self.scene.addItem(block)
                            
                            
                        x+=1
        self.map_info['ysize'] = y*32            
        