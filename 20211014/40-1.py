#输入
x=int(input("在此输入任意整数......"))
#先排除0这个奇怪的数字
if x==0:
    print(x,"既不属于奇数，又不属于偶数......")
#如果任意一个数字可以被2除没有余数则为偶数
elif x%2==0:
    print(x,"属于偶数......")
#反之奇数
else:
    print(x,"属于奇数......")
print("\n\n\n\n轻触回车以退出......")
#阿巴阿巴阿巴阿巴
#by xiaozhiyuqwq.top
#https://xiaozhiyuqwq.top
