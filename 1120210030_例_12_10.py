class person:

    def eat(self,name,place):
        print("{}在{}吃饭".format(name,place))
    def sleep(self,name,place):
        print("{}在{}睡觉".format(name,place))
    def dosports(self,name,place,sport_place):
        print("{}在{}{}".format(name,place,sport_place))

class student(person):
    def gotoclass(self,name,place,class_name):
        print("{}在{}上{}课".format(name,place,class_name))
class worker(person):
    def gotowork(self,name,place):
        print("{}在{}开会".format(name,place))

if __name__=="__main__":
    worker1 = "小罗"
    worker_class1=worker()
    print("======{}的一天=====".format(worker1))
    worker_class1.eat(worker1,"一食堂")
    worker_class1.gotowork(worker1,"华为")
    worker_class1.dosports(worker1,"操场","跑步")
