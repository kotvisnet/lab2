from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("apple.jpg"))
        self.setWindowTitle("Your task tree")
        self.setContentsMargins(20, 20, 20, 20)

        layout = QGridLayout()
        self.setLayout(layout)

        self.label1 = QLabel("Username: ")
        layout.addWidget(self.label1, 0, 0)

        self.label2 = QLabel("Password: ")
        layout.addWidget(self.label2, 1, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 0, 1)

        self.input2 = QLineEdit()
        layout.addWidget(self.input2, 1, 1)

        button = QPushButton("Submit")
        button.setFixedWidth(50)
        button.clicked.connect(self.display)
        layout.addWidget(button, 2, 1, Qt.AlignmentFlag.AlignRight)

    def display(self):
        print(self.input1.text())
        print(self.input2.text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())