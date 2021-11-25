count=0
print("1,2,3,4,5 可以组成多少个不重复的三位数？")
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            if i!=j and j!=k and k!=i:
                number=i*100+j*10+k
                count=count+1
                print("计算出三位数{}。".format(number))
print("一共可以组成{}个。".format(count))
