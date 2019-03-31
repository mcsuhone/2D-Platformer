import unittest
from physics import Physics
from PyQt5.Qt import QGraphicsPixmapItem
from texture import Texture


class Test(unittest.TestCase):
    
    def test_size_calculations(self):
        
        bottomside0 = 31
        topside0 = 9
        rightside0 = 27
        leftside0 = 5
        
        physics = Physics(height = 22, width = 23, offset = 5, weight = 1.0)
        bottomside1 = physics.bottom_side
        topside1 = physics.top_side
        rightside1 = physics.right_side
        leftside1 = physics.left_side
        
        self.assertEqual(bottomside1,bottomside0, "Bottom side is calculated wrong.")
        self.assertEqual(topside1,topside0, "Top side is calculated wrong.")
        self.assertEqual(rightside1,rightside0, "Right side is calculated wrong.")
        self.assertEqual(leftside1,leftside0, "Left side is calculated wrong.")
        
        #*************************************************************************************
        
        bottomside0 = 63
        topside0 = 13
        rightside0 = 53
        leftside0 = 10
        
        physics = Physics(height = 50, width = 44, offset = 10, weight = 1.0)
        bottomside1 = physics.bottom_side
        topside1 = physics.top_side
        rightside1 = physics.right_side
        leftside1 = physics.left_side
        
        self.assertEqual(bottomside1,bottomside0, "Bottom side is calculated wrong.")
        self.assertEqual(topside1,topside0, "Top side is calculated wrong.")
        self.assertEqual(rightside1,rightside0, "Right side is calculated wrong.")
        self.assertEqual(leftside1,leftside0, "Left side is calculated wrong.")

    '''
    def test_textures(self):
        
        object = QGraphicsPixmapItem()
        texture = Texture(object, "Textures/Derbiili/Derbiili.png")
        
        w = 1
        h = 1
        
        width = texture.width()
        height = texture.height()
        
        self.assertEqual(w, width, "Width was not correct.")
        self.assertEqual(h, height, "Height was not correct.")
    '''  
if __name__ == '__main__':
    unittest.main()