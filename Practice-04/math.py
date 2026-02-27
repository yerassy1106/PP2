# math.py

import math

# 1. Degree to radian
print("1️⃣ Degree to Radian")
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))


# 2. Area of trapezoid
print("\n2️⃣ Area of Trapezoid")
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area_trapezoid = 0.5 * (base1 + base2) * height
print("Expected Output:", area_trapezoid)


# 3. Area of regular polygon
print("\n3️⃣ Area of Regular Polygon")
n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))

area_polygon = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area_polygon))


# 4. Area of parallelogram
print("\n4️⃣ Area of Parallelogram")
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area_parallelogram = base * height
print("Expected Output:", area_parallelogram)