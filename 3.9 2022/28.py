#2、求两个数的最大公约数。（进阶1）
num1=int(input("在此键入一个自然数1......\n"))
num2=int(input("在此键入一个自然数2......\n"))
#取值
m=max(num1,num2)
n=min(num1,num2)
#取模(余数
while m%n:
    m,n=n,m%n
print(n)
#def gys(m,n):
#    r=m%n
#    if r==0:
#        print(n)
#    else:
#        m=n
#        n=r
#        return gys(m,n)
