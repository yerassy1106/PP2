class Father:
    def skills1(self):
        print("Programming")

class Mother:
    def skills2(self):
        print("Design")

class Child(Father, Mother):
    pass

child = Child()
child.skills1()
child.skills2()  
