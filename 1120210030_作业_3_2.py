#作业1(1-n的阶乘)
x=1
n=int(input("请输入一个正整数："))
for i in range(1,n+1):
    x=x*i
print(x)

#作业2(计算全部水仙花数）
for flower in range (100,1000):
    a=flower//100
    b=flower//10%10
    c=flower%10
    if flower==a**3+b**3+c**3:
        print(flower)


        
#作业3
test=int(input("请输入一个大于1的整数："))
for i in range(2,test):
    if test%i==0:
        print("不是素数")
        break
else:
        print("是素数")

#作业4（循环五次计算的小游戏）

import math
import random
compute01 = random.randint(0, 100)
compute02 = random.randint(0, 100)
print("数字1：{}，数字2：{}".format(compute01, compute02))
start = int(input("输入结果："))
count=1
sum=0
while  count<5:
    if start==compute01+compute02 :
        print("正确")
        sum += 1
    else:
        print("错误")
    compute01 = random.randint(0, 100)
    compute02 = random.randint(0, 100)
    print("数字1：{}，数字2：{}".format(compute01, compute02))
    start = int(input("输入结果："))
    count+= 1

else:
    if sum>=4:
        print("正确","闯关成功")
    else:
        print("错误","闯关失败")
