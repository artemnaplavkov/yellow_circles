import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPainter, QColor
from random import randint

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('UI')
        self.pushButton.clicked.connect(self.yellow)

    def yellow(self):
        size = randint(10, 100)
        x = randint(0, self.label.width())
        y = randint(0, self.label.height())
        qp = QPainter()
        self.image = QImage(self.label.size(), 6)
        qp.begin(self.image)
        qp.setPen(QColor('yellow'))
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(x, y, size, size)
        qp.end()
        self.pixmap = QPixmap(self.image)
        self.label.setPixmap(self.pixmap)


        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
