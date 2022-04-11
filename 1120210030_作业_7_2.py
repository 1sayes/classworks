class ANIMAL:
    zhonglei1="布偶猫"
    def __init__(self,name):
        self.name=name

    def eat(self, name, place):
        print("{}在{}吃饭".format(name, place))
    def jump(self, name, place):
        print("{}在{}跳".format(name, place))




class CAT(ANIMAL):
    def miaomiaobark(self, name, place):
        print("{}在{}喵喵叫".format(name, place))

cat1=ANIMAL("小蓝猫")
cat2=ANIMAL("小红猫")
cat3=CAT("小白猫")
print("小猫1的种类是：{}".format(cat1.zhonglei1))
print("小猫2的种类是：{}".format(cat2.zhonglei1))
print("小猫3的姓名是：{}".format(cat3.name))

cat3.eat("小白猫","厨房")
cat2.jump("小红猫","客厅")
cat3.miaomiaobark("小蓝猫","沙发上")
