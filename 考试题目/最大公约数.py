#请不要更改源程序的结构，删除原题里的①、②、③。填写正确的代码，使程序完善
num1=int(input('请输入第一个正整数：'))
num2=int(input('请输入第二个正整数：'))
m=max(num1,num2)
n=min(num1,num2)
r=m % n
while r!=0:
    m=n
    n=r
    r=m % n
print('这两个数的最大公约数为：',n)
input("运行完毕，请按回车键退出...") 
