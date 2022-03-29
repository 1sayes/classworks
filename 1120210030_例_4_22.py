import random
import time
player_list=['carol','david','ann','bob','eve','grace','monica','frank','heidi','judy']
print("游戏开始啦，共有{}个玩家！".format(len(player_list)))
print("他们分别是{}".format(",".join(player_list)))
print("所有人请按顺序排成一个圈！")
player_list.sort()
print("ok,排好序了。{}\n".format(player_list))

count=0
while (len(player_list)>1):
    count+=1
    print("第{}轮开始了，花在{}手上".format(count,player_list[0]))
    print("开始击鼓咯")
    badluck_number=random.randint(0,len(player_list)-1)
    print("咚"*badluck_number)

    badguy_name=player_list.pop(badluck_number)

    print("鼓声停了，一共敲了{}下，花到了{}手上，可怜的{}被淘汰啦！".format(badluck_number,badguy_name,badguy_name))
    print("剩下{}名玩家，他们是{}\n".format(len(player_list),player_list))
    time.sleep(5)
else:
    luckguy_number=player_list.pop()
    print("最后的胜者是{}，让我们恭喜他吧！".format(luckguy_number))
