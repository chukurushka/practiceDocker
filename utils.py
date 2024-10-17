import os
import json

# Указываем директорию для хранения файлов данных
DATA_DIR = '/app/data'

# Функция загрузки пользователей из JSON-файла
def load_users():
    global users
    try:
        # Загружаем пользователей из файла в директории /app/data
        with open(os.path.join(DATA_DIR, "users.json"), "r", encoding="utf-8") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

# Функция сохранения пользователей в JSON-файл
def save_users():
    with open(os.path.join(DATA_DIR, "users.json"), "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

# Функция загрузки покупок из JSON-файла
def load_purchases():
    global purchases
    try:
        # Загружаем покупки из файла в директории /app/data
        with open(os.path.join(DATA_DIR, "purchases.json"), "r", encoding="utf-8") as f:
            purchases = json.load(f)
    except FileNotFoundError:
        purchases = []

# Функция сохранения покупок в JSON-файл
def save_purchases():
    with open(os.path.join(DATA_DIR, "purchases.json"), "w", encoding="utf-8") as f:
        json.dump(purchases, f, ensure_ascii=False, indent=4)
