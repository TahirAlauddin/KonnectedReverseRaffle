from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CircleWidget(QWidget):
    
    def __init__(self, circle_radius, text, parent=None, text_size=30, bg_color='lime', fg_color='white', border_color='black'):
        super().__init__()
        self.arrowSection = 0
        self.border_color = border_color       
        self.circle_radius = circle_radius
        self.background_color = bg_color
        self.text = text
        self.text_color = fg_color
        self.text_size = text_size

        super().__init__(parent)
        self.setMinimumSize(2 * circle_radius + 10, 2 * circle_radius + 10)  # Set minimum size to accommodate circle

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(QColor('transparent'), 1))

        # Draw circle
        painter.setBrush(QColor(self.background_color))
        painter.drawEllipse(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)

        # Draw text
        font = QFont()
        font.setPointSize(self.text_size)  # Adjust size as needed
        painter.setFont(font)
        painter.setPen(QColor(self.text_color))  # Set text color

        rect = QRectF(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)  # Adjust position as needed
        painter.drawText(rect, Qt.AlignCenter, str(self.text))


    def update_number(self, num):
        self.text = num
        self.update()  # Trigger a repaint of the widget




        

class CircleWidget(QWidget):

    def __init__(self, circle_radius, text, parent=None, text_size=30, bg_color='black', fg_color='white', border_color='white'):
        super().__init__(parent)

        self.circle_radius = circle_radius
        self.background_color = QColor(bg_color)
        self.border_color = QColor(border_color)
        self.text = text
        self.text_color = QColor(fg_color)
        self.text_size = text_size

        # Set up the Graphics View and Scene (Canvas)
        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # Draw ball
        self.draw_ball()

        # Set minimum size to accommodate circle
        self.setMinimumSize(2 * circle_radius + 10, 2 * circle_radius + 10)

    def draw_ball(self):
        # Draw outer circle
        outer_circle = QGraphicsEllipseItem(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)
        outer_circle.setBrush(self.background_color)
        outer_circle.setPen(self.border_color)
        self.scene.addItem(outer_circle)

        # Draw inner white circle
        inner_circle = QGraphicsEllipseItem(5 + self.circle_radius / 4, 5 + self.circle_radius / 4,
                                             1.5 * self.circle_radius, 1.5 * self.circle_radius)
        inner_circle.setBrush(QColor('white'))
        inner_circle.setPen(QColor('transparent'))
        self.scene.addItem(inner_circle)

        # Draw text
        font = QFont("Manrope", self.text_size)
        text_item = QGraphicsTextItem(self.text)
        text_item.setFont(font)
        text_item.setDefaultTextColor(self.text_color)
        text_item.setTextWidth(2 * self.circle_radius)
        text_item.setTextInteractionFlags(Qt.TextEditorInteraction)
        text_item.setPos(5, 5)
        text_item.setTextWidth(2 * self.circle_radius)
        text_item.setHtml(f'<div style="text-align:center;">{self.text}</div>')
        self.scene.addItem(text_item)

        # Keep a reference to text_item for later updates
        self.text_item = text_item

    def update_number(self, num):
        # Update the text in the ball
        self.text = str(num)
        self.text_item.setHtml(f'<div style="text-align:center;">{self.text}</div>')




class CircleWidget(QWidget):

    def __init__(self, circle_radius, text, parent=None, text_size=40, bg_color='black', fg_color='black', border_color='white'):
        super().__init__(parent)

        self.setStyleSheet('border: none;')

        self.circle_radius = circle_radius
        self.background_color = QColor(bg_color)
        self.background_color = QColor('black')
        self.border_color = QColor(border_color)
        self.text = text
        if fg_color in ['white', '#fff', '#FFF', '#FFFFFF']:
            fg_color = 'black'
        self.text_color = QColor(fg_color)
        self.text_size = text_size

        # Set up the Graphics View and Scene (Canvas)
        self.view = QGraphicsView(self)
         
        # Remove scrollbars
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.view.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # Draw ball
        self.draw_ball()

        # Set minimum size to accommodate circle
        self.setMinimumSize(2 * circle_radius + 10, 2 * circle_radius + 10)

    def draw_ball(self):

        # Draw outer circle
        outer_circle = QGraphicsEllipseItem(5, 5, 2 * self.circle_radius, 2 * self.circle_radius)
        outer_circle.setBrush(self.background_color)
        outer_circle.setPen(self.border_color)
        self.scene.addItem(outer_circle)

        # Draw intermediate white circle
        intermediate_radius_ratio = 0.85
        intermediate_circle_diameter = intermediate_radius_ratio * 2 * self.circle_radius
        intermediate_circle_pos_offset = (1 - intermediate_radius_ratio) * self.circle_radius
        intermediate_circle = QGraphicsEllipseItem(5 + intermediate_circle_pos_offset, 5 + intermediate_circle_pos_offset,
                                                intermediate_circle_diameter, intermediate_circle_diameter)
        intermediate_circle.setBrush(QColor('transparent'))
        intermediate_circle.setPen(QPen(QColor('white'), 12))  # 3px white border
        self.scene.addItem(intermediate_circle)

        # Draw inner white circle - smaller and centered within the outer circle
        inner_radius_ratio = 0.7  # Smaller ratio makes the white circle smaller
        inner_circle_diameter = inner_radius_ratio * 2 * self.circle_radius
        inner_circle_pos_offset = (1 - inner_radius_ratio) * self.circle_radius
        inner_circle = QGraphicsEllipseItem(5 + inner_circle_pos_offset, 5 + inner_circle_pos_offset,
                                            inner_circle_diameter, inner_circle_diameter)
        inner_circle.setBrush(QColor('white'))
        inner_circle.setPen(QColor('transparent'))
        self.scene.addItem(inner_circle)


        # Draw text
        font = QFont("Futura", self.text_size)
        text_item = QGraphicsTextItem(self.text)
        text_item.setFont(font)
        text_item.setDefaultTextColor(self.text_color)
        text_item.setTextWidth(2 * self.circle_radius)
        # text_item.setHtml(f'<div style="text-align:center; height:{self.circle_radius}px; line-height:{self.circle_radius}px;">{self.text}</div>')
        text_item.setPos(35, 47)
        self.scene.addItem(text_item)

        # Keep a reference to text_item for later updates
        self.text_item = text_item


    def update_number(self, num):
        # Update the text in the ball
        self.text = str(num)
        self.text_item.setPlainText(self.text)
        if len(self.text) == 1:
            self.text_item.setPos(68, 47)
        elif len(self.text) == 2:
            self.text_item.setPos(53, 47)
        else:
            self.text_item.setPos(40, 47)


