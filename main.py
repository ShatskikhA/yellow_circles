import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QPoint
from PyQt6 import uic


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle
    ex.show()
    sys.exit(app.exec())
