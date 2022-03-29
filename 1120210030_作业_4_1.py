print("今天是我的生日。")
print("我在一周前就和我的好朋友们说好了，让他们来参加我的生日派对。")
friend_list1=["fan"]
friend_list2=["biao"]
friend_list3=["hao","yang","bo"]
friend_list=friend_list3+friend_list2+friend_list1
print("我的好朋友有{}个","第一个好朋友是{}","第二个好朋友是{}","剩下的好朋友是{}。".format(len(friend_list)),friend_list1,friend_list2,friend_list3)
print("当然，如果按名字排序的话，那就是{}。".format(sorted(friend_list)))
print("但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为".format(friend_list3[0]))
friend_lists=(sorted(friend_list))
del friend_lists[3]
print(friend_lists)
print("那我只能把他从我的名单中删除了。现在只剩{}".format(friend_lists))
print("人数好像有些不够啊,那我再叫一些人来吧。对了，把{}和{}叫过来好了.".format(friend_lists.append("yue"),friend_lists.insert(0,"liu")))
print("这样的话，就有这些人来了{}".format(friend_lists))
