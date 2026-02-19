def show_numbers(*args):
    for num in args:
        print(num)

def show_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_numbers(1, 2, 3, 4)

show_user(name="Erasyl", age=20, city="Almaty")
