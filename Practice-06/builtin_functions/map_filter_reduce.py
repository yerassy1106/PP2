from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map: возведение в квадрат
squares = list(map(lambda x: x**2, nums))

# filter: только четные
evens = list(filter(lambda x: x % 2 == 0, nums))

# reduce: сумма всех элементов
total_sum = reduce(lambda x, y: x + y, nums)

print(f"Original: {nums}")
print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"Sum: {total_sum}")