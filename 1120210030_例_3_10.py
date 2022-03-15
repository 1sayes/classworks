import random
games=10
for i in range(games):
    print("进行第{}场游戏".format(i+1))
    result=random.randint(0,1)
    if result==1:
        print("炫耀战绩")
    else:
        print("沉默")
print("*"*20)
