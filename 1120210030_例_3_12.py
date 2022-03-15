import random
point=random.randint(1,6)
count=1
while count <=3:
    guess=int(input("输入你的猜测："))
    if guess > point:
        print("大了")
    elif guess<point:
        print("小了")
    else:
        print("猜对了")
        break
    count+=1
else:
    print("三次全错")
