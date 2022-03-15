import random
games=10
for i in range(games):
    print("进行第{}场游戏".format(i+1))
    feeling=random.randint(0,10)
    if 5<=feeling<=9:
        print("下一局")
        continue
    elif feeling==10:
        print("不玩了")
    else:
        print("很开心")
    result=random.randint(0,1)
    if result==1:
        print("炫耀战绩")
    else:
        print("沉默")
print("*"*20)
