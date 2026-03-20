import shutil
import os

source = "sample.txt"
destination = "sample_backup.txt"

# Копирование
if os.path.exists(source):
    shutil.copy(source, destination)
    print(f"backup created: {destination}")

# Удаление (будь осторожен!)
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("Temporary file deleted.")