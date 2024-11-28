import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import style
from UserData import UserData




# Окно регистрации
class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
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

        user_data = load_user_data()

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

# Окно планировщика задач
class TaskPlannerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Планировщик задач")
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet(style)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        title = QLabel("Ваши задачи")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        add_task_button = QPushButton("Добавить задачу")
        add_task_button.clicked.connect(self.add_task)
        layout.addWidget(add_task_button)

        remove_task_button = QPushButton("Удалить выбранную задачу")
        remove_task_button.clicked.connect(self.remove_task)
        layout.addWidget(remove_task_button)

    def add_task(self):
        task, ok = QInputDialog.getText(self, "Новая задача", "Введите текст задачи:")
        if ok and task:
            self.task_list.addItem(task)

    def remove_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")

# Основное окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
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
        self.reg_window = RegistrationWindow()
        self.reg_window.show()

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()

# Запуск приложения
data = UserData
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())



# import sys
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QMainWindow, QVBoxLayout, QGridLayout,
#     QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog
# )
# from PyQt6.QtGui import QIcon
# from PyQt6.QtCore import Qt
# import style
#
# # Хранилище пользователей (в памяти, для демонстрации)
# user_data = {}
#
#
#
# # Окно регистрации
# class RegistrationWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Регистрация")
#         self.setGeometry(400, 400, 300, 200)
#         self.setStyleSheet(style)
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         title = QLabel("Регистрация")
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)
#
#         self.username = QLineEdit()
#         self.username.setPlaceholderText("Имя пользователя")
#         layout.addWidget(self.username)
#
#         self.password = QLineEdit()
#         self.password.setPlaceholderText("Пароль")
#         self.password.setEchoMode(QLineEdit.EchoMode.Password)
#         layout.addWidget(self.password)
#
#         register_button = QPushButton("Зарегистрироваться")
#         register_button.clicked.connect(self.register_user)
#         layout.addWidget(register_button)
#
#     def register_user(self):
#         username = self.username.text()
#         password = self.password.text()
#
#         if not username or not password:
#             QMessageBox.warning(self, "Ошибка", "Поля логина и пароля не должны быть пустыми.")
#             return
#
#         if username in user_data:
#             QMessageBox.warning(self, "Ошибка", "Этот пользователь уже существует.")
#         else:
#             user_data[username] = password
#             QMessageBox.information(self, "Успех", "Регистрация завершена!")
#             self.close()
#
#
#
# # Окно планировщика задач
# class TaskPlannerWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Планировщик задач")
#         self.setGeometry(300, 300, 400, 300)
#         self.setStyleSheet(style)
#
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#
#         layout = QVBoxLayout(central_widget)
#
#         title = QLabel("Ваши задачи")
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)
#
#         self.task_list = QListWidget()
#         layout.addWidget(self.task_list)
#
#         add_task_button = QPushButton("Добавить задачу")
#         add_task_button.clicked.connect(self.add_task)
#         layout.addWidget(add_task_button)
#
#         remove_task_button = QPushButton("Удалить выбранную задачу")
#         remove_task_button.clicked.connect(self.remove_task)
#         layout.addWidget(remove_task_button)
#
#     def add_task(self):
#         task, ok = QInputDialog.getText(self, "Новая задача", "Введите текст задачи:")
#         if ok and task:
#             self.task_list.addItem(task)
#
#     def remove_task(self):
#         selected_item = self.task_list.currentItem()
#         if selected_item:
#             self.task_list.takeItem(self.task_list.row(selected_item))
#         else:
#             QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")
#
# # Основное окно
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Your Task Tree")
#         self.setGeometry(300, 300, 400, 200)
#         self.setStyleSheet(style)
#
#         layout = QGridLayout()
#         self.setLayout(layout)
#
#         title = QLabel("Форма входа")
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title, 0, 0, 1, 3)
#
#         register_button = QPushButton("Регистрация")
#         register_button.clicked.connect(self.open_registration)
#         layout.addWidget(register_button, 1, 1)
#
#         login_button = QPushButton("Вход")
#         login_button.clicked.connect(self.open_login)
#         layout.addWidget(login_button, 1, 2)
#
#     def open_registration(self):
#         self.reg_window = RegistrationWindow()
#         self.reg_window.show()
#
#     def open_login(self):
#         self.login_window = LoginWindow()
#         self.login_window.show()
#
# # Запуск приложения
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())


