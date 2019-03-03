import sys
from scene import Scene
from menu import Menu
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()