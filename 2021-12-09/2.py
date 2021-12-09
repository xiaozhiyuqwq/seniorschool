def f(num):
    if num>0:
        list=[]
        while num>0:
            x=num%10
            list.append(x)
            num=num//10
        return list
    else:
        print("Erroe")
num=int(input("在此输入一个大于 0 的整数。\n"))
A=f(num)
print(A)
