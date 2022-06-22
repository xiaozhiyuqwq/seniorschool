while True:
    x=int(input("在此键入任意非 0 自然数......"))
    if x<=0:
        print("error")
    elif x%2==0:
        print("您输入的 {} 是一个偶数。".format(x))
        break
    else:
        print("您输入的 {} 是一个奇数。".format(x))
        break
#P.S.稍微完善了一下
