import sys
from scene import Scene
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()