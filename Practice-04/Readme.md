Practice 4 – Python Advanced Topics

This repository contains solutions for Practice 4.

Topics Covered

Python Iterators

Generators

Date and Time (datetime)

Math Module

Random Module

JSON Parsing and Creation

Repository Structure
Your-Repository/
├── generators.py
├── dates.py
├── math.py
├── json.py
└── README.md
📌 generators.py

Contains:

Generator that produces squares up to N

Generator for even numbers up to n

Generator for numbers divisible by 3 and 4

Generator for squares in range (a, b)

Countdown generator from n to 0

Concepts used:

yield

range()

Generator expressions

Loop iteration

📌 dates.py

Contains:

Subtract 5 days from current date

Print yesterday, today, tomorrow

Remove microseconds from datetime

Calculate difference between two dates in seconds

Concepts used:

datetime.now()

timedelta

.replace()

.total_seconds()

📌 math.py

Contains:

Degree to radian conversion

Area of trapezoid

Area of regular polygon

Area of parallelogram

Concepts used:

math.pi

math.tan()

Mathematical formulas

Basic arithmetic operations

📌 json.py

Contains:

Reading JSON file (sample-data.json)

Parsing JSON data using json.load()

Accessing nested dictionary structures

Filtering data

Writing JSON data using json.dump()

Concepts used:

JSON syntax

Dictionaries and lists

File handling

Data filtering

How to Run

Run each file separately:

python generators.py
python dates.py
python math.py
python json.py
Commit Instructions
git add .
git commit -m "Add Practice4 - Python iterators, generators, dates, math, and JSON"
git push origin main
Author

Student Name: Ibragimov Yerassyl
Course: Python Programming 2
Practice: 4