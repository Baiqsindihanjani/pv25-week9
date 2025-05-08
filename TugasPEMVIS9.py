import sys
from PyQt5.QtWidgets import *

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget() 

        self.tabs.addTab(self.tab1, "Input Nama")
        self.tabs.addTab(self.tab2, "Pilih Font")
        self.tabs.addTab(self.tab3, "Buka File")

        self.tab1.setStyleSheet("background-color: #a9cce3;")
        self.tab2.setStyleSheet("background-color: #a9cce3;")
        self.tab3.setStyleSheet("background-color: #a9cce3;")

        self.create_tab1()
        self.create_tab2()
        self.create_tab3()
        self.create_menu()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.infoLabel = QLabel("Nama: Baiq Sindi Hanjani | NIM: F1D022115")
        self.infoLabel.setStyleSheet("color: white; font-size: 12pt; background-color: #2c3e50; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.infoLabel)

        self.central_widget.setLayout(layout)

    def create_tab1(self):
        layout = QVBoxLayout()
        self.input_button = QPushButton("Input Nama")
        self.input_button.clicked.connect(self.input_nama)
        self.input_button.setStyleSheet("""
                                        QPushButton {
                                        background-color: #2c3e50;
                                        color: white;
                                        padding: 8px 16px;
                                        border-radius: 8px;
                                        font-weight: bold;
                                        }
                                        QPushButton:hover {background-color: #1a252f;}
                                        """)
        self.label_nama = QLabel("Nama: ")
        layout.addWidget(self.input_button)
        layout.addWidget(self.label_nama)
        self.tab1.setLayout(layout)

    def create_tab2(self):
        layout = QVBoxLayout()
        self.font_button = QPushButton("Pilih Font")
        self.font_button.clicked.connect(self.pilih_font)
        self.font_button.setStyleSheet("""
                                        QPushButton {
                                        background-color: #2c3e50;
                                        color: white;
                                        padding: 8px 16px;
                                        border-radius: 8px;
                                        font-weight: bold;
                                        }
                                        QPushButton:hover {background-color: #1a252f;}
                                        """)
        self.label_font = QLabel("Nama: ")
        layout.addWidget(self.font_button)
        layout.addWidget(self.label_font)
        self.tab2.setLayout(layout)

    def create_tab3(self):
        layout = QVBoxLayout()
        self.file_button = QPushButton("Buka File .txt")
        self.file_button.clicked.connect(self.buka_file)
        self.file_button.setStyleSheet("""
                                        QPushButton {
                                        background-color: #2c3e50;
                                        color: white;
                                        padding: 8px 16px;
                                        border-radius: 8px;
                                        font-weight: bold;
                                        }
                                        QPushButton:hover {background-color: #1a252f;}
                                        """)
        self.file_text = QTextEdit()
        self.file_text.setStyleSheet("background-color: white;")
        layout.addWidget(self.file_button)
        layout.addWidget(self.file_text)
        self.tab3.setLayout(layout)

    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        fitur_menu = menubar.addMenu("Fitur")

        keluar_action = QAction("Keluar", self)
        keluar_action.triggered.connect(self.close)
        file_menu.addAction(keluar_action)

        input_action = QAction("Input Nama", self)
        input_action.triggered.connect(lambda: self.tabs.setCurrentIndex(0))
        font_action = QAction("Pilih Font", self)
        font_action.triggered.connect(lambda: self.tabs.setCurrentIndex(1))
        file_action = QAction("Buka File", self)
        file_action.triggered.connect(lambda: self.tabs.setCurrentIndex(2))

        fitur_menu.addAction(input_action)
        fitur_menu.addAction(font_action)
        fitur_menu.addAction(file_action)

    def input_nama(self):
        nama, ok = QInputDialog.getText(self, "Input Nama", "Masukkan Nama:")
        if ok and nama:
            self.label_nama.setText(f"Nama: {nama}")
            self.label_font.setText(nama)

    def pilih_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_font.setFont(font)

    def buka_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.file_text.setText(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
