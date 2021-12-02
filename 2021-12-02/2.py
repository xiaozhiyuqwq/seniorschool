#1 2 3 4 5 可以组成多少的不重复的三位数
count=0
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,6):
            if a!=b and b!=c and c!=a:
                number=a*100+b*10+c
                count+=1
                print("找到了三位数 {} 。".format(number))
print("一共找到了 {} 个不重复的三位数。".format(count))
