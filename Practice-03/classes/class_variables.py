# Class variable vs instance variable

class Employee:
    company = "TechCorp"   # Class variable

    def __init__(self, name):
        self.name = name    # Instance variable

e1 = Employee("Ali")
e2 = Employee("Dana")

print(e1.company)
print(e2.company)

# Change class variable
Employee.company = "NewTech"

print(e1.company)
print(e2.company)
