import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Week 2 : Layout - User Registration Form')
        self.setGeometry(200, 200, 400, 400)

        identity_group = QGroupBox('Identitas (vertical box layout)')
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel('Nama  : Baiq Sindi Hanjani'))
        identity_layout.addWidget(QLabel('NIM   : F1D022115'))
        identity_layout.addWidget(QLabel('Kelas : D'))
        identity_group.setLayout(identity_layout)

        navigation_group = QGroupBox('Navigation (horizontal box layout)')
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton('Home'))
        navigation_layout.addWidget(QPushButton('About'))
        navigation_layout.addWidget(QPushButton('Contact'))
        navigation_group.setLayout(navigation_layout)

        registration_group = QGroupBox('User Registration (form layout)')
        registration_layout = QFormLayout()
        registration_layout.addRow('Full Name:', QLineEdit())
        registration_layout.addRow('Email:', QLineEdit())
        registration_layout.addRow('Phone:', QLineEdit())

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton('Male'))
        gender_layout.addWidget(QRadioButton('Female'))
        registration_layout.addRow('Gender:', gender_layout)

        country_combo = QComboBox()
        country_combo.addItems(['Select Country', 'Indonesia', 'Malaysia', 'Singapore', 'Korea', 'Jepang','Brazil', 'others'])
        registration_layout.addRow('Country:', country_combo)

        registration_group.setLayout(registration_layout)

        actions_group = QGroupBox('Actions (horizontal box layout)')
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton('Submit'))
        actions_layout.addWidget(QPushButton('Cancel'))
        actions_group.setLayout(actions_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(identity_group)
        main_layout.addWidget(navigation_group)
        main_layout.addWidget(registration_group)
        main_layout.addWidget(actions_group)

        self.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
