file_path = "output.txt"

# Режим 'w' (Write) — Полная перезапись. Если файл был, он удалится и создастся заново.
with open(file_path, "w") as f:
    f.write("Initial content.\n")

# Режим 'a' (Append) — Дозапись. Новые данные добавятся в конец, старые останутся.
with open(file_path, "a") as f:
    f.write("Added a new line.\n") # Используем .write(), а не .append()