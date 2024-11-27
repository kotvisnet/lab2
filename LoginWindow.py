import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
import style
# Окно входа
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(400, 400, 300, 200)
        self.setStyleSheet(style)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("Вход")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        login_button = QPushButton("Войти")
        login_button.clicked.connect(self.login_user)
        layout.addWidget(login_button)

    def login_user(self):
        username = self.username.text()
        password = self.password.text()

        if user_data.get(username) == password:
            QMessageBox.information(self, "Успех", "Добро пожаловать!")
            self.open_task_planner()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")

    def open_task_planner(self):
        """Открывает приложение планировщика задач."""
        self.task_planner = TaskPlannerWindow()
        self.task_planner.show()
        self.close()