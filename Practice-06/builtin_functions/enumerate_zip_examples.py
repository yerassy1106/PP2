names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# enumerate: индекс + значение
print("--- Enumerate ---")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# zip: объединение списков
print("\n--- Zip ---")
for name, score in zip(names, scores):
    print(f"Student: {name}, Score: {score}")

# Type conversion
print("\n--- Type Conversion ---")
x = "100"
print(f"String to int: {int(x) + 50}")