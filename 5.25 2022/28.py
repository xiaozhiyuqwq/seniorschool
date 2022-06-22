#二、操作题
#下面是利用欧几里得辗转相除法求两数最大公约数的部分代码,请分析并完善该代码。
a=int(input("请输入正整数a:"))
b=int(input("请输入正整数b:"))
if a<b:     				#如果a<b,则交换变量,使得a>b
    a,b=b,a  				#如果a<b,则交换变量,使得a>b
def gcdloop(a,b):
    while a%b!=0:			#构造循环迭代条件
        rem=a%b    		#求余数
        a=b
        b=rem	#构造新的除数
    return rem  			#返回最大公约数
#程序运行的结果
print("{0}和{1}的最大公约数是{2}".format(a,b,gcdloop(a,b)))
