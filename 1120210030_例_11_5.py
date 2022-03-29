import random
def zhufuyu():
    word_list=["万事如意","事事顺心","福寿安康","笑口常开","恭喜发财","步步高升","心想事成"]
    word1,word2=random.sample(word_list,2)
    return word1,word2
zhufu1,zhufu2=zhufuyu()
print("过年好，祝您{},{}".format(zhufu1,zhufu2))
