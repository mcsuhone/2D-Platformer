from io import StringIO

from Blocks.blockgrass import BlockGrass
from Blocks.blockground import BlockGround
from Blocks.blockrock import BlockRock
from Blocks.spikes import Spikes
from derbiili import Derbiili
from Items.cake import Cake
from Items.grass import Grass
from Blocks.blockbox import BlockBox

class MapLoader():
    
    def load_map(self,scene,mapname):
        
        self.file = open(mapname,"r")
        self.scene = scene
        
        self.map = False
        self.title = False
        
        self.map_name = ""
        self.map_size = {'xsize':0,'ysize':0}
        
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
            return self.map_size
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
                            self.map_name = info[1].strip()
                
        
        
        
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
                    self.map_size['xsize'] = len(row)*32
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
                            derbiili = Derbiili(self.scene,x,y)
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
                        
                            
                        x+=1
        self.map_size['ysize'] = y*32            
        