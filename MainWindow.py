from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from RegistrationWindow import RegistrationWindow
from LoginWindow import LoginWindow
from style import style

class MainWindow(QWidget):
    """Класс для создания основного окна"""
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("apple.jpg"))
        self.setWindowTitle("Your Task Tree")
        self.setGeometry(300, 300, 400, 200)
        self.setStyleSheet(style)

        layout = QGridLayout()
        self.setLayout(layout)

        title = QLabel("Форма входа")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title, 0, 0, 1, 3)

        register_button = QPushButton("Регистрация")
        register_button.clicked.connect(self.open_registration)
        layout.addWidget(register_button, 1, 1)

        login_button = QPushButton("Вход")
        login_button.clicked.connect(self.open_login)
        layout.addWidget(login_button, 1, 2)

    def open_registration(self):
        """Функция для открытия поля регистации"""
        self.reg_window = RegistrationWindow()
        self.reg_window.show()

    def open_login(self):
        """Функция для открытия поля входа"""
        self.login_window = LoginWindow()
        self.login_window.show()

