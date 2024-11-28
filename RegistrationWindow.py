from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from UserData import load_user_data, save_user_data
from style import style

# Окно регистрации
class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("apple.jpg"))
        self.setWindowTitle("Регистрация")
        self.setGeometry(400, 400, 300, 200)
        self.setStyleSheet(style)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("Регистрация")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        register_button = QPushButton("Зарегистрироваться")
        register_button.clicked.connect(self.register_user)
        layout.addWidget(register_button)

    def register_user(self):
        username = self.username.text()
        password = self.password.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Поля логина и пароля не должны быть пустыми.")
            return

        user_data = load_user_data()

        if username in user_data:
            QMessageBox.warning(self, "Ошибка", "Этот пользователь уже существует.")
        else:
            user_data[username] = password
            save_user_data(user_data)
            QMessageBox.information(self, "Успех", "Регистрация завершена!")
            self.close()