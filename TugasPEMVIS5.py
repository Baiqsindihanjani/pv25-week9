import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtCore import Qt

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setup_ui()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Q:
            self.close()

    def validate_inputs(self):
        name_input = self.name.text()
        email_input = self.email.text()
        age_input = self.age.text()
        phone_input = self.nbrphone.text()
        address_input = self.address.toPlainText()
        gender_input = self.gender.currentText()
        education_input = self.education.currentText()

        if not all([name_input.strip(), email_input.strip(), age_input.strip(),
                phone_input.strip(), address_input.strip(),
                gender_input.strip(), education_input.strip()]):
            QMessageBox.warning(self, "Input Error", "Gagal menyimpan! Semua input harus diisi.")
            return False
        
        #validasi nama
        if not re.fullmatch(r"[A-Za-z\s]+", name_input):
            QMessageBox.warning(self, "Input Error", "Nama hanya boleh berisi huruf!!")
            return False
        if len(name_input) < 5:
            QMessageBox.warning(self, "Input Error", "Nama harus terdiri dari minimal 5 huruf!!")
            return False


        # Validasi email
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email_input):
            QMessageBox.warning(self, "Input Error", "Format email harus benar (contoh: nama@email.com)")
            return False
        
        # Validasi umur
        if not age_input.isdigit():
            QMessageBox.warning(self, "Input Error", "Umur hanya boleh berisi angka!!")
            return False
        
        # Validasi nomor handphone
        number_part = phone_input[3:]

        if len(number_part) != 11:
            QMessageBox.warning(self, "Input Error", "Nomor handphone harus terdiri dari 13 digit angka")
            return False

        return True
    
    def on_save_clicked(self):
            if self.validate_inputs():
                QMessageBox.information(self, "Berhasil", "Data berhasil disimpan!")
                self.clear_fields()

    def clear_fields(self):
        self.name.clear()
        self.email.clear()
        self.age.clear()
        self.nbrphone.clear()
        self.address.clear()
        self.gender.setCurrentIndex(0)
        self.education.setCurrentIndex(0)


    def setup_ui(self):
        form_layout = QFormLayout()

        self.name = QLineEdit()
        self.name.setMaximumWidth(200)

        self.email = QLineEdit()
        self.email.setMaximumWidth(200)

        self.age = QLineEdit()
        self.age.setMaximumWidth(200)

        self.nbrphone = QLineEdit()
        self.nbrphone.setMaximumWidth(200)
        self.nbrphone.setInputMask("+6299999999999")

        self.address = QTextEdit()

        self.gender = QComboBox()
        self.gender.addItems(["", "Male", "Female"])
        self.gender.setMaximumWidth(200)

        self.education = QComboBox()
        self.education.addItems(["", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])
        self.education.setMaximumWidth(200)

        form_layout.addRow("Name:", self.name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Age:", self.age)
        form_layout.addRow("Phone Number:", self.nbrphone)
        form_layout.addRow("Address:", self.address)
        form_layout.addRow("Gender:", self.gender)
        form_layout.addRow("Education:", self.education)

        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")

        self.save_button.clicked.connect(self.on_save_clicked)
        self.clear_button.clicked.connect(self.clear_fields)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        self.signature_label = QLabel("Nama: Baiq Sindi Hanjani\nNIM: F1D022115")
        self.signature_label.setFont(QFont("Arial", 10))
        self.signature_label.setStyleSheet("margin-top: 10px; color: black")

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.signature_label)

        self.setLayout(main_layout)
        self.setFixedSize(400, 450)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidation()
    window.show()
    sys.exit(app.exec_())
