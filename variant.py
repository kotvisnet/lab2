# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
#     QPushButton, QLineEdit, QListWidget, QDialog, QLabel,
#     QFormLayout, QDialogButtonBox, QMessageBox
# )
# from PyQt6.QtGui import QFont, QIcon
#
#
# class TaskManager:
#     """Класс для управления задачами."""
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task: str):
#         """Добавляет задачу в список."""
#         self.tasks.append(task)
#
#     def remove_task(self, task: str):
#         """Удаляет задачу из списка."""
#         if task in self.tasks:
#             self.tasks.remove(task)
#
#     def get_tasks(self):
#         """Возвращает список задач."""
#         return self.tasks
#
#
# class AddTaskDialog(QDialog):
#     """Диалоговое окно для добавления новой задачи."""
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Добавить задачу")
#         self.setGeometry(400, 400, 300, 200)
#
#         self.task_input = QLineEdit(self)
#         self.task_input.setPlaceholderText("Введите описание задачи")
#
#         # Кнопки для подтверждения или отмены
#         buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
#         buttons.accepted.connect(self.accept)
#         buttons.rejected.connect(self.reject)
#
#         # Layout
#         layout = QVBoxLayout(self)
#         layout.addWidget(QLabel("Описание задачи:"))
#         layout.addWidget(self.task_input)
#         layout.addWidget(buttons)
#
#     def get_task(self):
#         """Возвращает введенную задачу."""
#         return self.task_input.text()
#
#
# class TaskPlannerApp(QMainWindow):
#     """Основное окно приложения для планирования дня."""
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Программа для планирования дня")
#         self.setGeometry(100, 100, 600, 400)
#         self.setWindowIcon(QIcon("calendar_icon.png"))
#
#         # Создание экземпляра менеджера задач
#         self.task_manager = TaskManager()
#
#         # Создание главного виджета
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#
#         # Создание пользовательского интерфейса
#         self.init_ui()
#
#     def init_ui(self):
#         """Инициализация пользовательского интерфейса."""
#         layout = QVBoxLayout(self.central_widget)
#
#         # Заголовок
#         title = QLabel("Планировщик задач", self)
#         title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)
#
#         # Список задач
#         self.task_list = QListWidget(self)
#         self.task_list.setStyleSheet("""
#             QListWidget {
#                 border: 1px solid #ddd;
#                 border-radius: 5px;
#                 font-size: 14px;
#                 background-color: #f9f9f9;
#             }
#             QListWidget::item {
#                 padding: 10px;
#             }
#             QListWidget::item:hover {
#                 background-color: #ecf0f1;
#             }
#             QListWidget::item:selected {
#                 background-color: #3498db;
#                 color: white;
#             }
#         """)
#         layout.addWidget(self.task_list)
#
#         # Панель с кнопками
#         button_layout = QHBoxLayout()
#
#         # Кнопка "Добавить задачу"
#         add_button = QPushButton("Добавить задачу", self)
#         add_button.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; border-radius: 5px;")
#         add_button.clicked.connect(self.open_add_task_dialog)
#         button_layout.addWidget(add_button)
#
#         # Кнопка "Удалить задачу"
#         remove_button = QPushButton("Удалить задачу", self)
#         remove_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; border-radius: 5px;")
#         remove_button.clicked.connect(self.remove_task)
#         button_layout.addWidget(remove_button)
#
#         layout.addLayout(button_layout)
#
#         # Загрузить задачи из менеджера
#         self.load_tasks()
#
#     def open_add_task_dialog(self):
#         """Открывает диалоговое окно для добавления задачи."""
#         dialog = AddTaskDialog()
#         if dialog.exec() == QDialog.DialogCode.Accepted:
#             task = dialog.get_task()
#             if task:
#                 self.task_manager.add_task(task)
#                 self.load_tasks()
#
#     def load_tasks(self):
#         """Загружает задачи из менеджера и отображает их в списке."""
#         self.task_list.clear()
#         for task in self.task_manager.get_tasks():
#             self.task_list.addItem(task)
#
#     def remove_task(self):
#         """Удаляет выбранную задачу."""
#         selected_item = self.task_list.currentItem()
#         if selected_item:
#             task = selected_item.text()
#             self.task_manager.remove_task(task)
#             self.load_tasks()
#         else:
#             self.show_message("Ошибка", "Выберите задачу для удаления.")
#
#     def show_message(self, title, message):
#         """Показывает сообщение пользователю."""
#         msg_box = QMessageBox(self)
#         msg_box.setWindowTitle(title)
#         msg_box.setText(message)
#         msg_box.setIcon(QMessageBox.Icon.Warning)
#         msg_box.exec()
#
#
# def main():
#     """Запуск приложения."""
#     app = QApplication(sys.argv)
#     planner_app = TaskPlannerApp()
#     planner_app.show()
#     sys.exit(app.exec())
#
#
# if __name__ == "__main__":
#     main()













#
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
#     # Показываем окно регистрации или входа
#     while True:
#         dialog_choice = QMessageBox.question(
#             None,
#             "Вход или регистрация",
#             "Вы хотите войти или зарегистрироваться?",
#             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
#             QMessageBox.StandardButton.Yes
#         )
#
#         if dialog_choice == QMessageBox.StandardButton.Yes:  # Вход
#             login_dialog = LoginDialog()
#             if login_dialog.exec() == QDialog.DialogCode.Accepted and login_dialog.is_authenticated:
#                 break
#         else:  # Регистрация
#             registration_dialog = RegistrationDialog()
#             registration_dialog.exec()
#
#     # Показываем основное окно после успешного входа
#     planner_app = TaskPlannerApp()
#     planner_app.show()
#     sys.exit(app.exec())
#
#
# if __name__ == "__main__":
#     main()