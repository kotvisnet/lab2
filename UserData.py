import json
USER_DATA_FILE = "users.json"
"""Функции для работы с JSON"""
def load_user_data():
    """Загружает данные пользователей из JSON-файла."""
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_user_data(data):
    """Сохраняет данные пользователей в JSON-файл."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)