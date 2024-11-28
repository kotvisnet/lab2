from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QInputDialog, QMessageBox
from style import style


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
