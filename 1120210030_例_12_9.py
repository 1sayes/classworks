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

if __name__=="__main__":
    student_name1 = "小明"
    student_class1=student()
    print("======{}的一天=====".format(student_name1))
    student_class1.eat(student_name1,"一食堂")
    student_class1.gotoclass(student_name1,"一教","python")
    student_class1.dosports(student_name1,"操场","跑步")
