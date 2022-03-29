def fees(water):
    results=""
    if water<=220:
        results=water*3.45
    elif water<=300:
        results=(water-220)*4.83+220*3.45
    else:
        results=(water-300)*5.83+80*4.83+220*3.45
    return results
while True:
    water=float(input("请输入用水量（立方米）："))
    results = fees(water)
    print("水费为：{}元".format(results))
