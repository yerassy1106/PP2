import os
from pathlib import Path

# Создание вложенных папок
dir_name = "nested/test/folder"
os.makedirs(dir_name, exist_ok=True)
print(f"directory {dir_name} ready.")

# Список файлов в текущей папке
print("Contents of the current directory:", os.listdir('.'))

# Поиск файлов по расширению (.py)
py_files = [f for f in os.listdir('.') if f.endswith('.py')]
print("Python files:", py_files)