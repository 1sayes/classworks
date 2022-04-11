class ANIMAL:
    zhonglei1="家庭宠物"
    def __init__(self,name):
        self.name=name

    def eat(self, name, place):
        print("{}在{}吃饭".format(name, place))
    def jump(self, name, place):
        print("{}在{}跳".format(name, place))
class CAT(ANIMAL):
    def miaomiaobark(self, name, place):
        print("{}在{}喵喵叫".format(name, place))
class DOG(ANIMAL):
    def wangwangjiao(self,name,place):
        print("{}在{}汪汪叫".format(name,place))
cat1=CAT("小黑猫")
dog1=DOG("小黄狗")

print("小猫1的种类是：{}".format(cat1.zhonglei1))
print("小狗1的种类是：{}".format(dog1.zhonglei1))
print("小猫1的姓名是：{}".format(cat1.name))
print("小狗1的姓名是：{}".format(dog1.name))

cat1.miaomiaobark("小蓝猫","沙发上")
dog1.wangwangjiao("小黄狗","家门口")
