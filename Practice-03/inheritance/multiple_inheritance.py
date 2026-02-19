class Father:
    def skills(self):
        print("Programming")

class Mother:
    def skills(self):
        print("Design")

class Child(Father, Mother):
    pass

child = Child()
child.skills()  
