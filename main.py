from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys

"""Окно входа и регистрации"""
class Window(QWidget):
    def __init__(self):
        super().__init__()
        """Создание макета"""
        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        self.setWindowIcon(QIcon("apple.jpg"))
        self.setWindowTitle("Your task tree")
        self.setLayout(layout)

        """Создание основных виджетов"""
        title = QLabel("Login Form")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        user = QLabel("Username: ")
        layout.addWidget(user, 1, 0)

        pwd = QLabel("Password")
        layout.addWidget(pwd, 2, 0)

        """Поля ввода"""
        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 1, 1, 1, 2)

        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input2, 2, 1, 1, 2)

        button1 = QPushButton("Register")
        layout.addWidget(button1, 3, 1)

        button2 = QPushButton("Login")
        layout.addWidget(button2, 3, 2)


app = QApplication(sys.argv)

"""Применение ко всему приложению
    window.setStyleSheet() - к одному окну"""

app.setStyleSheet("""
    QWidget  {
        background-color: "pink";
        colour: "brown";
    }
    
    QLineEdit {
        background-color: "white";
    }
    
    QPushButton {
        font-size: 16px;
    }
    
""")

window = Window()
window.show()
sys.exit(app.exec())


