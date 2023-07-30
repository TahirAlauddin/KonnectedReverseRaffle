import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

NUMBER_TO_LIST_DICT = {
    50: ["50", "40", "30", "10"],
    60: ["60", "40", "20", "10"],
    70: ["70", "40", "20", "10"],
    80: ["80", "50", "30", "10"],
    90: ["90", "60", "30", "10"],
    100: ["100", "70", "40", "20"],
    150: ["150", "100", "50"],
    200: ["200", "150", "100", "50"],
    250: ["250", "150", "100", "50"],
    300: ["300", "200", "100", "50"]
}

class TriangleArrowWidget(QWidget):
    def __init__(self, bg_color='lime', fg_color='white', border_color='black', num_list=["300", "200", "100", "50"]):
        super().__init__()
        self.arrowSection = 0
        self.background_color = bg_color
        self.foreground_color = fg_color
        self.border_color = border_color
        self.num_list = num_list

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

        triangle_height = 200  # Assume the height of the triangle is 165
        section_values = self.num_list
        number_of_sections = len(section_values)  # Divide the triangle into 4 sections

        lines_y = self.generate_lines_y(triangle_height, number_of_sections)
        qp.setFont(QFont('Manrope', 12))
        qp.setBrush(QColor(self.foreground_color))
        qp.setPen(QPen(QColor(self.foreground_color), 2))

        for i, y in enumerate(lines_y):
            qp.drawLine(QPoint(5, y), QPoint(155, y))
            if i == 3 and len(section_values) == 3:
                continue
            qp.drawText(QPoint(76, y - 10), section_values[i])

        #! May remove this line
        # self.calculate_intersection_points_line_triangle()

            
    def line_intersection(self, p1, p2, q1, q2):
        # Line p1-p2 represented as a1*x + b1*y = c1
        a1 = p2.y() - p1.y()
        b1 = p1.x() - p2.x()
        c1 = a1 * p1.x() + b1 * p1.y()

        # Line q1-q2 represented as a2*x + b2*y = c2
        a2 = q2.y() - q1.y()
        b2 = q1.x() - q2.x()
        c2 = a2 * q1.x() + b2 * q1.y()

        determinant = a1 * b2 - a2 * b1

        # If determinant is 0, lines are parallel or coincident
        if determinant == 0:
            return None  # No intersection

        # Find intersection point
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

        return QPoint(x, y)

    def find_intersections(self, triangle_points, line_points):
        intersections = []

        # Loop through each side of the triangle
        for i in range(3):
            # Points of the side of the triangle
            p1 = triangle_points[i]
            p2 = triangle_points[(i + 1) % 3]

            # Points of the line
            q1 = line_points[0]
            q2 = line_points[1]

            # Find intersection
            intersection = self.line_intersection(p1, p2, q1, q2)

            # Check if intersection is within segment of triangle side
            if intersection and min(p1.x(), p2.x()) <= intersection.x() <= max(p1.x(), p2.x()) and \
                            min(p1.y(), p2.y()) <= intersection.y() <= max(p1.y(), p2.y()):
                intersections.append(intersection)

        return intersections

    def calculate_intersection_points_line_triangle(self):
        # Example usage
        triangle_points = [QPoint(10, 5), QPoint(160, 5), QPoint(85, 205)]
        line_points = [QPoint(5, 46), QPoint(155, 46)]

        intersection_points = self.find_intersections(triangle_points, line_points)
        for point in intersection_points:
            print(f"Intersection at: ({point.x()}, {point.y()})")

    def generate_lines_y(self, triangle_height, number_of_sections):
        # Calculate the distance between lines
        distance_between_lines = triangle_height / number_of_sections 
        if number_of_sections == 3:
            distance_between_lines -= 20
        else:
            distance_between_lines -= 10
        # Generate y coordinates for each line
        return [int(distance_between_lines * i)  for i in range(1, number_of_sections + 1)]


    def drawArrow(self, qp, section):
        lines_y = [25, 65, 105, 145, 185]
        points = [QPoint(10, lines_y[section]), QPoint(0, lines_y[section]-10), QPoint(0, lines_y[section]+10)]
        qp.setPen(QPen(QColor(self.foreground_color), 2))
        qp.setBrush(QColor(self.foreground_color))
        qp.drawPolygon(QPolygon(points))


    def moveArrow(self, section):
        if 0 <= section < 5:
            self.arrowSection = section
            self.update()

    def moveArrowRelatively(self, moveByHowMuch: int):
        self.arrowSection += moveByHowMuch
        if self.arrowSection < 5:
            self.update()


def main():
    app = QApplication(sys.argv)
    ex = TriangleArrowWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
