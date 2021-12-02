#7过
while True:
    number=int(input("请输入一个正整数，不超过100......"))
    if 0<number<100:
        for i in range(1,number+1):
            if i%10==7:
                print("pass")
            elif i//10%10==7:
                print("pass")
            elif i%7==0:
                print("pass")
            else:
                print(i)
        break
    else:
        print("输入非法")

