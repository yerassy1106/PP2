class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

s = Student("Erasyl", "KBTU")
print(s.name)
print(s.university)
