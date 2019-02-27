import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QBrush,QColor
from PyQt5 import QtGui

class Window(QWidget,QtGui):
    def __init__(self):
        super().__init__()
        self.title = 'Hill climb'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
        self.scene = QtGui.QGraphicsScene(self)
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
    def BackGround(self):
        color = QColor(211,211,211)
        brush = QBrush(color)
        
        self.scene.addItem(square)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())