friend_list=["马云","马化腾","王健林","李彦宏"]
for friend in friend_list:
    print("{},好哥们，谢谢你们！".format(friend))
friend_list[-1]="许家印"
for friend in friend_list:
    print("{},好哥们，谢谢你们！".format(friend))
