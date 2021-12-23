#输入
num1=int(input("在此键入一共非零自然数......"))
num2=int(input("在此键入一共非零自然数......"))
#判断
m=max(num1,num2)
n=min(num1,num2)
#mn赋值完成
while m%n:
    m,n=n,m%n
print(n)
#这个有点蒙，靠抄，注意弄懂
