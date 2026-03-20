import shutil
import os

# Перемещение файла (или переименование)
if os.path.exists("sample_backup.txt"):
    os.makedirs("backups", exist_ok=True)
    shutil.move("sample_backup.txt", "backups/sample_backup_v1.txt")
    print("The file has been moved to the backups folder.")