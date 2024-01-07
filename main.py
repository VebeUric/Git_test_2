import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MakeCircleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pushButton = None
        self.do_draw_flag = None
        self.IOput()

    def IOput(self):
        self.setWindowTitle('Рисовать круги2')
        self.setGeometry(200, 200, 900, 900)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(20, 20, 250, 50)
        self.pushButton.setText('Рисовать')
        self.pushButton.clicked.connect(self.do_draw)

    def do_draw(self):
        self.do_draw_flag = True
        self.update()

    def run(self, qp):
        rect_size = randint(10, 500)
        x = randint(0, 700)
        y = randint(0, 700)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setPen(QColor(r, g, b))
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, rect_size, rect_size)
        self.do_draw_flag = False
        qp.end()

    def paintEvent(self, event):
        if self.do_draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MakeCircleWindow()
    ex.show()
    sys.exit(app.exec_())
