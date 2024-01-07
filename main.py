import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MakeCircleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.do_draw_flag = None
        uic.loadUi('UI.ui', self)
        self.IOput()

    def IOput(self):
        self.pushButton.clicked.connect(self.do_draw)

    def do_draw(self):
        self.do_draw_flag = True
        self.update()

    def run(self, qp):
        rect_size = randint(10, 500)
        x = randint(0, 700)
        y = randint(0, 700)
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
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
