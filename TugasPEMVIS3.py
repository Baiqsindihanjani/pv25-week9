import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Task Week 3 - (F1D022115 - Baiq Sindi Hanjani)')

        self.label = QLabel(self)
        self.label.setStyleSheet(                        
            'color: white; '
            'background-color: blue; '
            'font-size: 16px; '
            'border-radius: 5px;'
        )  
        self.label.setFixedSize(150, 30) 

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        text = f'x: {x}, y: {y}'
        
        self.label.setText(text)
        self.label.move(x + 10, y + 10) 


def main():
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
