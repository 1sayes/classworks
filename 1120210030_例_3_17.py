while 1:
    password=input("请输入密码：")
    if len(password)<6:
        print("密码长度为6，重新输入")
        continue
    if password=="123456":
        print("密码正确")
    else:
        print("密码错误")
