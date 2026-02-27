# generators.py

# 1. Generator squares up to N
print("1️⃣ Squares up to N")

def square_generator(N):
    for i in range(N + 1):
        yield i * i

for value in square_generator(5):
    print(value)


# 2. Even numbers between 0 and n (comma separated)
print("\n2️⃣ Even numbers up to n")
n = int(input("Enter n: "))

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print(",".join(str(num) for num in even_numbers(n)))


# 3. Numbers divisible by 3 and 4
print("\n3️⃣ Divisible by 3 and 4")

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(100):
    print(num)


# 4. Generator squares from a to b
print("\n4️⃣ Squares from a to b")

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for num in squares(3, 7):
    print(num)


# 5. Countdown generator
print("\n5️⃣ Countdown from n to 0")

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)