# import sys
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QDialog, QLineEdit, QLabel, QPushButton,
#     QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox, QWidget, QInputDialog
# )
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QFont
#
# # Пользовательские данные (имитация базы данных)
# user_data = {}
#
#
# class RegistrationDialog(QDialog):
#     """Окно регистрации нового пользователя."""
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Регистрация")
#         self.setFixedSize(300, 200)
#
#         layout = QVBoxLayout()
#
#         self.username_input = QLineEdit(self)
#         self.username_input.setPlaceholderText("Введите имя пользователя")
#         self.password_input = QLineEdit(self)
#         self.password_input.setPlaceholderText("Введите пароль")
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#
#         register_button = QPushButton("Зарегистрироваться", self)
#         register_button.clicked.connect(self.register_user)
#
#         layout.addWidget(QLabel("Регистрация нового пользователя:"))
#         layout.addWidget(self.username_input)
#         layout.addWidget(self.password_input)
#         layout.addWidget(register_button)
#
#         self.setLayout(layout)
#
#     def register_user(self):
#         """Регистрирует нового пользователя."""
#         username = self.username_input.text()
#         password = self.password_input.text()
#
#         if not username or not password:
#             QMessageBox.warning(self, "Ошибка", "Имя пользователя и пароль не могут быть пустыми.")
#             return
#
#         if username in user_data:
#             QMessageBox.warning(self, "Ошибка", "Имя пользователя уже занято.")
#         else:
#             user_data[username] = password
#             QMessageBox.information(self, "Успех", "Вы успешно зарегистрированы!")
#             self.accept()
#
#
# class LoginDialog(QDialog):
#     """Окно входа в приложение."""
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Вход")
#         self.setFixedSize(300, 200)
#
#         layout = QVBoxLayout()
#
#         self.username_input = QLineEdit(self)
#         self.username_input.setPlaceholderText("Введите имя пользователя")
#         self.password_input = QLineEdit(self)
#         self.password_input.setPlaceholderText("Введите пароль")
#         self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
#
#         login_button = QPushButton("Войти", self)
#         login_button.clicked.connect(self.login_user)
#
#         layout.addWidget(QLabel("Вход для зарегистрированных пользователей:"))
#         layout.addWidget(self.username_input)
#         layout.addWidget(self.password_input)
#         layout.addWidget(login_button)
#
#         self.setLayout(layout)
#         self.is_authenticated = False
#
#     def login_user(self):
#         """Проверяет учетные данные и аутентифицирует пользователя."""
#         username = self.username_input.text()
#         password = self.password_input.text()
#
#         if user_data.get(username) == password:
#             QMessageBox.information(self, "Успех", "Вы вошли в систему!")
#             self.is_authenticated = True
#             self.accept()
#         else:
#             QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")
#
#
# class TaskPlannerApp(QMainWindow):
#     """Основное приложение для планирования задач."""
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Программа для планирования дня")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#
#         self.init_ui()
#
#     def init_ui(self):
#         """Создание интерфейса главного окна."""
#         layout = QVBoxLayout(self.central_widget)
#
#         # Заголовок
#         title_label = QLabel("Планировщик задач", self)
#         title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
#         title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title_label)
#
#         # Список задач
#         self.task_list = QListWidget(self)
#         layout.addWidget(self.task_list)
#
#         # Панель с кнопками
#         button_layout = QHBoxLayout()
#
#         add_task_button = QPushButton("Добавить задачу", self)
#         add_task_button.clicked.connect(self.add_task)
#
#         remove_task_button = QPushButton("Удалить задачу", self)
#         remove_task_button.clicked.connect(self.remove_task)
#
#         button_layout.addWidget(add_task_button)
#         button_layout.addWidget(remove_task_button)
#         layout.addLayout(button_layout)
#
#         # Стиль приложения
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: #f0f4f8;
#             }
#             QLabel {
#                 color: #2c3e50;
#             }
#             QPushButton {
#                 background-color: #3498db;
#                 color: white;
#                 border: none;
#                 padding: 8px 12px;
#                 border-radius: 5px;
#             }
#             QPushButton:hover {
#                 background-color: #2980b9;
#             }
#             QListWidget {
#                 background-color: #ecf0f1;
#                 border: 1px solid #bdc3c7;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#         """)
#
#     def add_task(self):
#         """Добавляет новую задачу."""
#         task, ok = QInputDialog.getText(self, "Добавить задачу", "Введите описание задачи:")
#         if ok and task.strip():
#             self.task_list.addItem(task.strip())
#
#     def remove_task(self):
#         """Удаляет выбранную задачу."""
#         selected_item = self.task_list.currentItem()
#         if selected_item:
#             self.task_list.takeItem(self.task_list.row(selected_item))
#         else:
#             QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")
#
#
# def main():
#     """Главная функция для запуска приложения."""
#     app = QApplication(sys.argv)
#
#     # login_dialog = LoginDialog()
#
#     # # Показываем окно регистрации или входа
#     # while True:
#     #     dialog_choice = QMessageBox.question(
#     #         None,
#     #         "Вход или регистрация",
#     #         "Вы хотите войти или зарегистрироваться?",
#     #         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
#     #         QMessageBox.StandardButton.Yes
#     #     )
#     #
#     #     if dialog_choice == QMessageBox.StandardButton.Yes:  # Вход
#     #         login_dialog = LoginDialog()
#     #         if login_dialog.exec() == QDialog.DialogCode.Accepted and login_dialog.is_authenticated:
#     #             break
#     #     else:  # Регистрация
#     #         registration_dialog = RegistrationDialog()
#     #         registration_dialog.exec()
#
#     # Показываем основное окно после успешного входа
#     planner_app = TaskPlannerApp()
#     planner_app.show()
#     sys.exit(app.exec())
#
#
# if __name__ == "__main__":
#     main()
#
#
