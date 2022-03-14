#作业6.1(利用random求圆锥体积）
import random
radius=random.randint(1,10)
height=random.randint(1,10)
import math
vol=1/3*radius*radius*height*(math.pi)
print("圆锥的体积是:{0:.2f}".format(vol))



#作业6.2（判断闰年）
year=int(input("请输入年份："))
result=((year%4==0) and (year%100!=0))or (year%400==0)
if result:
    print("%d是闰年"%(year))
else:
    print("%d不是闰年"%(year))
 


#作业6.3（一元二次方程根存在）

import math
print("计算一元二次方程的根")
a=float(input("输入a的值："))
b=float(input("输入b的值："))
c=float(input("输入c的值："))
d=b**2-4*a*c
if d <0:
    print("x无解")
else:
    e=math.sqrt(d)
    x1=((-b+e)/2*a)
    x2=((-b-e)/2*a)
    print("x1=",x1,"\t","x2=",x2)

#作业6.4（水费计算）

water=float(input("请输入用水量（立方米）:"))
if water<=0:
    print("水费为0")
elif water<=220:
    expense=float(water*3.45)
    print("水费为%2f"%(expense))
elif water<=300:
    expense=float((r-220)*4.83+220*3.45)
    print("水费为%2f"%(ewatexpense))
else:
    expense=float((water-300)*5.83+80*4.83+220*3.45)
    print("水费为%2f"%(expense))
