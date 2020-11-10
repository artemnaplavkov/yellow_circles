import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QPushButton
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPainter, QColor
from random import randint
from random import randrange

def get_color():
    color = QColor()
    color.setRed(randrange(256))
    color.setGreen(randrange(256))
    color.setBlue(randrange(256))
    return color

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.yellow)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('UI')
        self.pushButton = QPushButton('pushButton', self)
        self.label = QLabel('', self)
        self.label.setGeometry(0, self.pushButton.height(), self.width(), self.height())
        self.show()

    def yellow(self):
        size = randint(10, 100)
        x = randint(0, self.label.width())
        y = randint(0, self.label.height())
        color = get_color()
        qp = QPainter()
        self.image = QImage(self.label.size(), 6)
        qp.begin(self.image)
        qp.setPen(color)
        qp.setBrush(color)
        qp.drawEllipse(x, y, size, size)
        qp.end()
        self.pixmap = QPixmap(self.image)
        self.label.setPixmap(self.pixmap)


        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
