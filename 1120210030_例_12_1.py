class dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print("{}发出汪汪的声音".format(self.name))
    def eat(self):
        print("{}吃骨头".format(self.name))

d1=dog("小黑")
d1.bark()
d1.eat()
