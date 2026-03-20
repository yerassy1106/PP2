# Чтение файла разными методами
filename = "sample.txt"

# Создадим файл для демонстрации, если его нет
with open(filename, "w") as f:
    f.write("Line 1: Hello Python\nLine 2: File Handling\nLine 3: W3Schools Practice")

print("--- Methodread() ---")
with open(filename, "r") as f:
    print(f.read())

print("\n--- Method readline() ---")
with open(filename, "r") as f:
    print(f.readline().strip())

print("\n--- Method readlines() ---")
with open(filename, "r") as f:
    lines = f.readlines()
    print(lines)