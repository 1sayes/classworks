class dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print("{}发出汪汪的声音".format(self.name))
    def eat(self):
        print("{}吃骨头".format(self.name))

d1=dog("小黄")
print(d1.bark())
print(d1.eat())
