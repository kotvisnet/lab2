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
