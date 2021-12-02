#水仙花数
for number in range(100,1000):
    ge=number%10
    shi=number//10%10
    bai=number//100
    if number==bai**3+shi**3+ge**3:
        print("找到水仙花数 {} 。".format(number))
