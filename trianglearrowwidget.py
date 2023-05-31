import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TriangleArrowWidget(QWidget):
    def __init__(self, bg_color='lime', fg_color='white', border_color='black'):
        super().__init__()
        self.arrowSection = 0
        self.background_color = bg_color
        self.foreground_color = fg_color
        self.border_color = border_color

    def sizeHint(self):
        return QSize(280, 270)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawTriangle(qp)
        self.drawArrow(qp, self.arrowSection)
        qp.end()

    def drawTriangle(self, qp):
        points = [QPoint(10, 5), QPoint(160, 5), QPoint(85, 205)]
        qp.setPen(QPen(QColor(self.border_color), 2))
        qp.setBrush(QColor(self.background_color))
        qp.drawPolygon(QPolygon(points))

        lines_y = [45, 85, 125, 165]
        section_values = ["300", "200", "100", "50"]
        qp.setFont(QFont('Arial', 10))
        qp.setBrush(QColor(self.foreground_color))
        qp.setPen(QPen(QColor(self.foreground_color), 2))

        for i, y in enumerate(lines_y):
            qp.drawLine(QPoint(5, y), QPoint(155, y))
            qp.drawText(QPoint(76, y - 10), section_values[i])

    def drawArrow(self, qp, section):
        lines_y = [25, 65, 105, 145, 185]
        points = [QPoint(10, lines_y[section]), QPoint(0, lines_y[section]-10), QPoint(0, lines_y[section]+10)]
        qp.setPen(QPen(QColor(self.border_color), 2))
        qp.setBrush(QColor(Qt.black))
        qp.drawPolygon(QPolygon(points))

    def moveArrow(self, section):
        if 0 <= section < 5:
            self.arrowSection = section
            self.update()

def main():
    app = QApplication(sys.argv)
    ex = TriangleArrowWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
