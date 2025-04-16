import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Font Size and Color Adjuster")
        self.setStyleSheet("background-color: #2c2c2c;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("F1D022115")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        layout.addWidget(self.label)

        self.fontSizeSlider = self.createSlider(20, 60, self.changeFontSize)
        layout.addLayout(self.labeledSlider("Font Size", self.fontSizeSlider))

        self.bgColorSlider = self.createSlider(0, 255, self.changeBgColor)
        layout.addLayout(self.labeledSlider("Background Color", self.bgColorSlider))

        self.fontColorSlider = self.createSlider(0, 255, self.changeFontColor)
        layout.addLayout(self.labeledSlider("Font Color", self.fontColorSlider))

        self.infoLabel = QLabel("Nama: Baiq Sindi Hanjani | NIM: F1D022115")
        self.infoLabel.setStyleSheet("color: white; font-size: 12pt;")
        layout.addWidget(self.infoLabel)

        self.setLayout(layout)

    def labeledSlider(self, label_text, slider):
        container = QVBoxLayout()
        label = QLabel(label_text)
        label.setStyleSheet("color: white;")
        container.addWidget(label)
        container.addWidget(slider)
        return container

    def createSlider(self, min_val, max_val, callback):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue((min_val + max_val) // 2)
        slider.valueChanged.connect(callback)
        return slider

    def changeFontSize(self):
        size = self.fontSizeSlider.value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def changeFontColor(self):
        val = self.fontColorSlider.value()
        self.label.setStyleSheet(f"color: rgb({val},{val},{val}); background-color: {self.label.palette().window().color().name()}")

    def changeBgColor(self):
        val = self.bgColorSlider.value()
        bg_color = f"rgb({val},{val},{val})"
        current_font_color_val = self.fontColorSlider.value()
        self.label.setStyleSheet(f"color: rgb({current_font_color_val},{current_font_color_val},{current_font_color_val}); background-color: {bg_color}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.resize(500, 300)
    window.show()
    sys.exit(app.exec_())
