import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())


