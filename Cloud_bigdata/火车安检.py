a = True
b = 10
if a:
    print("车票检查通过，开始准备安检")
    if b > 20:
        print("刀太长了")
        print("不允许上车")
    else:
        print("安检通过，一路顺风")
else:
    print("没有票，不能上车")
